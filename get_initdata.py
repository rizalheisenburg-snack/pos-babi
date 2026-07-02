import hashlib
import hmac
import json
import time
import urllib.parse

def generate_init_data(bot_token: str, user_id: int, first_name: str = "George", username: str = "george_test"):
    """
    Generate a valid Telegram WebApp init-data string for testing purposes.
    Requires the bot token (owner-only secret) to sign the payload correctly.
    """
    user_obj = {
        "id": user_id,
        "first_name": first_name,
        "username": username,
        "language_code": "en",
        "allows_write_to_pm": True
    }

    auth_date = int(time.time())

    data = {
        "query_id": "AAHdF6IQAAAAAN0XohDhrOrc",  # dummy, format-valid
        "user": json.dumps(user_obj, separators=(",", ":")),
        "auth_date": str(auth_date),
    }

    # Build data_check_string: sorted key=value joined by \n
    data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(data.items()))

    # secret_key = HMAC_SHA256(key="WebAppData", msg=bot_token)
    secret_key = hmac.new(
        key=b"WebAppData",
        msg=bot_token.encode(),
        digestmod=hashlib.sha256
    ).digest()

    # hash = HMAC_SHA256(key=secret_key, msg=data_check_string)
    calculated_hash = hmac.new(
        key=secret_key,
        msg=data_check_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    data["hash"] = calculated_hash

    # URL-encode into final init_data query string (order doesn't matter here)
    init_data_str = urllib.parse.urlencode(data)
    return init_data_str


if __name__ == "__main__":
    import os

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "PASTE_YOUR_BOT_TOKEN_HERE")
    TELEGRAM_USER_ID = int(os.environ.get("TG_USER_ID", "123456789"))

    init_data = generate_init_data(BOT_TOKEN, TELEGRAM_USER_ID)
    print("X-Init-Data header value:\n")
    print(init_data)