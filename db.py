import sqlite3
from config import DB_PATH


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db() -> None:
    with open("schema.sql") as f:
        sql = f.read()
    with get_conn() as conn:
        conn.executescript(sql)
        cols = [r[1] for r in conn.execute("PRAGMA table_info(orders)").fetchall()]
        if "admin_msg_id" not in cols:
            conn.execute("ALTER TABLE orders ADD COLUMN admin_msg_id INTEGER")
        if "payment_method" not in cols:
            conn.execute("ALTER TABLE orders ADD COLUMN payment_method TEXT")
        conn.execute(
            "UPDATE orders SET payment_method='ABA' WHERE note LIKE '[Transfer ABA]%'"
        )
        conn.execute(
            "UPDATE orders SET payment_method='CASH' WHERE payment_method IS NULL OR payment_method = ''"
        )
        conn.commit()
