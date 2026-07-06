"""HTTP server — aiohttp. Melayani API + static webapp."""
from __future__ import annotations
import json
import logging
import pathlib

log = logging.getLogger(__name__)

from aiohttp import web

from checkout_flow import checkout, confirm_partial, verify_init_data
from config import OWNER_ID
from db import get_conn
from state_machine import (
    get_order,
    get_user_orders,
    mark_paid,
    transition,
)

WEBAPP_DIR = pathlib.Path(__file__).parent / "webapp"
routes = web.RouteTableDef()


def _json(data, status=200):
    return web.Response(
        text=json.dumps(data, ensure_ascii=False),
        content_type="application/json",
        status=status,
    )


def _auth(request: web.Request) -> dict | None:
    return verify_init_data(request.headers.get("X-Init-Data", ""))


# ── Menu ──────────────────────────────────────────────────────────────────────

@routes.get("/api/menu")
async def api_menu(request):
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT * FROM menu_items WHERE available=1 ORDER BY category, name"
        ).fetchall()
    by_cat: dict[str, list] = {}
    for r in rows:
        d = dict(r)
        by_cat.setdefault(d["category"], []).append(d)
    return _json({"categories": by_cat})


# ── Checkout ──────────────────────────────────────────────────────────────────

@routes.post("/api/checkout")
async def api_checkout(request):
    user = _auth(request)
    if not user:
        return _json({"ok": False, "error": "Unauthorized"}, 401)
    try:
        body = await request.json()
        note = body.get("note", "")
        result = checkout(
            user=user,
            items=body.get("items", []),
            use_voucher=bool(body.get("use_voucher", False)),
            note=note,
            payment_method=body.get("payment_method", "CASH"),
        )
        # Kirim notif ke owner kalau order masuk (ok atau PARTIAL)
        if result.get("ok") or result.get("error") == "PARTIAL":
            await _notify_owner_new_order(request, result.get("order_id"))
        # Kirim mirror ke pelanggan untuk semua order sukses yang bukan auto-paid
        if result.get("ok") and not result.get("auto_paid"):
            await _send_order_mirror_to_user(request, result.get("order_id"))
        return _json(result, 200 if result["ok"] else 400)
    except Exception as e:
        log.exception("checkout error")
        return _json({"ok": False, "error": f"Server error: {e}"}, 500)


async def _notify_owner_new_order(request: web.Request, order_id: int | None):
    if not order_id:
        return
    bot = request.app["bot"]
    if not bot:
        return
    try:
        from owner_console import _order_keyboard, _order_text
        from state_machine import get_order, set_admin_msg_id
        o = get_order(order_id)
        if not o:
            return
        msg = await bot.send_message(
            chat_id=OWNER_ID,
            text=f"🔔 *Order baru masuk!*\n\n{_order_text(o)}",
            parse_mode="Markdown",
            reply_markup=_order_keyboard(o["id"], o["status"], o["payment_status"]),
        )
        set_admin_msg_id(order_id, msg.message_id)
    except Exception:
        log.exception("gagal kirim notif owner")


async def _send_order_mirror_to_user(request: web.Request, order_id: int | None):
    if not order_id:
        return
    bot = request.app["bot"]
    if not bot:
        return
    try:
        from owner_console import _order_text
        from state_machine import get_order
        from config import ABA_QR_IMAGE_PATH, VOUCHER_QR_IMAGE_PATH

        o = get_order(order_id)
        if not o:
            return

        if o["total"] == 0:
            await bot.send_message(
                chat_id=o["user_id"],
                text=f"✅ Order #{o['id']} berhasil. Total 0៛, pesanan Anda telah diterima.",
                parse_mode="Markdown",
            )
            return

        lines = [
            _order_text(o, for_admin=False),
        ]
        proof_needed = []
        if o.get("payment_method") == "ABA":
            proof_needed.append("bukti transfer ABA")
        if o.get("voucher_used"):
            proof_needed.append("bukti scan voucher")
        if proof_needed:
            lines.append(f"📸 Reply pesan ini dengan screenshot {' & '.join(proof_needed)}.")
        text = "\n\n".join(lines)

        await bot.send_message(
            chat_id=o["user_id"],
            text=text,
            parse_mode="Markdown",
        )

        async def _send_photo(path):
            if not path:
                return
            try:
                with open(path, "rb") as f:
                    await bot.send_photo(chat_id=o["user_id"], photo=f)
            except FileNotFoundError:
                log.warning("QR image not found: %s", path)
            except Exception:
                log.exception("gagal kirim foto ke user")

        if o.get("payment_method") == "ABA":
            await _send_photo(ABA_QR_IMAGE_PATH)
        if o.get("voucher_used"):
            await _send_photo(VOUCHER_QR_IMAGE_PATH)
    except Exception:
        log.exception("gagal kirim mirror order ke user")


