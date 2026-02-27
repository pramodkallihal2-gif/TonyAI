import webbrowser
import requests
import datetime
import os   

API_KEY = "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"

def cloud_brain(command):

    command = command.lower()

    # ---------- PRIORITY LOCAL TASKS (Even When Online) ----------
    if "time" in command:
        return datetime.datetime.now().strftime("The time is %I:%M %p")

    if "date" in command:
        return datetime.datetime.now().strftime("Today is %A, %d %B %Y")
    if "open vs code" in command or "open vscode" in command or "open vs" in command or "open code" in command:
        os.system("code")
        return "Opening Visual Studio Code."

    if "open google" in command or "open browser" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    if command.startswith("search") or command.startswith("google") or command.startswith("search for"):
        query = command.replace("search", "").replace("google", "").replace("search for", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return f"Searching for {query}"
        else:
            return "What should I search for?"

    # ---------- CLOUD AI FOR GENERAL QUESTIONS ----------

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Tony Assistant"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {
                "role": "system",
                "content": "You are Tony. Answer briefly in 1 to 2 short sentences only."
            },
            {
                "role": "user",
                "content": command
            }
        ],
        "temperature": 0.3,
        "max_tokens": 100
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=8)

        if response.status_code != 200:
            return "Cloud service unavailable."

        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"].strip()
        else:
            return "Unexpected cloud response."

    except:
        return "Cloud request failed."


def local_brain(command):

    command = command.lower()

    # ---------- GREETINGS ----------
    if any(word in command for word in ["hello", "hi", "hey"]):
        return "Hello. How can I help you?"

    # ---------- TIME ----------
    if "time" in command:
        return datetime.datetime.now().strftime("The time is %I:%M %p")

    # ---------- DATE ----------
    if "date" in command:
        return datetime.datetime.now().strftime("Today is %A, %d %B %Y")

    # ---------- OPEN APPS ----------

    if "open vs code" in command or "open vscode" in command:
        os.system("code")
        return "Opening Visual Studio Code."

    # ---------- SHUTDOWN ----------
    if "shutdown" in command:
        return "Shutdown command detected. I will not execute it without confirmation."
        

    # ---------- DEFAULT ----------
    return "I am offline and still learning. Please connect to internet for advanced responses."





def generate_response(command):
    return cloud_brain(command)
