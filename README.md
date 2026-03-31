# 🧠 Cyber Daily Digest Bot

> A Python-based cybersecurity bot that fetches the latest updates from trusted RSS feeds, summarizes them using the Groq API, and delivers a clean daily digest to Telegram every morning.

---

## ✨ Overview

Cybersecurity moves fast. Blogs, CVEs, write-ups, advisories, and research posts pile up every day.

This project solves that problem by turning scattered updates into a **short, readable morning briefing**.

With this bot, you can:

* stay updated without doom-scrolling
* read the latest cyber news in **5 minutes**
* automate your daily learning workflow
* build consistency as a student, SOC analyst, or bug bounty learner

---

## 🚀 Features

* 📰 Pulls the latest cybersecurity updates from RSS feeds
* ⏱️ Filters only **fresh posts from the last 24 hours**
* ♻️ Avoids duplicate articles using seen-link tracking
* 🧠 Summarizes each item using **Groq LLM**
* 📩 Sends a clean daily digest directly to **Telegram**
* ⚙️ Supports **automatic daily execution**

  * `cron` for Linux / WSL / Kali / Parrot
  * `Task Scheduler` for Windows

---

## 🛠️ Tech Stack

| Category              | Tools            |
| --------------------- | ---------------- |
| Language              | Python           |
| Parsing               | feedparser       |
| HTTP Requests         | requests         |
| Environment Variables | python-dotenv    |
| Date Handling         | python-dateutil  |
| AI Summarization      | Groq API         |
| Delivery              | Telegram Bot API |

---

## 📡 Sources Used

This bot currently tracks updates from:

* PortSwigger Research
* Google Project Zero
* The Hacker News
* Snyk Blog
* CISA Alerts
* Bugcrowd Blog
* Intigriti Blog
* NVD CVE Feed

> You can easily customize the source list inside `config.py`.

---

## 📂 Project Structure

```bash
cyber-daily-digest-bot/
│
├── main.py              # Main workflow
├── feeds.py             # RSS feed fetching
├── filters.py           # Freshness + duplicate filtering
├── summarizer.py        # Groq API summarization
├── formatter.py         # Digest formatting
├── telegram_sender.py   # Telegram delivery
├── config.py            # Config + RSS feed definitions
├── seen_links.json      # Stores already sent links
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
├── .gitignore           # Ignore secrets and cache files
└── README.md            # Project documentation
```

---

## ⚙️ Setup

### 1) Clone the Repository

```bash
git clone https://github.com/yourusername/cyber-daily-digest-bot.git
cd cyber-daily-digest-bot
```

### 2) Install Dependencies

```bash
pip install -r requirements.txt
```

### 3) Add Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
MAX_ITEMS=5
```

### 4) Run the Bot

```bash
python main.py
```

If configured correctly, the bot will:

* fetch fresh cybersecurity updates
* summarize them using Groq
* send a clean digest to Telegram

---

## ⏰ Automation

Once tested manually, you can schedule the bot to run automatically every morning.

---

### 🐧 Linux / WSL / Kali / Parrot — Using `cron`

Open your crontab:

```bash
crontab -e
```

Add this line:

```bash
0 7 * * * /usr/bin/python3 /full/path/to/cyber-daily-digest-bot/main.py >> /full/path/to/cyber-daily-digest-bot/digest.log 2>&1
```

#### Example

```bash
0 7 * * * /usr/bin/python3 /home/mohak/cyber-daily-digest-bot/main.py >> /home/mohak/cyber-daily-digest-bot/digest.log 2>&1
```

**What this does:**

* Runs the bot **every day at 7:00 AM**
* Saves logs to `digest.log`

---

### 🪟 Windows — Using Task Scheduler

1. Open **Task Scheduler**
2. Click **Create Basic Task**
3. Set:

   * **Name:** `Cyber Daily Digest Bot`
   * **Trigger:** `Daily`
   * **Time:** `7:00 AM`
4. Choose **Start a Program**

#### Program / Script

```bash
python
```

> If Python is not recognized, use the full Python path:

```bash
C:\Users\YourName\AppData\Local\Programs\Python\Python312\python.exe
```

#### Add Arguments

```bash
C:\Users\YourName\Desktop\cyber-daily-digest-bot\main.py
```

#### Start In

```bash
C:\Users\YourName\Desktop\cyber-daily-digest-bot
```

After setup, the bot will run **automatically every day at 7:00 AM**.

---

## 📌 Why I Built This

One of the biggest problems in cybersecurity is **information overload**.

There is too much happening every day:

* new CVEs
* new research write-ups
* new bug bounty techniques
* new threat reports

Instead of manually checking everything, I wanted a simple system that gives me a **5-minute cyber briefing every morning**.

This project was built to make learning:

* more consistent
* more practical
* more efficient

---

## 🔮 Future Improvements

Planned upgrades for future versions:

* Prioritize **high-value / critical CVEs**
* Add category-based sections:

  * Web
  * CVEs
  * Threat Intel
  * Research
* Save digest to **Markdown / Notion / Obsidian**
* Add a simple **web dashboard**
* Improve ranking of important stories
* Add keyword-based filtering
* Replace JSON tracking with **SQLite**

---

## 🧪 Example Use Case

### Every Morning at 7:00 AM:

* the bot fetches the latest cyber updates
* filters only fresh unseen entries
* summarizes them using AI
* sends a Telegram digest

☕ Result: you read your daily cyber briefing in under **5 minutes**.

---

## 🤝 Contributing

Suggestions, improvements, and custom source ideas are always welcome.

If you want to improve the bot, feel free to fork the project and experiment.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## ⭐ If You Found This Useful

If you like the project, consider giving it a **star** on GitHub.

It helps more people discover it and motivates future improvements 🚀
