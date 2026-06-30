"""Inject/replace menu Warteg Babi Kompong Dewa. Aman dijalanin ulang."""
from db import get_conn, init_db

Q = "?w=400&q=80&auto=format&fit=crop"

# ── Image URL per jenis masakan ───────────────────────────────────────────────
_SWEET_SOUR     = f"https://images.unsplash.com/photo-1625477811235-78d02ef94efe{Q}"
_BRAISED_PORK   = f"https://images.unsplash.com/photo-1612156502174-bbbad9882af2{Q}"
_SPICY          = f"https://images.unsplash.com/photo-1606728035253-49e8a23146de{Q}"
_FRIED_BATTER   = f"https://images.unsplash.com/photo-1567620832903-9fc6debc209f{Q}"
_GRILLED        = f"https://images.unsplash.com/photo-1625477811233-044633d10dd1{Q}"
_SATAY          = f"https://images.unsplash.com/photo-1555939594-58d7cb561fbf{Q}"
_FRIED_RICE     = f"https://images.unsplash.com/photo-1603133872878-684f208fb84b{Q}"
_EGG_FRIED_RICE = f"https://images.unsplash.com/photo-1609570324378-ec0c4c9b6ba8{Q}"
_FLAT_NOODLE    = f"https://images.unsplash.com/photo-1612170153139-6f881ff067e0{Q}"
_FRIED_NOODLE   = f"https://images.unsplash.com/photo-1555939594-58d7cb561fbf{Q}"
_BIHUN          = f"https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7{Q}"
_EGG_FOO_YOUNG  = f"https://images.unsplash.com/photo-1546069901-ba9599a7e63c{Q}"
_TOFU           = f"https://images.unsplash.com/photo-1540189549336-e6e99c3679fe{Q}"
_BRAISED_TOFU   = f"https://images.unsplash.com/photo-1546069901-ba9599a7e63c{Q}"
_POTATO         = f"https://images.unsplash.com/photo-1597103442097-8b74394b95c6{Q}"
_VEG            = f"https://images.unsplash.com/photo-1512621776951-a57141f2eefd{Q}"
_STIR_VEG       = f"https://images.unsplash.com/photo-1609334374789-a14917ffc3ac{Q}"
_SQUID          = f"https://images.unsplash.com/photo-1579584425555-c3ce17fd4351{Q}"
_FISH           = f"https://images.unsplash.com/photo-1580959375944-abd7e991f971{Q}"
_SHRIMP         = f"https://images.unsplash.com/photo-1580959375944-abd7e991f971{Q}"
_CHICKEN_MAYO   = f"https://images.unsplash.com/photo-1567620832903-9fc6debc209f{Q}"
_CLAYPOT        = f"https://images.unsplash.com/photo-1540189549336-e6e99c3679fe{Q}"
_RICE           = f"https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6{Q}"
_MEDICINE       = f"https://images.unsplash.com/photo-1587854692152-cbe660dbde36{Q}"

