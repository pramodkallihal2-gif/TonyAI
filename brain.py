import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY ="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"

# ===============================
# Internet Check
# ===============================
def is_online():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except:
        return False


# ===============================
# Cloud Brain (OpenRouter)
# ===============================
def cloud_brain(command):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Chhanukya"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": command}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    print("Status:", response.status_code)
    print("Response:", response.text)

    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return "Cloud AI error occurred."


# ===============================
# Local Brain (Fallback)
# ===============================
def local_brain(command):

    if "hello" in command:
        return "Hello! I am running in offline mode."

    elif "time" in command:
        import datetime
        return datetime.datetime.now().strftime("The time is %I:%M %p")

    else:
        return "I am offline and still learning."


# ===============================
# Main Brain Interface
# ===============================
def generate_response(command):

    if is_online():
        return cloud_brain(command)
    else:
        return local_brain(command)
