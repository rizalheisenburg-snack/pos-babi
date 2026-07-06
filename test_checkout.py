import sqlite3
from importlib import reload
from types import SimpleNamespace

import pytest

import config
import checkout_flow
import db
import server
import state_machine

from db import get_conn
from checkout_flow import checkout, confirm_partial
from state_machine import get_order

@pytest.fixture(autouse=True)
def temp_db(monkeypatch, tmp_path):
    db_path = tmp_path / "test.db"
    monkeypatch.setenv("DB_PATH", str(db_path))
    reload(config)
    reload(db)
    reload(checkout_flow)
    reload(state_machine)
    reload(server)

    with open("schema.sql") as f:
        sql = f.read()
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.executescript(sql)
    conn.commit()
    conn.close()
    yield

@pytest.fixture
def fake_user():
    return {"id": 111, "username": "testuser", "first_name": "Test", "last_name": "User"}

@pytest.fixture
def seeded_menu():
    with get_conn() as conn:
        conn.executemany(
            "INSERT INTO menu_items (name, description, price, category, emoji) VALUES (?,?,?,?,?)",
            [
                ("Item A", "Desc", 5000, "Cat1", "🧾"),
                ("Item B", "Desc", 15000, "Cat2", "🍛"),
            ],
        )
        conn.commit()
    return True

def test_checkout_cash_assigns_payment_method(fake_user, seeded_menu):
    result = checkout(
        user=fake_user,
        items=[{"item_id": 1, "qty": 1}],
        use_voucher=False,
        note="[KD] test",
        payment_method="CASH",
    )
    assert result["ok"]
    order = get_order(result["order_id"])
    assert order["payment_method"] == "CASH"
    assert order["total"] == 5000

def test_checkout_aba_assigns_payment_method(fake_user, seeded_menu):
    result = checkout(
        user=fake_user,
        items=[{"item_id": 2, "qty": 1}],
        use_voucher=False,
        note="[Transfer ABA] [KD] test",
        payment_method="ABA",
    )
    assert result["ok"]
    order = get_order(result["order_id"])
    assert order["payment_method"] == "ABA"
    assert order["note"].startswith("[Transfer ABA]")

@pytest.mark.parametrize("use_voucher, expected_total", [
    (False, 15000),
    (True, 5000),
])
def test_checkout_voucher_total(fake_user, seeded_menu, use_voucher, expected_total):
    result = checkout(
        user=fake_user,
        items=[{"item_id": 2, "qty": 1}],
        use_voucher=use_voucher,
        note="[KD] test",
        payment_method="CASH",
    )
    assert result["ok"]
    assert result["total"] == expected_total

def test_checkout_voucher_free_total_is_paid(fake_user, seeded_menu):
    result = checkout(
        user=fake_user,
        items=[{"item_id": 1, "qty": 2}],  # 2 x 5000 = 10000, pas voucher
        use_voucher=True,
        note="[KD] gratis voucher",
        payment_method="VOUCHER",
    )
    assert result["ok"]
    assert result["total"] == 0
    assert result["auto_paid"] is True
    order = get_order(result["order_id"])
    assert order["payment_method"] == "VOUCHER"
    assert order["payment_status"] == "PAID"

def test_checkout_voucher_rejected_when_total_not_zero(fake_user, seeded_menu):
    result = checkout(
        user=fake_user,
        items=[{"item_id": 2, "qty": 1}],  # 15000, voucher potong 10000, sisa 5000
        use_voucher=True,
        note="[KD] test",
        payment_method="VOUCHER",
    )
    assert not result["ok"]
    assert "VOUCHER" in result["error"]

def test_confirm_partial_succeeds_and_order_pending(fake_user, seeded_menu):
    result = checkout(
        user=fake_user,
        items=[{"item_id": 1, "qty": 1}],
        use_voucher=False,
        note="[KD] test",
        payment_method="CASH",
    )
    assert result["ok"]

    with get_conn() as conn:
        conn.execute("UPDATE orders SET status='PARTIAL_PENDING' WHERE id=?", (result["order_id"],))
        conn.commit()

    confirm = confirm_partial(result["order_id"], fake_user["id"])
    assert confirm["ok"]
    order = get_order(result["order_id"])
    assert order["status"] == "PENDING"

def test_auto_paid_order_no_mirror_needed(fake_user, seeded_menu):
    result = checkout(
        user=fake_user,
        items=[{"item_id": 1, "qty": 2}],
        use_voucher=True,
        note="[KD] gratis",
        payment_method="CASH",
    )
    assert result["ok"]
    assert result["total"] == 0
    assert result["auto_paid"] is True
    order = get_order(result["order_id"])
    assert order["payment_status"] == "PAID"


