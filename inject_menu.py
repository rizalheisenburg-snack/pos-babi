"""Inject/replace menu Warteg Babi Kompong Dewa. Aman dijalanin ulang."""
from db import get_conn, init_db

# (name, description, price, category, emoji, image_url)
MENU = [
    # ── BABI & SAMCAN ──────────────────────────────────────────────────────────
    ("Babi Asam Manis",                 "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Babi Cah Jahe / Kecap Jahe",      "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Babi Cabe Hijau",                 "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Babi Goreng Tepung Asam Manis",   "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Babi Goreng Tepung Sambal Matah", "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Babi Lada Garam",                 "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Babi Lada Hitam",                 "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Babi Kecap",                      "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Babi Rica-Rica",                  "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Babi Semur",                      "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Bihun Goreng Babi",               "", 12_000, "Babi & Samcan", "🐷", None),
    ("Fu Yung Hai Babi",                "", 4_000,  "Babi & Samcan", "🐷", None),
    ("Kentang Babi",                    "", 5_000,  "Babi & Samcan", "🐷", None),
    ("Kentang Kecap",                   "", 4_000,  "Babi & Samcan", "🐷", None),
    ("Kwetiau Babi",                    "", 6_000,  "Babi & Samcan", "🐷", None),
    ("Mun Tahu Babi",                   "", 4_000,  "Babi & Samcan", "🐷", None),
    ("Nasi Goreng Babi",                "", 12_000, "Babi & Samcan", "🐷", None),
    ("Samcan Asam Manis",               "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Samcan Bakar",                    "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Samcan Balado",                   "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Samcan Cabe Ijo",                 "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Samcan Crispy",                   "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Samcan Kecap",                    "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Samcan Sambal Matah",             "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Samcan Semur",                    "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Sate Babi Manis",                 "", 4_000,  "Babi & Samcan", "🐷", None),
    ("Sayur Asin Babi",                 "", 8_000,  "Babi & Samcan", "🐷", None),
    ("Sayur Asin Bakut",                "", 8_000,  "Babi & Samcan", "🐷", None),

    # ── CHINESE FOOD & SEAFOOD/AYAM ────────────────────────────────────────────
    ("Ayam Asam Manis",                 "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Ayam Mayonaise",                  "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Udang Mayo",                      "", 15_000, "Chinese Food & Seafood", "🦐", None),
    ("Bihun Goreng Ayam",               "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Bihun Goreng Seafood",            "", 14_000, "Chinese Food & Seafood", "🍤", None),
    ("Bihun Goreng Telur",              "", 10_000, "Chinese Food & Seafood", "🍤", None),
    ("Bihun Siram Ayam",                "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Bihun Siram Seafood",             "", 14_000, "Chinese Food & Seafood", "🍤", None),
    ("Bihun Siram Telur",               "", 10_000, "Chinese Food & Seafood", "🍤", None),
    ("Cumi Goreng Tepung",              "", 8_000,  "Chinese Food & Seafood", "🦑", None),
    ("Cumi Goreng Tepung Asam Manis",   "", 8_000,  "Chinese Food & Seafood", "🦑", None),
    ("Cumi Goreng Tepung Sambal Matah", "", 8_000,  "Chinese Food & Seafood", "🦑", None),
    ("Fish Cake Lada Hitam",            "", 5_000,  "Chinese Food & Seafood", "🐟", None),
    ("Fuyunghai Ayam",                  "", 15_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Goreng Ayam",             "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Goreng Seafood",          "", 14_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Goreng Telur",            "", 10_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Siram Ayam",              "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Siram Seafood",           "", 14_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Siram Telur",             "", 10_000, "Chinese Food & Seafood", "🍤", None),
    ("Mie Ayam Babi",                   "", 15_000, "Chinese Food & Seafood", "🍜", None),
    ("Mie Goreng Ayam",                 "", 12_000, "Chinese Food & Seafood", "🍜", None),
    ("Mie Goreng Telor",                "", 10_000, "Chinese Food & Seafood", "🍜", None),
    ("Mun Tahu Ayam",                   "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Nasi Goreng Ati Ampela",          "", 12_000, "Chinese Food & Seafood", "🍳", None),
    ("Nasi Goreng Ayam",                "", 12_000, "Chinese Food & Seafood", "🍳", None),
    ("Nasi Goreng Ikan Asin",           "", 12_000, "Chinese Food & Seafood", "🍳", None),
    ("Nasi Goreng Telur",               "", 10_000, "Chinese Food & Seafood", "🍳", None),
    ("Sapo Tahu Ayam",                  "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Sapo Tahu Babi (Chinese Style)",  "", 15_000, "Chinese Food & Seafood", "🍤", None),

    # ── SAYUR & PELENGKAP ──────────────────────────────────────────────────────
    ("Capcay Goreng Ayam",              "", 15_000, "Sayur & Pelengkap", "🥦", None),
    ("Capcay Kuah Ayam",                "", 15_000, "Sayur & Pelengkap", "🥦", None),
    ("Capcay Polos",                    "", 3_000,  "Sayur & Pelengkap", "🥦", None),
    ("Capcay Babi",                     "", 4_000,  "Sayur & Pelengkap", "🥦", None),
    ("Cah Kangkung",                    "", 10_000, "Sayur & Pelengkap", "🥦", None),
    ("Kangkung Cah Terasi",             "", 12_000, "Sayur & Pelengkap", "🥦", None),
    ("Sapo Tahu Polos",                 "", 3_000,  "Sayur & Pelengkap", "🥦", None),
    ("Sapo Tahu Babi",                  "", 4_000,  "Sayur & Pelengkap", "🥦", None),
    ("Sayur Asin Cah Tahu",             "", 3_000,  "Sayur & Pelengkap", "🥦", None),
    ("Sayur Ati Tahu",                  "", 3_000,  "Sayur & Pelengkap", "🥦", None),
    ("Semur Tahu",                      "", 2_000,  "Sayur & Pelengkap", "🥦", None),
    ("Semur Telor",                     "", 3_000,  "Sayur & Pelengkap", "🥦", None),
    ("Toge Tumis Tahu",                 "", 3_000,  "Sayur & Pelengkap", "🥦", None),
    ("Toge Cah Bawang Putih",           "", 10_000, "Sayur & Pelengkap", "🥦", None),
    ("Toge Cah Ikan Asin",              "", 12_000, "Sayur & Pelengkap", "🥦", None),
    ("Fu Yung Hai",                     "", 5_000,  "Sayur & Pelengkap", "🥚", None),
    ("Nasi Putih",                      "", 2_000,  "Sayur & Pelengkap", "🍚", None),

    # ── OBAT-OBATAN ────────────────────────────────────────────────────────────
    ("Bodrex",                          "", 4_000,  "Obat-Obatan", "💊", None),
    ("Cataflam",                        "", 5_000,  "Obat-Obatan", "💊", None),
    ("Cetirizine",                      "", 5_000,  "Obat-Obatan", "💊", None),
    ("Decolgen",                        "", 4_000,  "Obat-Obatan", "💊", None),
    ("Degirol",                         "", 15_000, "Obat-Obatan", "💊", None),
    ("Diapet",                          "", 6_000,  "Obat-Obatan", "💊", None),
    ("Freshcare Citrus / Hot",          "", 7_000,  "Obat-Obatan", "💊", None),
    ("Komix",                           "", 2_000,  "Obat-Obatan", "💊", None),
    ("Minyak Kayu Putih",               "", 7_000,  "Obat-Obatan", "🌿", None),
    ("Mixagrip Flu",                    "", 4_000,  "Obat-Obatan", "💊", None),
    ("Mylanta",                         "", 12_000, "Obat-Obatan", "💊", None),
    ("Nin Jiom Pei Pa Koa",             "", 30_000, "Obat-Obatan", "🍯", None),
    ("Panadol Biru",                    "", 10_000, "Obat-Obatan", "💊", None),
    ("Panadol Merah",                   "", 10_000, "Obat-Obatan", "💊", None),
    ("Paramex",                         "", 4_000,  "Obat-Obatan", "💊", None),
    ("Promag",                          "", 12_000, "Obat-Obatan", "💊", None),
    ("Sanmol",                          "", 5_000,  "Obat-Obatan", "💊", None),
    ("Tolak Angin",                     "", 3_000,  "Obat-Obatan", "🌿", None),
    ("Ultraflu",                        "", 4_000,  "Obat-Obatan", "💊", None),
    ("Vitacimin",                       "", 2_000,  "Obat-Obatan", "💊", None),
    ("XonCe",                           "", 2_000,  "Obat-Obatan", "💊", None),
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
