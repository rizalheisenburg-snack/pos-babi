# Jakarta Cafe TMA — Rangkuman Proyek

Sistem ordering buat Jakarta Cafe lewat **Telegram Mini App (TMA)**. Customer mesen dari Mini App, owner ngurus dari chat bot Telegram. Satu cabang, satu owner.

---

## 1. Tiga Aktor

| Aktor | Lewat apa | Ngapain |
|---|---|---|
| **Customer** | Mini App (webview) | Liat menu, masukin cart, checkout, konfirm |
| **Owner** | Bot Telegram (chat) | Terima/tolak order, masak, kelar, toggle stok, liat omzet, tandai lunas |
| **Barber** | — | **Di-skip** (ga relevan buat cafe) |

**Objektif:**
- Customer: mesen low-friction, tau total + metode bayar sebelum konfirm.
- Owner: omzet per-hari & per-bulan, operasional dari HP.

---

## 2. Keputusan Desain Inti (+ alasannya)

### 💰 Semua duit dalam RIEL, integer
Base currency = Riel Kamboja. Menu dihargain riel, voucher riel, omzet riel. **Alasan:** Riel ga punya subunit (ga ada sen) → murni integer, ga ada error pembulatan desimal. USD jadi "pembayaran asing" yang dikonversi, bukan basis.

### 💵 USD pakai rate STATIS 4000
Customer boleh bayar cash/transfer USD, tapi **pembukuan selalu riel** — langsung dikonversi pakai rate tetap 4000/\$1. Ga ada input rate per-transaksi. `paid_currency` cuma nyatet duit fisik apa yang masuk (buat rekonsiliasi laci), angka di buku tetap riel.

### 🎟️ Aturan voucher (TEGAS — ini yang paling banyak direvisi)
Voucher = nilai **tetap 10.000 riel**, ga ada kembalian, ga bisa nyimpen receh.
- Belanja **> 10k** → potong 10k, sisanya bayar cash/transfer.
- Belanja **pas 10k** → total 0, **GRATIS**, auto-lunas (ini ~40% customer).
- Belanja **< 10k** → **TOPUP_REQUIRED**: "genepin sampe 10k, atau order batal." Sistem ga maksa, lempar balik ke customer.

**Alasan:** kalo voucher di-cap diam-diam (kasih gratis pas belanja < nominal), itu sama aja warung ngasih kembalian voucher = rugi tiap transaksi.

### 🍳 Pembayaran TERPISAH dari state dapur
Dapur (`PRE_CHECK → ... → DONE`) jalan sendiri, **ga pernah nungguin bayar**. `payment_status` (UNPAID/PAID) itu kolom independen, bukan state. Order diproses dulu walau belum bayar.

**Alasan:** ini sistem kepercayaan. Kalo customer ghosting (kabur ga bayar), makanan udah terlanjur dibikin = **rugi, ditanggung owner**, bukan dijaga kode. Omzet cuma ngitung yang `PAID`.

### 🕐 "Hari kerja" ikut shift, bukan tengah malam
Shift 1 (siang) 07:00–19:00, Shift 2 (malam) 19:00–07:00. Omzet harian reset jam 7 pagi.

**Trik emas:** jam 7 pagi Phnom Penh = **00:00 UTC**. Jadi kalo `paid_at` disimpan UTC, `date(paid_at)` mentah udah = hari kerja yang bener (transaksi shift malam yang nyebrang tengah malam ga bocor ke hari berikutnya). Shift dipisah dari jam UTC: `<12` = siang, `>=12` = malam. **Syarat keras: `paid_at` WAJIB UTC.**

### 🛒 Cart hidup di client, row lahir saat checkout
Cart disimpan di Mini App (client-side), **belum nyentuh DB**. Baru pas checkout, row order lahir di state `PRE_CHECK` (server validasi stok + hitung total). **Alasan:** low-friction, ga ada junk row dari cart yang ditinggal.

### 🔄 3-state dapur + window cancel
`PENDING → CONFIRMED → PREPARING → DONE` (owner 3 klik, granularitas penuh ke customer). **Cancel customer cuma boleh selagi PENDING** — begitu owner terima (CONFIRMED), window cancel tutup. Mau ngambek telat = makanan tetap dibikin, derita customer. (Edge case race ~0% sengaja ga di-kode, ditanggung owner.)

---

## 3. State Machine Dapur

```
[cart — client, no DB]
        │ checkout (INSERT row)
        ▼
   PRE_CHECK ──────────────► PARTIAL_PENDING   (system: ada item habis)
     │ confirm                  │ terima tanpa item itu
     │◄─────────────────────────┘ (recompute + cek voucher)
     ▼
  PENDING ──────► REJECTED      (owner tolak)        [terminal]
     │     └────► CANCELLED      (cust/owner, selagi  [terminal]
     │                            PENDING aja)
     │ owner terima
     ▼
 CONFIRMED   🔒 window cancel customer TUTUP di sini
     │ owner mulai masak
     ▼
 PREPARING
     │ owner kelar
     ▼
   DONE  [terminal]

PAYMENT (overlay terpisah):
UNPAID → PAID  bisa kapanpun di PENDING/CONFIRMED/PREPARING/DONE
total=0 (voucher pas) → auto-PAID saat confirm
```

