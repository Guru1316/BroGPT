import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def ask_groq(message):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.1-8b-instant",  # You can also try llama3-8b-8192
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        # DEBUGGING: Print entire response
        print("🔍 Groq Response:", result)

        if 'choices' in result:
            return result['choices'][0]['message']['content'].strip()
        elif 'error' in result:
            return f"⚠️ API Error: {result['error']['message']}"
        else:
            return "⚠️ Unexpected response format."

    except Exception as e:
        return f"❌ Error: {str(e)}"
