import feedparser
from config import RSS_FEEDS

def fetch_feed_entries(limit_per_feed=5):
    all_entries = []

    for source_name, url in RSS_FEEDS.items():
        try:
            feed = feedparser.parse(url)

            for entry in feed.entries[:limit_per_feed]:
                item = {
                    "source": source_name,
                    "title": entry.get("title", "No Title"),
                    "link": entry.get("link", ""),
                    "summary": entry.get("summary", "") or entry.get("description", ""),
                    "published": entry.get("published", "") or entry.get("updated", "Unknown Date"),
                }
                all_entries.append(item)

        except Exception as e:
            print(f"[ERROR] Failed to fetch {source_name}: {e}")

    return all_entries