---

## 4. Arsitektur Teknis

```
CUSTOMER                          OWNER
(Mini App webview)                (chat Telegram)
     │                                 ▲
     │ HTTPS                           │ push kartu order
     ▼                                 │ + tombol Terima/Tolak/Lunas
┌─────────────────────────────────────────────┐
│  VPS — main.py (1 proses, 1 event loop)      │
│  ┌──────────────┐      ┌──────────────────┐  │
│  │ aiohttp      │      │ Pyrogram bot     │  │
│  │ server :8081 │◄────►│ (owner console)  │  │
│  └──────┬───────┘      └────────┬─────────┘  │
│         └──── share ───┬────────┘            │
│                   ┌────▼─────┐               │
│                   │ SQLite   │               │
│                   └──────────┘               │
└─────────────────────────────────────────────┘
        ▲
        │ Nginx (reverse proxy, HTTPS :443 → :8081)
   cafe.rizal-wl.cloud
```

**Alur jembatan:** customer konfirm di Mini App → server `confirm()` → order masuk PENDING → server manggil `push_order_card()` → kartu nongol di chat owner. Verifikasi `initData` juga pakai token bot. **Bot = separuh sistem (sisi owner), bukan komponen terpisah.**

---

## 5. File Proyek

| File | Isi |
|---|---|
| `schema.sql` | Struktur 3 tabel: `menu_items`, `orders`, `order_items`. Kolom `total`/`line_total` = GENERATED (anti-drift). |
| `db.py` | Koneksi (foreign_keys ON, WAL, row_factory) + init. |
| `seed_menu.py` | Isi menu awal (riel). Idempotent. |
| `state_machine.py` | `can_transition()`, `can_mark_paid()`, `apply_voucher()`, `should_auto_pay()`. Pure logic, gampang dites. |
| `checkout_flow.py` | `verify_init_data()` (HMAC + anti-replay), `checkout()`, `confirm()`. |
| `owner_console.py` | Handler tombol owner (Pyrogram), `/stok`, `/omzet`, render kartu, `push_order_card()`. |
| `server.py` | Endpoint aiohttp: `/menu`, `/checkout`, `/confirm`, `/health` + serve `webapp/`. |
| `config.py` | Baca `.env`, fail-fast. |
| `.env` | Secret: `API_ID`, `API_HASH`, `BOT_TOKEN`, `OWNER_ID`, `PORT`. Jangan commit. |
| `main.py` | **ENTRY POINT** — nyalain server + bot satu proses. |
| `webapp/` | Frontend Mini App (HTML/JS) — udah jadi, render menu + cart. |

---

## 6. Keamanan

`initData` Telegram diverifikasi tiap request:
- HMAC-SHA256 pakai secret turunan dari `BOT_TOKEN` — request palsu yang ga di-sign token bot lo → ditolak 401.
- **Anti-replay:** `auth_date` lebih tua dari 24 jam → ditolak.
- Harga & stok dibaca LIVE dari DB server (bukan dari client) → customer ga bisa ngakalin harga lewat devtools.

Semua udah dites end-to-end di SQLite asli (request sah lolos, palsu & basi ditolak).

---

## 7. Status Deploy

✅ **Selesai:**
- Semua file backend + frontend dibikin & dites.
- Push ke GitHub (`rizalheisenburg-snack/jakarta-cafe-tma`).
- Clone + install di VPS, jalan sebagai systemd service (auto-restart).
- Frontend kebukti render (menu, kategori, cart) lewat IP langsung.
- Nginx terinstall + terkonfigurasi.
- DNS A record `cafe.rizal-wl.cloud` → `202.10.37.240` dibuat (setting udah bener, tinggal nunggu propagasi).

⏳ **Nunggu:**
- Propagasi DNS.

🔲 **Belum:**
- Test full flow di Telegram.
- **Receipt printing** (RawBT thermal) — adaptasi dari bot lama, belum dikerjain.

---

## 8. Catatan Penting Buat Lanjut

1. **Port: app jalan di `:8081`** (bukan 8080). Pastikan `proxy_pass` Nginx → `127.0.0.1:8081`.
2. **Urutan deploy aman:** `dig` resolve → cek Nginx (`server_name` + `proxy_pass`) → `certbot --nginx -d cafe.rizal-wl.cloud` → buka `https://cafe.rizal-wl.cloud/menu` (harus keluar JSON = checkpoint emas) → baru BotFather → test Telegram.
3. **Restart service tiap edit `.env`:** `systemctl restart jakarta-cafe`.
4. **BotFather butuh HTTPS** — Mini App ga bisa pakai `http://` atau IP+port.

---

## 9. Sisa Roadmap

- **Receipt printing** (step 5) — hook order DONE → RawBT thermal.
- **Testing portfolio QA** — `state_machine.py` itu decision table siap jadi test case pytest (validasi desain + isi portfolio sekaligus).
