import requests
from config import GROQ_API_KEY

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def summarize_text(title, content):
    if not GROQ_API_KEY:
        return "Groq API key missing."

    prompt = f"""
You are a cybersecurity digest assistant.

Summarize the following cybersecurity article in:
1. Maximum 2 very short sentences
2. Keep total summary under 35 words
3. Focus only on the most important takeaway
4. Make it useful for a cybersecurity learner or practitioner

Title: {title}

Content:
{content[:3000]}
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You summarize cybersecurity content clearly and concisely."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(GROQ_URL, headers=headers, json=payload, timeout=30)
        print(response.text) 
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"[ERROR] Groq summarization failed: {e}")
        return "Summary unavailable."