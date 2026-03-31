# 🧠 Cyber Daily Digest Bot

A Python-based cybersecurity digest bot that fetches the latest cyber updates from RSS feeds, summarizes them using the Groq API, and sends a clean daily briefing to Telegram.

## 🚀 Features
- Pulls the latest cybersecurity news from RSS feeds
- Filters only fresh posts from the last 24 hours
- Avoids duplicate articles using seen link tracking
- Summarizes each item with Groq LLM
- Sends a clean digest directly to Telegram
- Can run automatically every morning using cron / Task Scheduler

## 🛠️ Tech Stack
- Python
- feedparser
- requests
- python-dotenv
- python-dateutil
- Groq API
- Telegram Bot API

## 📡 Sources Used
- PortSwigger Research
- Google Project Zero
- The Hacker News
- Snyk Blog
- CISA Alerts
- Bugcrowd Blog
- Intigriti Blog
- NVD CVE Feed

## 📂 Project Structure
```bash
main.py              # Main workflow
feeds.py             # RSS fetching
filters.py           # Freshness + duplicate filtering
summarizer.py        # Groq API summarization
formatter.py         # Digest formatting
telegram_sender.py   # Telegram delivery
config.py            # Config and feeds
seen_links.json      # Stores already sent links

⚙️ Setup
1. Clone the repo
git clone https://github.com/yourusername/cyber-daily-digest-bot.git
cd cyber-daily-digest-bot
2. Install dependencies
pip install -r requirements.txt
3. Add environment variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
MAX_ITEMS=5
4. Run the bot
python main.py
⏰ Automation

You can schedule this bot to run every morning using:

cron (Linux / WSL / Parrot / Kali)
Task Scheduler (Windows)

Example cron job:

0 7 * * * /usr/bin/python3 /full/path/to/main.py >> /full/path/to/digest.log 2>&1
📌 Why I Built This

Cybersecurity moves fast, and reading everything manually is overwhelming.
This bot helps turn scattered updates into a short, readable daily briefing.

🔮 Future Improvements
Prioritize high-value CVEs
Add category-based sections
Save digest to Markdown / Notion
Add a web dashboard
Better ranking of important stories
