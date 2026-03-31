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
````

⚙️ Setup
1. Clone the Repository
``git clone https://github.com/yourusername/cyber-daily-digest-bot.git``
``cd cyber-daily-digest-bot``
2. Install Dependencies
``pip install -r requirements.txt``
3. Add Environment Variables

Create a .env file in the project root:

``GROQ_API_KEY=your_groq_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
MAX_ITEMS=5``

4. Run the Bot
``python main.py``

If everything is configured correctly, the bot will:

Fetch fresh cybersecurity updates
Summarize them using Groq
Send a daily digest to Telegram
⏰ Automation

You can schedule this bot to run automatically every morning.

🐧 Linux / WSL / Kali / Parrot — Using cron
Open your crontab:
``crontab -e``
Add this line:
``0 7 * * * /usr/bin/python3 /full/path/to/cyber-daily-digest-bot/main.py >> /full/path/to/cyber-daily-digest-bot/digest.log 2>&1``
Example:
``0 7 * * * /usr/bin/python3 /home/mohak/cyber-daily-digest-bot/main.py >> /home/mohak/cyber-daily-digest-bot/digest.log 2>&1``
What this does:
Runs the bot every day at 7:00 AM
Saves logs to digest.log

🪟 Windows — Using Task Scheduler
Steps to schedule the bot daily:
1. Open Task Scheduler
``Press Windows Key``
Search for Task Scheduler
``Open it``
2. Click Create Basic Task

Set:

Name: Cyber Daily Digest Bot
Description: Runs the cybersecurity digest bot every morning
3. Choose Trigger

Select:

Daily

Then set the time:

7:00 AM
4. Choose Action

Select:

Start a Program
5. Program / Script

Enter:

python

If Python is not recognized, use the full Python path, for example:
``C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe``

6. Add Arguments
Enter the full path to your main.py file:
``C:\Users\YourName\Desktop\cyber-daily-digest-bot\main.py``

7. Start In (Optional but Recommended)
Enter the project folder path:
``C:\Users\YourName\Desktop\cyber-daily-digest-bot``

9. Finish

Click Finish

Your bot will now run automatically every day at 7:00 AM.

📌 Why I Built This

Cybersecurity moves fast, and keeping up manually can become overwhelming.
This project was built to solve a simple problem:
How can I stay up to date every day without spending hours scrolling through blogs, CVEs, and write-ups?
This bot turns scattered security updates into a short, readable daily briefing.
It is designed to make learning more consistent, practical, and efficient.
🔮 Future Improvements

Planned upgrades for future versions:

Prioritize high-value / critical CVEs
Add category-based sections (Web, CVEs, Threat Intel, Research)
Save digest to Markdown / Notion / Obsidian
Add a simple web dashboard
Better ranking of important stories
Keyword-based filtering
SQLite database instead of JSON tracking
