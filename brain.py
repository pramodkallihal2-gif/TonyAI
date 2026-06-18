import webbrowser
import requests
import datetime
import os

from memory import (
    add_to_history,
    get_history,
    load_profile,
    load_long_memory,
    save_long_memory
)


# ---------------- LOCAL COMMANDS ---------------- #

def local_brain(command):

    command = command.lower()
    if "recall my memory" in command:

        memory = load_long_memory()

        return (
            f"Your name is {memory['profile'].get('name', 'unknown')}. "
            f"You are working toward {', '.join(memory['goals'])}."
        )
    # Greetings
    if any(word in command for word in ["hello", "hi", "hey"]):
        return "Hello. How can I help you?"

    # Time
    if "time" in command:
        return datetime.datetime.now().strftime(
            "The time is %I:%M %p"
        )

    # Date
    if "date" in command:
        return datetime.datetime.now().strftime(
            "Today is %A, %d %B %Y"
        )

    # VS Code
    if (
        "open vs code" in command
        or "open vscode" in command
        or "open code" in command
        or "open vs" in command
    ):
        os.system("code")
        return "Opening Visual Studio Code."

    # Browser
    if "open google" in command or "open browser" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    # Search
    if (
        command.startswith("search")
        or command.startswith("google")
        or command.startswith("search for")
    ):

        query = (
            command.replace("search for", "")
            .replace("search", "")
            .replace("google", "")
            .strip()
        )

        if query:
            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )
            return f"Searching for {query}"

        return "What should I search for?"

    return None


# ---------------- MEMORY ---------------- #

def update_memory(command):

    command = command.lower()

    memory = load_long_memory()

    if (
        command.startswith("i am")
        or command.startswith("my ")
        or command.startswith("i like")
        or command.startswith("i want")
    ):

        key = f"fact_{len(memory)+1}"
        memory[key] = command
        save_long_memory(memory)


# ---------------- OLLAMA ---------------- #

def ollama_brain(command):

    profile = load_profile()
    memory = load_long_memory()

    add_to_history("user", command)

    conversation = ""

    for msg in get_history():
        conversation += (
            f"{msg['role']}: {msg['content']}\n"
        )

    prompt = f"""
You are Tony, a personal AI assistant.

User Profile:
Name: {profile.get('name')}
College: {profile.get('college')}
Branch: {profile.get('branch')}
Interests: {profile.get('interests')}
Goal: {profile.get('goal')}

User Memory:
{memory}
Memory:
{memory}
Recent Conversation:
{conversation}

Rules:
- Keep responses concise.
- Be helpful and friendly.
- Reply in 1 or 2 short sentences.
- Do not ask follow-up questions unless necessary.
- Be concise.
- Use user profile when relevant.
- If unsure, say you do not know.
- Answer in 1 to 3 sentences unless asked for detail.

User: {command}

Tony:
"""

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        if response.status_code != 200:
            return "Ollama returned an error."

        result = response.json()

        reply = result.get("response", "").strip()

        add_to_history("assistant", reply)

        return reply

    except Exception as e:
        return f"Ollama connection error: {e}"


# ---------------- MAIN RESPONSE ---------------- #

def generate_response(command):

    # Local commands first
    local_response = local_brain(command)

    if local_response:
        return local_response

    # Update memory
    update_memory(command)

    # Ollama response
    return ollama_brain(command)