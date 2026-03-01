import webbrowser
import requests
import datetime
import os
import profile
from memory import add_to_history, get_history, load_profile,save_long_memory,load_long_memory  
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

def cloud_brain(command):
    
    command = command.lower()
    
    from memory import load_profile
    profile = load_profile()

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

    # ---------- MEMORY HANDLING ----------
    
    long_memory = load_long_memory()

    # Simple automatic memory extraction
    if command.startswith("i am") or command.startswith("my ") or command.startswith("i like") or command.startswith("i want"):
        key = f"fact_{len(long_memory)+1}"
        long_memory[key] = command
        save_long_memory(long_memory)

    if command.startswith("remember that"):
        fact = command.replace("remember that", "").strip()
        long_memory["fact"] = fact
        save_long_memory(long_memory)
        return "Okay, I will remember that."

    if "what did i tell you" in command or "what do you remember" in command or "what is in your memory" in command:
        return long_memory.get("fact", "You haven't told me anything yet.")

    # ---------- CLOUD AI FOR GENERAL QUESTIONS ----------
        profile = load_profile()

    add_to_history("user", command)

    messages = [
    {
        "role": "system",
        "content": f"""
    You are Tony, a personal AI assistant.

    User profile:
    Name: {profile.get("name")}
    College: {profile.get("college")}
    Branch: {profile.get("branch")}
    Interests: {profile.get("interests")}
    Goal: {profile.get("goal")}

    Use this information naturally when relevant.
    Answer briefly in 1-2 short sentences.
    If you don't know the answer, say you don't know instead of making something up."""
    }
]

    messages.extend(get_history())

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Tony Assistant"
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 100
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=8)

        if response.status_code != 200:
            return "Cloud service unavailable."

        result = response.json()

        if "choices" in result:
            reply = result["choices"][0]["message"]["content"].strip()
            add_to_history("assistant", reply)
            return reply
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
