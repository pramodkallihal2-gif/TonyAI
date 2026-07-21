import webbrowser
import requests
import datetime
import os
from intent_router import route
from system_control import execute_system_command
from avatar import update_status, app
from memory import (
    load_long_memory,
    save_long_memory,
    update_memory,
    recall_memory,
    add_to_history,
    load_profile,
    get_history
)
from local_brain import local_brain



# ---------------- OLLAMA ---------------- #

def ollama_brain(command):
    update_status("think.PNG")

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

    response = route(command)

    if response:
        return response

    return ollama_brain(command)