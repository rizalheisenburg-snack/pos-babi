"""Inject/replace menu Warteg Babi Kompong Dewa. Aman dijalanin ulang."""
from db import get_conn, init_db

# (name, description, price, category, emoji, image_url)
MENU = [
    # ── MENU BABI ─────────────────────────────────────────────────────────────
    ("Ricebowl Babi / Samcan Sambal Matah",   "", 12_000, "Babi & Samcan", "🐷", None),
    ("Ricebowl Babi / Samcan Sambal Ijo",     "", 12_000, "Babi & Samcan", "🐷", None),
    ("Ricebowl Babi / Samcan Sambal Bawang",  "", 12_000, "Babi & Samcan", "🐷", None),
    ("Ricebowl Babi / Samcan Sambal Tempong", "", 12_000, "Babi & Samcan", "🐷", None),
    ("Ricebowl Babi Rica",                    "", 12_000, "Babi & Samcan", "🐷", None),
    ("Ricebowl Babi Asam Manis",              "", 12_000, "Babi & Samcan", "🐷", None),
    ("Ricebowl Babi Lada Hitam",              "", 12_000, "Babi & Samcan", "🐷", None),
    ("Ricebowl Babi Lada Garam",              "", 12_000, "Babi & Samcan", "🐷", None),
    ("Ricebowl Samcan Kecap",                 "", 12_000, "Babi & Samcan", "🐷", None),

    # ── MENU CHINEESEFOOD ────────────────────────────────────────────────────
    ("Nasi Goreng Telor",               "", 10_000, "Chinese Food & Seafood", "🍳", None),
    ("Nasi Goreng Ayam",                "", 12_000, "Chinese Food & Seafood", "🍳", None),
    ("Nasi Goreng Ikan Asin",           "", 12_000, "Chinese Food & Seafood", "🍳", None),
    ("Nasi Goreng Ati Ampela",          "", 15_000, "Chinese Food & Seafood", "🍳", None),
    ("Nasi Goreng Seafood",             "", 15_000, "Chinese Food & Seafood", "🍳", None),
    ("Nasi Goreng Sapi",                "", 15_000, "Chinese Food & Seafood", "🍳", None),
    ("Nasi Goreng Babi",                "", 15_000, "Chinese Food & Seafood", "🍳", None),

    ("Kwetiau Goreng Telor",            "", 10_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Goreng Ayam",             "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Goreng Seafood",          "", 14_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Goreng Sapi",             "", 14_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Goreng Babi",             "", 14_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Siram Telor",             "", 10_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Siram Ayam",              "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Siram Seafood",           "", 14_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Siram Sapi",              "", 14_000, "Chinese Food & Seafood", "🍤", None),
    ("Kwetiau Siram Babi",              "", 14_000, "Chinese Food & Seafood", "🍤", None),

    ("Mie Goreng Telor",                "", 10_000, "Chinese Food & Seafood", "🍜", None),
    ("Mie Goreng Ayam",                 "", 12_000, "Chinese Food & Seafood", "🍜", None),
    ("Mie Goreng Seafood",              "", 14_000, "Chinese Food & Seafood", "🍜", None),
    ("Mie Goreng Sapi",                 "", 14_000, "Chinese Food & Seafood", "🍜", None),
    ("Mie Goreng Babi",                 "", 14_000, "Chinese Food & Seafood", "🍜", None),

    ("Bihun Goreng Telor",              "", 10_000, "Chinese Food & Seafood", "🍤", None),
    ("Bihun Goreng Ayam",               "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Bihun Goreng Seafood",            "", 14_000, "Chinese Food & Seafood", "🍤", None),
    ("Bihun Goreng Sapi",               "", 14_000, "Chinese Food & Seafood", "🍤", None),
    ("Bihun Goreng Babi",               "", 14_000, "Chinese Food & Seafood", "🍤", None),
    ("Bihun Siram Ayam",                "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Bihun Siram Seafood",             "", 14_000, "Chinese Food & Seafood", "🍤", None),

    ("Fuyunghai Ayam",                  "", 15_000, "Chinese Food & Seafood", "🍤", None),
    ("Fuyunghai Seafood",               "", 16_000, "Chinese Food & Seafood", "🍤", None),
    ("Fuyunghai Babi",                  "", 14_000, "Chinese Food & Seafood", "🍤", None),

    ("Sop Bakso Ikan",                  "", 12_000, "Chinese Food & Seafood", "🍲", None),
    ("Sop Seafood",                     "", 15_000, "Chinese Food & Seafood", "🍲", None),

    ("Ayam Salted Egg",                 "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Ayam Goreng Mentega",             "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Ayam Goreng Tepung",              "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Ayam Goreng Rica",                "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Ayam Goreng Kering",              "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Ayam Lada Garam",                 "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Ayam Lada Hitam",                 "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Ayam Mayonaise",                  "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Ayam Asam Manis",                 "", 12_000, "Chinese Food & Seafood", "🍤", None),

    ("Udang / Cumi Mentega",             "", 15_000, "Chinese Food & Seafood", "🦐", None),
    ("Udang / Cumi Goreng Tepung",       "", 15_000, "Chinese Food & Seafood", "🦐", None),
    ("Udang / Cumi Rica",                "", 15_000, "Chinese Food & Seafood", "🦐", None),
    ("Udang / Cumi Lada Garam",          "", 15_000, "Chinese Food & Seafood", "🦐", None),
    ("Udang / Cumi Lada Hitam",          "", 15_000, "Chinese Food & Seafood", "🦐", None),
    ("Udang / Cumi Mayonaise",           "", 15_000, "Chinese Food & Seafood", "🦐", None),
    ("Udang / Cumi Asam Manis",          "", 15_000, "Chinese Food & Seafood", "🦐", None),

    ("Sapi Lada Hitam",                 "", 15_000, "Chinese Food & Seafood", "🥩", None),
    ("Nila Goreng Asam Manis",          "", 15_000, "Chinese Food & Seafood", "🐟", None),
    ("Nila Goreng Rica",                "", 15_000, "Chinese Food & Seafood", "🐟", None),

    ("Mun Tahu Ayam",                   "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Sapo Tahu Ayam",                  "", 12_000, "Chinese Food & Seafood", "🍤", None),
    ("Sapo Tahu Seafood",               "", 15_000, "Chinese Food & Seafood", "🍤", None),
    ("Sapo Tahu Babi",                  "", 14_000, "Chinese Food & Seafood", "🍤", None),

    ("Kangkung Cah Bawang Putih",       "", 8_000,  "Chinese Food & Seafood", "🥦", None),
    ("Kangkung Cah Terasi",             "", 12_000, "Chinese Food & Seafood", "🥦", None),
    ("Toge Cah Bawang Putih",           "", 10_000, "Chinese Food & Seafood", "🥦", None),
    ("Toge Cah Ikan Asin",              "", 12_000, "Chinese Food & Seafood", "🥦", None),
    ("Capcay Goreng / Capcay Kuah Ayam",    "", 15_000, "Chinese Food & Seafood", "🥦", None),
    ("Capcay Goreng / Capcay Kuah Seafood", "", 15_000, "Chinese Food & Seafood", "🥦", None),
    ("Capcay Goreng / Capcay Kuah Babi",    "", 15_000, "Chinese Food & Seafood", "🥦", None),

    ("Nasi Putih",                      "", 2_000,  "Chinese Food & Seafood", "🍚", None),

    # ── OBAT - OBATAN ─────────────────────────────────────────────────────────
    ("Tolak Angin",                     "", 3_000,  "Obat-Obatan", "🌿", None),
    ("Cataflam",                        "", 5_000,  "Obat-Obatan", "💊", None),
    ("Cetirizine",                      "", 5_000,  "Obat-Obatan", "💊", None),
    ("Nin Jiom Pei Pa Koa",             "", 30_000, "Obat-Obatan", "🍯", None),
    ("Panadol Biru",                    "", 10_000, "Obat-Obatan", "💊", None),
    ("Panadol Merah",                   "", 10_000, "Obat-Obatan", "💊", None),
    ("Degirol",                         "", 15_000, "Obat-Obatan", "💊", None),
    ("Komix",                           "", 2_000,  "Obat-Obatan", "💊", None),
    ("XonCe",                           "", 2_000,  "Obat-Obatan", "💊", None),
    ("Vitacimin",                       "", 2_000,  "Obat-Obatan", "💊", None),
    ("Freshcare Citrus",                "", 7_000,  "Obat-Obatan", "💊", None),
    ("Freshcare Hot",                   "", 7_000,  "Obat-Obatan", "💊", None),
    ("Minyak Kayu Putih",               "", 7_000,  "Obat-Obatan", "🌿", None),
    ("Promag",                          "", 12_000, "Obat-Obatan", "💊", None),
    ("Mylanta",                         "", 12_000, "Obat-Obatan", "💊", None),
    ("Sanmol",                          "", 5_000,  "Obat-Obatan", "💊", None),
    ("Bodrex",                          "", 4_000,  "Obat-Obatan", "💊", None),
    ("Mixagrip Flu",                    "", 4_000,  "Obat-Obatan", "💊", None),
    ("Ultraflu",                        "", 4_000,  "Obat-Obatan", "💊", None),
    ("Paramex",                         "", 4_000,  "Obat-Obatan", "💊", None),
    ("Decolgen",                        "", 4_000,  "Obat-Obatan", "💊", None),
    ("Diapet",                          "", 6_000,  "Obat-Obatan", "💊", None),
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
