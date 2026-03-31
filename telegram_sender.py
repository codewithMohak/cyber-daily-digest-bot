import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

TELEGRAM_LIMIT = 4000  # safe below actual Telegram limit

def split_message(message, limit=TELEGRAM_LIMIT):
    chunks = []
    while len(message) > limit:
        split_index = message.rfind("\n\n", 0, limit)
        if split_index == -1:
            split_index = limit
        chunks.append(message[:split_index])
        message = message[split_index:].strip()
    chunks.append(message)
    return chunks

def send_telegram_message(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("[ERROR] Telegram credentials missing.")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    chunks = split_message(message)

    for i, chunk in enumerate(chunks, start=1):
        payload = {
            "chat_id": str(TELEGRAM_CHAT_ID).strip(),
            "text": chunk,
            "disable_web_page_preview": True
        }

        try:
            response = requests.post(url, json=payload, timeout=30)

            print(f"[DEBUG] Sending chunk {i}/{len(chunks)}")
            print("[DEBUG] Telegram Status Code:", response.status_code)
            print("[DEBUG] Telegram Response:", response.text)

            response.raise_for_status()

        except requests.exceptions.HTTPError:
            print("[ERROR] Telegram API rejected the request.")
            print("[ERROR] Full Telegram Response:", response.text)
            return False

        except Exception as e:
            print(f"[ERROR] Failed to send Telegram message: {e}")
            return False

    print("[INFO] Telegram message sent successfully.")
    return True