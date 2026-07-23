"""Inject/replace menu Warteg Babi Kompong Dewa. Aman dijalanin ulang."""
from db import get_conn, init_db

# (name, description, price, category, emoji, image_url)
MENU = [
# ── MENU BABI ─────────────────────────────────────────────
("Ricebowl Babi / Samcan Sambal Matah", "", 12000, "Babi & Samcan", "🐷", None),
("Ricebowl Babi / Samcan Sambal Ijo", "", 12000, "Babi & Samcan", "🐷", None),
("Ricebowl Babi / Samcan Sambal Bawang", "", 12000, "Babi & Samcan", "🐷", None),
("Ricebowl Babi / Samcan Sambal Tempong", "", 12000, "Babi & Samcan", "🐷", None),
("Ricebowl Babi Rica", "", 12000, "Babi & Samcan", "🐷", None),
("Ricebowl Babi Asam Manis", "", 12000, "Babi & Samcan", "🐷", None),
("Ricebowl Babi Lada Hitam", "", 12000, "Babi & Samcan", "🐷", None),
("Ricebowl Babi Lada Garam", "", 12000, "Babi & Samcan", "🐷", None),
("Ricebowl Samcan Kecap", "", 12000, "Babi & Samcan", "🐷", None),


# ── NASI GORENG ───────────────────────────────────────────
("Nasi Goreng Telor", "", 10000, "Nasi Goreng", "🍳", None),
("Nasi Goreng Ayam", "", 12000, "Nasi Goreng", "🍳", None),
("Nasi Goreng Ikan Asin", "", 12000, "Nasi Goreng", "🍳", None),
("Nasi Goreng Ati Ampela", "", 15000, "Nasi Goreng", "🍳", None),
("Nasi Goreng Seafood", "", 15000, "Nasi Goreng", "🍳", None),
("Nasi Goreng Sapi", "", 15000, "Nasi Goreng", "🍳", None),
("Nasi Goreng Babi", "", 15000, "Nasi Goreng", "🍳", None),

# ── KWETIAU ───────────────────────────────────────────────
("Kwetiau Goreng Telor", "", 10000, "Kwetiau", "🍜", None),
("Kwetiau Goreng Ayam", "", 12000, "Kwetiau", "🍜", None),
("Kwetiau Goreng Seafood", "", 14000, "Kwetiau", "🍜", None),
("Kwetiau Goreng Sapi", "", 14000, "Kwetiau", "🍜", None),
("Kwetiau Goreng Babi", "", 14000, "Kwetiau", "🍜", None),
("Kwetiau Siram Telor", "", 10000, "Kwetiau", "🍜", None),
("Kwetiau Siram Ayam", "", 12000, "Kwetiau", "🍜", None),
("Kwetiau Siram Seafood", "", 14000, "Kwetiau", "🍜", None),
("Kwetiau Siram Sapi", "", 14000, "Kwetiau", "🍜", None),
("Kwetiau Siram Babi", "", 14000, "Kwetiau", "🍜", None),

# ── MIE GORENG ────────────────────────────────────────────
("Mie Goreng Telor", "", 10000, "Mie Goreng", "🍜", None),
("Mie Goreng Ayam", "", 12000, "Mie Goreng", "🍜", None),
("Mie Goreng Seafood", "", 14000, "Mie Goreng", "🍜", None),
("Mie Goreng Sapi", "", 14000, "Mie Goreng", "🍜", None),
("Mie Goreng Babi", "", 14000, "Mie Goreng", "🍜", None),

# ── BIHUN ─────────────────────────────────────────────────
("Bihun Goreng Telor", "", 10000, "Bihun", "🍜", None),
("Bihun Goreng Ayam", "", 12000, "Bihun", "🍜", None),
("Bihun Goreng Seafood", "", 14000, "Bihun", "🍜", None),
("Bihun Goreng Sapi", "", 14000, "Bihun", "🍜", None),
("Bihun Goreng Babi", "", 14000, "Bihun", "🍜", None),
("Bihun Siram Ayam", "", 12000, "Bihun", "🍜", None),
("Bihun Siram Seafood", "", 14000, "Bihun", "🍜", None),

# ── FUYUNGHAI ─────────────────────────────────────────────
("Fuyunghai Ayam", "", 15000, "Fuyunghai", "🍳", None),
("Fuyunghai Seafood", "", 16000, "Fuyunghai", "🍳", None),
("Fuyunghai Babi", "", 14000, "Fuyunghai", "🍳", None),

# ── SUP ───────────────────────────────────────────────────
("Sop Bakso Ikan", "", 12000, "Sup", "🍲", None),
("Sop Seafood", "", 15000, "Sup", "🍲", None),

# ── AYAM ──────────────────────────────────────────────────
("Ayam Salted Egg", "", 12000, "Ayam", "🍗", None),
("Ayam Goreng Mentega", "", 12000, "Ayam", "🍗", None),
("Ayam Goreng Tepung", "", 12000, "Ayam", "🍗", None),
("Ayam Goreng Rica", "", 12000, "Ayam", "🍗", None),
("Ayam Goreng Kering", "", 12000, "Ayam", "🍗", None),
("Ayam Lada Garam", "", 12000, "Ayam", "🍗", None),
("Ayam Lada Hitam", "", 12000, "Ayam", "🍗", None),
("Ayam Mayonaise", "", 12000, "Ayam", "🍗", None),
("Ayam Asam Manis", "", 12000, "Ayam", "🍗", None),

# ── UDANG ─────────────────────────────────────────────────
("Udang Mentega", "", 15000, "Udang", "🦐", None),
("Udang Goreng Tepung", "", 15000, "Udang", "🦐", None),
("Udang Rica", "", 15000, "Udang", "🦐", None),
("Udang Lada Garam", "", 15000, "Udang", "🦐", None),
("Udang Lada Hitam", "", 15000, "Udang", "🦐", None),
("Udang Mayonaise", "", 15000, "Udang", "🦐", None),
("Udang Asam Manis", "", 15000, "Udang", "🦐", None),

# ── CUMI ──────────────────────────────────────────────────
("Cumi Mentega", "", 15000, "Cumi", "🦑", None),
("Cumi Goreng Tepung", "", 15000, "Cumi", "🦑", None),
("Cumi Rica", "", 15000, "Cumi", "🦑", None),
("Cumi Lada Garam", "", 15000, "Cumi", "🦑", None),
("Cumi Lada Hitam", "", 15000, "Cumi", "🦑", None),
("Cumi Mayonaise", "", 15000, "Cumi", "🦑", None),
("Cumi Asam Manis", "", 15000, "Cumi", "🦑", None),

# ── SAPI / IKAN ───────────────────────────────────────────
("Sapi Lada Hitam", "", 15000, "Sapi / Ikan", "🥩", None),
("Nila Goreng Asam Manis", "", 15000, "Sapi / Ikan", "🐟", None),
("Nila Goreng Rica", "", 15000, "Sapi / Ikan", "🐟", None),

# ── TAHU ──────────────────────────────────────────────────
("Mun Tahu Ayam", "", 12000, "Tahu", "🥘", None),
("Sapo Tahu Ayam", "", 12000, "Tahu", "🥘", None),
("Sapo Tahu Seafood", "", 15000, "Tahu", "🥘", None),
("Sapo Tahu Babi", "", 14000, "Tahu", "🥘", None),

# ── SAYURAN ───────────────────────────────────────────────
("Kangkung Cah Bawang Putih", "", 8000, "Sayuran", "🥬", None),
("Kangkung Cah Terasi", "", 12000, "Sayuran", "🥬", None),
("Toge Cah Bawang Putih", "", 10000, "Sayuran", "🥬", None),
("Toge Cah Ikan Asin", "", 12000, "Sayuran", "🥬", None),
("Capcay Goreng / Capcay Kuah Ayam", "", 15000, "Sayuran", "🥬", None),
("Capcay Goreng / Capcay Kuah Seafood", "", 15000, "Sayuran", "🥬", None),
("Capcay Goreng / Capcay Kuah Babi", "", 15000, "Sayuran", "🥬", None),

# ── NASI ──────────────────────────────────────────────────
("Nasi Putih", "", 2000, "Nasi", "🍚", None),

# ── OBAT-OBATAN ───────────────────────────────────────────
("Tolak Angin",         "", 3_000,  "Obat-Obatan", "🌿", None),
("Cataflam",            "", 5_000,  "Obat-Obatan", "💊", None),
("Cetirizine",          "", 5_000,  "Obat-Obatan", "💊", None),
("Nin Jiom Pei Pa Koa", "", 30_000, "Obat-Obatan", "🍯", None),
("Panadol Biru",        "", 10_000, "Obat-Obatan", "💊", None),
("Panadol Merah",       "", 10_000, "Obat-Obatan", "💊", None),
("Degirol",             "", 15_000, "Obat-Obatan", "💊", None),
("Komix",               "", 2_000,  "Obat-Obatan", "💊", None),
("XonCe",               "", 2_000,  "Obat-Obatan", "💊", None),
("Vitacimin",           "", 2_000,  "Obat-Obatan", "💊", None),
("Freshcare Citrus",    "", 7_000,  "Obat-Obatan", "💊", None),
("Freshcare Hot",       "", 7_000,  "Obat-Obatan", "💊", None),
("Minyak Kayu Putih",   "", 7_000,  "Obat-Obatan", "🌿", None),
("Promag",              "", 12_000, "Obat-Obatan", "💊", None),
("Mylanta",             "", 12_000, "Obat-Obatan", "💊", None),
("Sanmol",              "", 5_000,  "Obat-Obatan", "💊", None),
("Bodrex",              "", 4_000,  "Obat-Obatan", "💊", None),
("Mixagrip Flu",        "", 4_000,  "Obat-Obatan", "💊", None),
("Ultraflu",            "", 4_000,  "Obat-Obatan", "💊", None),
("Paramex",             "", 4_000,  "Obat-Obatan", "💊", None),
("Decolgen",            "", 4_000,  "Obat-Obatan", "💊", None),
("Diapet",              "", 6_000,  "Obat-Obatan", "💊", None),

# ── ROKOK INDO ────────────────────────────────────────────
("Esse Double Change", "", 22_000, "Rokok Indo", "🚬", None),
("Esse Double Pop",    "", 22_000, "Rokok Indo", "🚬", None),
("Esse Change Juice",  "", 22_000, "Rokok Indo", "🚬", None),
("GG Filter",          "", 14_000, "Rokok Indo", "🚬", None),
("Surya 16",           "", 17_000, "Rokok Indo", "🚬", None),

# ── ROKOK LOKAL ───────────────────────────────────────────
("Marlboro Gold",    "", 8_000, "Rokok Lokal", "🚬", None),
("Marlboro Merah",   "", 8_000, "Rokok Lokal", "🚬", None),
("Esse Change Biru", "", 8_000, "Rokok Lokal", "🚬", None),
("Korek Api",        "", 2_000, "Rokok Lokal", "🔥", None),

# ── MINUMAN ───────────────────────────────────────────────
("Vital 500ml",        "", 2_000, "Minuman", "💧", None),
("Vital 1.5L",         "", 4_000, "Minuman", "💧", None),
("Pocari Sweat 500ml", "", 6_000, "Minuman", "🥤", None),
("Liang Teh Kaleng",   "", 4_000, "Minuman", "🥤", None),
("Coca Cola",          "", 4_000, "Minuman", "🥤", None),
("Fanta Orange",       "", 4_000, "Minuman", "🥤", None),
("Fanta Grape",        "", 4_000, "Minuman", "🥤", None),
("Sprite",             "", 4_000, "Minuman", "🥤", None),
("Bir Cambodia",       "", 6_000, "Minuman", "🍺", None),
("Angkor Beer Botol",  "", 10_000, "Minuman", "🍺", None),

# ── MENU WARTEG ───────────────────────────────────────────
("Babi Rica Rica",        "", 10_000, "Menu Warteg", "🍛", None),
("Babi Cabe Ijo",         "", 10_000, "Menu Warteg", "🍛", None),
("Babi Lada Hitam",       "", 10_000, "Menu Warteg", "🍛", None),
("Babi Casio",            "", 10_000, "Menu Warteg", "🍛", None),
("Samcan Sambal Ijo",     "", 10_000, "Menu Warteg", "🍛", None),
("Babi Semur",            "", 10_000, "Menu Warteg", "🍛", None),
("Telor Semur",           "", 3_000,  "Menu Warteg", "🍛", None),
("Tahu Semur",            "", 3_000,  "Menu Warteg", "🍛", None),
("Sapo Tahu Polos",       "", 4_000,  "Menu Warteg", "🍛", None),
("Cah Toge",              "", 4_000,  "Menu Warteg", "🍛", None),
("Buncis Babi",           "", 4_000,  "Menu Warteg", "🍛", None),
("Mun Tahu Babi",         "", 5_000,  "Menu Warteg", "🍛", None),
("Sayur Asin Bakut 3pcs", "", 15_000, "Menu Warteg", "🍛", None),
("Sayur Capcai Polos",    "", 4_000,  "Menu Warteg", "🍛", None),
("Babi Kecap",            "", 10_000, "Menu Warteg", "🍛", None),
("Sayur Asin Tahu",       "", 4_000,  "Menu Warteg", "🍛", None),
("Fuyunghai Babi",        "", 5_000,  "Menu Warteg", "🍛", None),
]


def inject():
    init_db()
    with get_conn() as conn:
        cur = conn.cursor()
        cols = [r[1] for r in cur.execute("PRAGMA table_info(menu_items)").fetchall()]
        if "image_url" not in cols:
            cur.execute("ALTER TABLE menu_items ADD COLUMN image_url TEXT")

        cur.execute("DELETE FROM menu_items")
        cur.executemany(
            "INSERT INTO menu_items (name, description, price, category, emoji, image_url) VALUES (?,?,?,?,?,?)",
            MENU,
        )
        conn.commit()
    print(f"Inject selesai: {len(MENU)} item menu.")


if __name__ == "__main__":
    inject()