@routes.post("/api/checkout/confirm-partial")
async def api_confirm_partial(request):
    user = _auth(request)
    if not user:
        return _json({"ok": False, "error": "Unauthorized"}, 401)
    body = await request.json()
    result = confirm_partial(int(body.get("order_id", 0)), user["id"])
    if result.get("ok"):
        await _send_order_mirror_to_user(request, result.get("order_id"))
    return _json(result, 200 if result["ok"] else 400)


# ── Orders ────────────────────────────────────────────────────────────────────

@routes.get("/api/orders")
async def api_orders(request):
    user = _auth(request)
    if not user:
        return _json({"ok": False, "error": "Unauthorized"}, 401)
    return _json({"ok": True, "orders": get_user_orders(user["id"])})


@routes.get("/api/orders/{order_id}")
async def api_order_detail(request):
    user = _auth(request)
    if not user:
        return _json({"ok": False, "error": "Unauthorized"}, 401)
    oid = int(request.match_info["order_id"])
    o = get_order(oid)
    if not o:
        return _json({"ok": False, "error": "Tidak ditemukan"}, 404)
    if o["user_id"] != user["id"] and user["id"] != OWNER_ID:
        return _json({"ok": False, "error": "Forbidden"}, 403)
    return _json({"ok": True, "order": o})


@routes.post("/api/orders/{order_id}/cancel")
async def api_cancel_order(request):
    user = _auth(request)
    if not user:
        return _json({"ok": False, "error": "Unauthorized"}, 401)
    oid = int(request.match_info["order_id"])
    result = transition(oid, "CANCELLED", actor="customer")
    return _json(result, 200 if result["ok"] else 400)


# ── Owner ─────────────────────────────────────────────────────────────────────

@routes.post("/api/owner/orders/{order_id}/status")
async def api_owner_status(request):
    user = _auth(request)
    if not user or user["id"] != OWNER_ID:
        return _json({"ok": False, "error": "Forbidden"}, 403)
    oid = int(request.match_info["order_id"])
    body = await request.json()
    result = transition(oid, body.get("status", ""), actor="owner")
    return _json(result, 200 if result["ok"] else 400)


@routes.post("/api/owner/orders/{order_id}/pay")
async def api_owner_pay(request):
    user = _auth(request)
    if not user or user["id"] != OWNER_ID:
        return _json({"ok": False, "error": "Forbidden"}, 403)
    oid = int(request.match_info["order_id"])
    body = await request.json()
    result = mark_paid(oid, body.get("currency", "RIEL"))
    return _json(result, 200 if result["ok"] else 400)


# ── Static ────────────────────────────────────────────────────────────────────

@routes.get("/{tail:.*}")
async def static_files(request):
    tail = request.match_info["tail"] or "index.html"
    path = WEBAPP_DIR / tail
    if not path.exists() or not path.is_file():
        path = WEBAPP_DIR / "index.html"
    # JS/CSS/img di-cache 1 jam, HTML tidak (supaya update langsung keliatan)
    is_html = path.suffix == ".html"
    headers = {} if is_html else {"Cache-Control": "public, max-age=3600"}
    return web.FileResponse(path, headers=headers)


def build_app(bot=None) -> web.Application:
    app = web.Application()
    app["bot"] = bot
    app.add_routes(routes)
    return app
