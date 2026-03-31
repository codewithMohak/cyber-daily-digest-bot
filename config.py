import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
MAX_ITEMS = int(os.getenv("MAX_ITEMS", 8))

# Keep v1 small and useful
RSS_FEEDS = {
    "PortSwigger Research": "https://portswigger.net/research/rss",
    "Google Project Zero": "https://googleprojectzero.blogspot.com/feeds/posts/default?alt=rss",
    "The Hacker News": "https://feeds.feedburner.com/TheHackersNews",
    "Snyk Blog": "https://snyk.io/blog/feed/",
    "CISA Alerts": "https://www.cisa.gov/news-events/cybersecurity-advisories/all.xml",
    "Bugcrowd Blog": "https://www.bugcrowd.com/blog/feed/",
    "Intigriti Blog": "https://blog.intigriti.com/feed/",
    "NVD CVE Feed": "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss-analyzed.xml",
}