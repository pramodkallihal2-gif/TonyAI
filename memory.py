import json
import os

PROFILE_FILE = "profile.json"
LONG_MEMORY_FILE = "long_memory.json"

conversation_history = []

# ---------- Short Term ----------
def add_to_history(role, content):
    conversation_history.append({"role": role, "content": content})
    if len(conversation_history) > 10:
        conversation_history.pop(0)

def get_history():
    return conversation_history


# ---------- Profile ----------
def load_profile():
    if not os.path.exists(PROFILE_FILE):
        return {}
    with open(PROFILE_FILE, "r") as f:
        return json.load(f)


# ---------- Long Memory ----------
MEMORY_FILE = "long_memory.json"

def load_long_memory():

    if not os.path.exists(MEMORY_FILE):
        return {
            "profile": {},
            "goals": [],
            "preferences": [],
            "projects": [],
            "facts": []
        }

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_long_memory(memory):

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