# ── Mirror order ke pelanggan (Task 2) ──────────────────────────────────────

class _FakeBot:
    """Bot palsu yang beneran baca isi file foto, biar ketauan kalau
    file-nya kepanggil sesudah closed (bug closed-file di _send_photo)."""
    def __init__(self):
        self.messages = []
        self.photos = []

    async def send_message(self, chat_id, text, parse_mode=None):
        self.messages.append(text)

    async def send_photo(self, chat_id, photo):
        self.photos.append(photo.read())


def _fake_request(bot):
    return SimpleNamespace(app={"bot": bot})


@pytest.fixture
def fake_qr_images(monkeypatch, tmp_path):
    aba_path = tmp_path / "aba.jpg"
    aba_path.write_bytes(b"ABA_QR_BYTES")
    voucher_path = tmp_path / "voucher.jpg"
    voucher_path.write_bytes(b"VOUCHER_QR_BYTES")
    monkeypatch.setattr(config, "ABA_QR_IMAGE_PATH", str(aba_path))
    monkeypatch.setattr(config, "VOUCHER_QR_IMAGE_PATH", str(voucher_path))


@pytest.mark.asyncio
async def test_mirror_aba_no_voucher_sends_aba_qr_only(fake_user, seeded_menu, fake_qr_images):
    result = checkout(
        user=fake_user, items=[{"item_id": 2, "qty": 1}],
        use_voucher=False, note="[Transfer ABA] [KD] test", payment_method="ABA",
    )
    assert result["ok"] and not result["auto_paid"]

    bot = _FakeBot()
    await server._send_order_mirror_to_user(_fake_request(bot), result["order_id"])

    assert len(bot.messages) == 1
    assert "bukti transfer" in bot.messages[0]
    assert bot.photos == [b"ABA_QR_BYTES"]


@pytest.mark.asyncio
async def test_mirror_aba_with_voucher_sends_both_qr(fake_user, seeded_menu, fake_qr_images):
    result = checkout(
        user=fake_user, items=[{"item_id": 2, "qty": 1}],
        use_voucher=True, note="[Transfer ABA] [KD] test", payment_method="ABA",
    )
    assert result["ok"] and result["total"] == 5000 and not result["auto_paid"]

    bot = _FakeBot()
    await server._send_order_mirror_to_user(_fake_request(bot), result["order_id"])

    assert len(bot.messages) == 1
    assert "bukti transfer" in bot.messages[0]
    assert "bukti scan voucher" in bot.messages[0]
    assert sorted(bot.photos) == sorted([b"ABA_QR_BYTES", b"VOUCHER_QR_BYTES"])


@pytest.mark.asyncio
async def test_mirror_cash_with_voucher_sends_voucher_qr_only(fake_user, seeded_menu, fake_qr_images):
    result = checkout(
        user=fake_user, items=[{"item_id": 2, "qty": 1}],
        use_voucher=True, note="[KD] test", payment_method="CASH",
    )
    assert result["ok"] and result["total"] == 5000 and not result["auto_paid"]

    bot = _FakeBot()
    await server._send_order_mirror_to_user(_fake_request(bot), result["order_id"])

    assert len(bot.messages) == 1
    assert "bukti transfer" not in bot.messages[0]
    assert "bukti scan voucher" in bot.messages[0]
    assert bot.photos == [b"VOUCHER_QR_BYTES"]


@pytest.mark.asyncio
async def test_mirror_full_cash_no_voucher_sends_no_photo(fake_user, seeded_menu, fake_qr_images):
    result = checkout(
        user=fake_user, items=[{"item_id": 1, "qty": 1}],
        use_voucher=False, note="[KD] test", payment_method="CASH",
    )
    assert result["ok"] and not result["auto_paid"]

    bot = _FakeBot()
    await server._send_order_mirror_to_user(_fake_request(bot), result["order_id"])

    assert len(bot.messages) == 1
    assert "bukti transfer" not in bot.messages[0]
    assert bot.photos == []


@pytest.mark.asyncio
async def test_mirror_auto_paid_sends_short_confirmation_only(fake_user, seeded_menu, fake_qr_images):
    result = checkout(
        user=fake_user, items=[{"item_id": 1, "qty": 2}],
        use_voucher=True, note="[KD] gratis", payment_method="CASH",
    )
    assert result["ok"] and result["total"] == 0 and result["auto_paid"] is True

    bot = _FakeBot()
    await server._send_order_mirror_to_user(_fake_request(bot), result["order_id"])

    assert len(bot.messages) == 1
    assert "Total 0" in bot.messages[0]
    assert bot.photos == []
