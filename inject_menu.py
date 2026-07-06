"""Inject/replace menu Warteg Babi Kompong Dewa. Aman dijalanin ulang."""
from db import get_conn, init_db

# (name, description, price, category, emoji, image_url)
MENU = [
# ── MENU BABI ─────────────────────────────────────────────
("Ricebowl Babi / Samcan Sambal Matah", "", 12000, "Babi & Samcan", "🐷", None),
("Ricebowl Babi / Samcan Sambal Ijo", "", 12000, "Babi & Samcan", "🐷", None),
...
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

# ── UDANG / CUMI ──────────────────────────────────────────
("Udang / Cumi Mentega", "", 15000, "Udang / Cumi", "🦐", None),
("Udang / Cumi Goreng Tepung", "", 15000, "Udang / Cumi", "🦐", None),
("Udang / Cumi Rica", "", 15000, "Udang / Cumi", "🦐", None),
("Udang / Cumi Lada Garam", "", 15000, "Udang / Cumi", "🦐", None),
("Udang / Cumi Lada Hitam", "", 15000, "Udang / Cumi", "🦐", None),
("Udang / Cumi Mayonaise", "", 15000, "Udang / Cumi", "🦐", None),
("Udang / Cumi Asam Manis", "", 15000, "Udang / Cumi", "🦐", None),

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
# (tidak berubah)
("Tolak Angin", "", 3000, "Obat-Obatan", "🌿", None),
...
("Diapet", "", 6000, "Obat-Obatan", "💊", None),
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
