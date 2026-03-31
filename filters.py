import json
import os
from datetime import datetime, timedelta, timezone
from dateutil import parser

SEEN_FILE = "seen_links.json"

def load_seen_links():
    if not os.path.exists(SEEN_FILE):
        return set()

    try:
        with open(SEEN_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data)
    except:
        return set()

def save_seen_links(seen_links):
    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(list(seen_links), f, indent=2)

def is_recent(published_str, hours=24):
    if not published_str or published_str == "Unknown Date":
        return False

    try:
        published_dt = parser.parse(published_str)

        if published_dt.tzinfo is None:
            published_dt = published_dt.replace(tzinfo=timezone.utc)

        now = datetime.now(timezone.utc)
        cutoff = now - timedelta(hours=hours)

        return published_dt >= cutoff

    except Exception:
        return False

def filter_new_entries(entries):
    seen_links = load_seen_links()
    new_entries = []

    for entry in entries:
        if entry["link"] not in seen_links and is_recent(entry.get("published", "")):
            new_entries.append(entry)

    return new_entries

def mark_entries_as_seen(entries):
    seen_links = load_seen_links()
    for entry in entries:
        seen_links.add(entry["link"])
    save_seen_links(seen_links)