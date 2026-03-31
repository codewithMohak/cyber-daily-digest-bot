from feeds import fetch_feed_entries
from filters import filter_new_entries, mark_entries_as_seen
from summarizer import summarize_text
from formatter import format_digest
from telegram_sender import send_telegram_message
from config import MAX_ITEMS

def main():
    print("[INFO] Fetching RSS feeds...")
    entries = fetch_feed_entries(limit_per_feed=5)

    print(f"[INFO] Total fetched: {len(entries)}")

    print("[INFO] Filtering fresh + unseen entries...")
    new_entries = filter_new_entries(entries)

    print(f"[INFO] Fresh new entries found: {len(new_entries)}")

    if not new_entries:
        print("[INFO] No fresh entries found in the last 24 hours.")
        send_telegram_message("🧠 Daily Cyber Digest\n\nNo fresh cyber updates in the last 24 hours. Enjoy your chai ☕")
        return

    selected_entries = new_entries[:MAX_ITEMS]

    print(f"[INFO] Summarizing {len(selected_entries)} entries...")

    for entry in selected_entries:
        text_to_summarize = f"{entry['title']}\n\n{entry['summary']}"
        entry["ai_summary"] = summarize_text(entry["title"], text_to_summarize)

    print("[INFO] Formatting digest...")
    digest_message = format_digest(selected_entries)

    print("[INFO] Sending digest to Telegram...")
    sent = send_telegram_message(digest_message)

    if sent:
        print("[INFO] Marking entries as seen...")
        mark_entries_as_seen(selected_entries)
    else:
        print("[WARNING] Telegram failed, entries will NOT be marked as seen.")

    print("[DONE] Digest completed successfully.")

if __name__ == "__main__":
    main()