# (name, description, price, category, emoji, image_url)
MENU = [
    # ── BABI & SAMCAN ──────────────────────────────────────────────────────────
    ("Babi Asam Manis",                 "", 8_000,  "Babi & Samcan", "🐷", _SWEET_SOUR),
    ("Babi Cah Jahe / Kecap Jahe",      "", 8_000,  "Babi & Samcan", "🐷", _BRAISED_PORK),
    ("Babi Cabe Hijau",                 "", 8_000,  "Babi & Samcan", "🐷", _SPICY),
    ("Babi Goreng Tepung Asam Manis",   "", 8_000,  "Babi & Samcan", "🐷", _FRIED_BATTER),
    ("Babi Goreng Tepung Sambal Matah", "", 8_000,  "Babi & Samcan", "🐷", _FRIED_BATTER),
    ("Babi Lada Garam",                 "", 8_000,  "Babi & Samcan", "🐷", _SPICY),
    ("Babi Lada Hitam",                 "", 8_000,  "Babi & Samcan", "🐷", _SPICY),
    ("Babi Kecap",                      "", 8_000,  "Babi & Samcan", "🐷", _BRAISED_PORK),
    ("Babi Rica-Rica",                  "", 8_000,  "Babi & Samcan", "🐷", _SPICY),
    ("Babi Semur",                      "", 8_000,  "Babi & Samcan", "🐷", _BRAISED_PORK),
    ("Bihun Goreng Babi",               "", 12_000, "Babi & Samcan", "🐷", _BIHUN),
    ("Fu Yung Hai Babi",                "", 4_000,  "Babi & Samcan", "🐷", _EGG_FOO_YOUNG),
    ("Kentang Babi",                    "", 5_000,  "Babi & Samcan", "🐷", _POTATO),
    ("Kentang Kecap",                   "", 4_000,  "Babi & Samcan", "🐷", _POTATO),
    ("Kwetiau Babi",                    "", 6_000,  "Babi & Samcan", "🐷", _FLAT_NOODLE),
    ("Mun Tahu Babi",                   "", 4_000,  "Babi & Samcan", "🐷", _BRAISED_TOFU),
    ("Nasi Goreng Babi",                "", 12_000, "Babi & Samcan", "🐷", _FRIED_RICE),
    ("Samcan Asam Manis",               "", 8_000,  "Babi & Samcan", "🐷", _SWEET_SOUR),
    ("Samcan Bakar",                    "", 8_000,  "Babi & Samcan", "🐷", _GRILLED),
    ("Samcan Balado",                   "", 8_000,  "Babi & Samcan", "🐷", _SPICY),
    ("Samcan Cabe Ijo",                 "", 8_000,  "Babi & Samcan", "🐷", _SPICY),
    ("Samcan Crispy",                   "", 8_000,  "Babi & Samcan", "🐷", _FRIED_BATTER),
    ("Samcan Kecap",                    "", 8_000,  "Babi & Samcan", "🐷", _BRAISED_PORK),
    ("Samcan Sambal Matah",             "", 8_000,  "Babi & Samcan", "🐷", _SPICY),
    ("Samcan Semur",                    "", 8_000,  "Babi & Samcan", "🐷", _BRAISED_PORK),
    ("Sate Babi Manis",                 "", 4_000,  "Babi & Samcan", "🐷", _SATAY),
    ("Sayur Asin Babi",                 "", 8_000,  "Babi & Samcan", "🐷", _VEG),
    ("Sayur Asin Bakut",                "", 8_000,  "Babi & Samcan", "🐷", _VEG),

    # ── CHINESE FOOD & SEAFOOD/AYAM ────────────────────────────────────────────
    ("Ayam Asam Manis",                 "", 12_000, "Chinese Food & Seafood", "🍤", _SWEET_SOUR),
    ("Ayam Mayonaise",                  "", 12_000, "Chinese Food & Seafood", "🍤", _CHICKEN_MAYO),
    ("Udang Mayo",                      "", 15_000, "Chinese Food & Seafood", "🦐", _SHRIMP),
    ("Bihun Goreng Ayam",               "", 12_000, "Chinese Food & Seafood", "🍤", _BIHUN),
    ("Bihun Goreng Seafood",            "", 14_000, "Chinese Food & Seafood", "🍤", _BIHUN),
    ("Bihun Goreng Telur",              "", 10_000, "Chinese Food & Seafood", "🍤", _BIHUN),
    ("Bihun Siram Ayam",                "", 12_000, "Chinese Food & Seafood", "🍤", _BIHUN),
    ("Bihun Siram Seafood",             "", 14_000, "Chinese Food & Seafood", "🍤", _BIHUN),
    ("Bihun Siram Telur",               "", 10_000, "Chinese Food & Seafood", "🍤", _BIHUN),
    ("Cumi Goreng Tepung",              "", 8_000,  "Chinese Food & Seafood", "🦑", _SQUID),
    ("Cumi Goreng Tepung Asam Manis",   "", 8_000,  "Chinese Food & Seafood", "🦑", _SQUID),
    ("Cumi Goreng Tepung Sambal Matah", "", 8_000,  "Chinese Food & Seafood", "🦑", _SQUID),
    ("Fish Cake Lada Hitam",            "", 5_000,  "Chinese Food & Seafood", "🐟", _FISH),
    ("Fuyunghai Ayam",                  "", 15_000, "Chinese Food & Seafood", "🍤", _EGG_FOO_YOUNG),
    ("Kwetiau Goreng Ayam",             "", 12_000, "Chinese Food & Seafood", "🍤", _FLAT_NOODLE),
    ("Kwetiau Goreng Seafood",          "", 14_000, "Chinese Food & Seafood", "🍤", _FLAT_NOODLE),
    ("Kwetiau Goreng Telur",            "", 10_000, "Chinese Food & Seafood", "🍤", _FLAT_NOODLE),
    ("Kwetiau Siram Ayam",              "", 12_000, "Chinese Food & Seafood", "🍤", _FLAT_NOODLE),
    ("Kwetiau Siram Seafood",           "", 14_000, "Chinese Food & Seafood", "🍤", _FLAT_NOODLE),
    ("Kwetiau Siram Telur",             "", 10_000, "Chinese Food & Seafood", "🍤", _FLAT_NOODLE),
    ("Mie Ayam Babi",                   "", 15_000, "Chinese Food & Seafood", "🍜", _FRIED_NOODLE),
    ("Mie Goreng Ayam",                 "", 12_000, "Chinese Food & Seafood", "🍜", _FRIED_NOODLE),
    ("Mie Goreng Telor",                "", 10_000, "Chinese Food & Seafood", "🍜", _FRIED_NOODLE),
    ("Mun Tahu Ayam",                   "", 12_000, "Chinese Food & Seafood", "🍤", _BRAISED_TOFU),
    ("Nasi Goreng Ati Ampela",          "", 12_000, "Chinese Food & Seafood", "🍳", _FRIED_RICE),
    ("Nasi Goreng Ayam",                "", 12_000, "Chinese Food & Seafood", "🍳", _FRIED_RICE),
    ("Nasi Goreng Ikan Asin",           "", 12_000, "Chinese Food & Seafood", "🍳", _FRIED_RICE),
    ("Nasi Goreng Telur",               "", 10_000, "Chinese Food & Seafood", "🍳", _EGG_FRIED_RICE),
    ("Sapo Tahu Ayam",                  "", 12_000, "Chinese Food & Seafood", "🍤", _CLAYPOT),
    ("Sapo Tahu Babi (Chinese Style)",  "", 15_000, "Chinese Food & Seafood", "🍤", _CLAYPOT),

    # ── SAYUR & PELENGKAP ──────────────────────────────────────────────────────
    ("Capcay Goreng Ayam",              "", 15_000, "Sayur & Pelengkap", "🥦", _STIR_VEG),
    ("Capcay Kuah Ayam",                "", 15_000, "Sayur & Pelengkap", "🥦", _STIR_VEG),
    ("Capcay Polos",                    "", 3_000,  "Sayur & Pelengkap", "🥦", _STIR_VEG),
    ("Capcay Babi",                     "", 4_000,  "Sayur & Pelengkap", "🥦", _STIR_VEG),
    ("Cah Kangkung",                    "", 10_000, "Sayur & Pelengkap", "🥦", _STIR_VEG),
    ("Kangkung Cah Terasi",             "", 12_000, "Sayur & Pelengkap", "🥦", _STIR_VEG),
    ("Sapo Tahu Polos",                 "", 3_000,  "Sayur & Pelengkap", "🥦", _TOFU),
    ("Sapo Tahu Babi",                  "", 4_000,  "Sayur & Pelengkap", "🥦", _TOFU),
    ("Sayur Asin Cah Tahu",             "", 3_000,  "Sayur & Pelengkap", "🥦", _VEG),
    ("Sayur Ati Tahu",                  "", 3_000,  "Sayur & Pelengkap", "🥦", _TOFU),
    ("Semur Tahu",                      "", 2_000,  "Sayur & Pelengkap", "🥦", _BRAISED_TOFU),
    ("Semur Telor",                     "", 3_000,  "Sayur & Pelengkap", "🥦", _BRAISED_TOFU),
    ("Toge Tumis Tahu",                 "", 3_000,  "Sayur & Pelengkap", "🥦", _STIR_VEG),
    ("Toge Cah Bawang Putih",           "", 10_000, "Sayur & Pelengkap", "🥦", _STIR_VEG),
    ("Toge Cah Ikan Asin",              "", 12_000, "Sayur & Pelengkap", "🥦", _STIR_VEG),
    ("Fu Yung Hai",                     "", 5_000,  "Sayur & Pelengkap", "🥚", _EGG_FOO_YOUNG),
    ("Nasi Putih",                      "", 2_000,  "Sayur & Pelengkap", "🍚", _RICE),

    # ── OBAT-OBATAN ────────────────────────────────────────────────────────────
    ("Bodrex",                          "", 4_000,  "Obat-Obatan", "💊", _MEDICINE),
    ("Cataflam",                        "", 5_000,  "Obat-Obatan", "💊", _MEDICINE),
    ("Cetirizine",                      "", 5_000,  "Obat-Obatan", "💊", _MEDICINE),
    ("Decolgen",                        "", 4_000,  "Obat-Obatan", "💊", _MEDICINE),
    ("Degirol",                         "", 15_000, "Obat-Obatan", "💊", _MEDICINE),
    ("Diapet",                          "", 6_000,  "Obat-Obatan", "💊", _MEDICINE),
    ("Freshcare Citrus / Hot",          "", 7_000,  "Obat-Obatan", "💊", _MEDICINE),
    ("Komix",                           "", 2_000,  "Obat-Obatan", "💊", _MEDICINE),
    ("Minyak Kayu Putih",               "", 7_000,  "Obat-Obatan", "🌿", _MEDICINE),
    ("Mixagrip Flu",                    "", 4_000,  "Obat-Obatan", "💊", _MEDICINE),
    ("Mylanta",                         "", 12_000, "Obat-Obatan", "💊", _MEDICINE),
    ("Nin Jiom Pei Pa Koa",             "", 30_000, "Obat-Obatan", "🍯", _MEDICINE),
    ("Panadol Biru",                    "", 10_000, "Obat-Obatan", "💊", _MEDICINE),
    ("Panadol Merah",                   "", 10_000, "Obat-Obatan", "💊", _MEDICINE),
    ("Paramex",                         "", 4_000,  "Obat-Obatan", "💊", _MEDICINE),
    ("Promag",                          "", 12_000, "Obat-Obatan", "💊", _MEDICINE),
    ("Sanmol",                          "", 5_000,  "Obat-Obatan", "💊", _MEDICINE),
    ("Tolak Angin",                     "", 3_000,  "Obat-Obatan", "🌿", _MEDICINE),
    ("Ultraflu",                        "", 4_000,  "Obat-Obatan", "💊", _MEDICINE),
    ("Vitacimin",                       "", 2_000,  "Obat-Obatan", "💊", _MEDICINE),
    ("XonCe",                           "", 2_000,  "Obat-Obatan", "💊", _MEDICINE),
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
