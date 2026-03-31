from datetime import datetime

def format_digest(entries):
    today = datetime.now().strftime("%d %b %Y")

    message = f"🧠 *Daily Cyber Digest* — {today}\n"
    message += "☕ Your 5-minute cybersecurity morning brief\n\n"

    for idx, entry in enumerate(entries, start=1):
        message += (
            f"*{idx}. {entry['title']}*\n"
            f"📌 *Source:* {entry['source']}\n"
            f"📝 *Summary:* {entry['ai_summary']}\n"
            f"🔗 {entry['link']}\n\n"
        )

    message += "⚔️ Stay sharp. Read smart."
    return message