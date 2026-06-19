import webbrowser
import requests
import datetime
import os
from system_control import execute_system_command
from avatar import update_status, app
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
    if "recall myself" in command:

        memory = load_long_memory()
        update_status("recall.PNG")

        return (
            f"Your name is {memory['profile'].get('name', 'unknown')}. "
            f"You are working toward {', '.join(memory['goals'])}."
        )
    # Greetings
    words = command.split()

    if any(word in words for word in ["hello", "hi", "hey"]):
        update_status("greet.PNG")
        return "Hello. How can I help you?"

    # Time
    if "time" in command:
        update_status("time.PNG")
        return datetime.datetime.now().strftime(
            "The time is %I:%M %p"
        )

    # Date
    if "date" in command:
        update_status("date.PNG")
        return datetime.datetime.now().strftime(
            "Today is %A, %d %B %Y"
        )
    return None


# ---------------- MEMORY ---------------- #

def update_memory(command):

    command = command.lower()

    memory = load_long_memory()
    update_status("think.PNG")

    if (
        command.startswith("i am")
        or command.startswith("my ")
        or command.startswith("i like")
        or command.startswith("i want")
    ):

        key = f"fact_{len(memory)+1}"
        memory[key] = command
        update_status("update.PNG")
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
        update_status("speak.PNG")

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
    system_response = execute_system_command(command)

    if system_response:
        update_status("system.PNG")
        return system_response

    # Ollama response
    return ollama_brain(command)