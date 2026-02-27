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
        "X-Title": "Chhanukya Assistant"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "system", "content": "You are Chhanukya, a smart and concise AI assistant."},
            {"role": "user", "content": command}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=15  # Prevent infinite waiting
        )

        if response.status_code != 200:
            print("OpenRouter Status:", response.status_code)
            print("OpenRouter Response:", response.text)
            return local_brain(command)

        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"].strip()
        else:
            print("Unexpected Response:", result)
            return local_brain(command)

    except requests.exceptions.Timeout:
        print("Cloud Timeout")
        return local_brain(command)

    except Exception as e:
        print("Cloud Exception:", e)
        return local_brain(command)


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
