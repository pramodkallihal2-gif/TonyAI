import json
import os

PROFILE_FILE = "profile.json"
LONG_MEMORY_FILE = "long_memory.json"

conversation_history = []

MEMORY_FILE = "long_memory.json"


def load_long_memory():

    if not os.path.exists(MEMORY_FILE):

        return {
            "profile": {},
            "preferences": [],
            "goals": [],
            "projects": []
        }

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_long_memory(memory):

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

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
def update_memory(command):

    command = command.lower()

    memory = load_long_memory()

    # Name
    if command.startswith("my name is"):

        memory["profile"]["name"] = (
            command.replace("my name is", "")
            .strip()
            .title()
        )

    # College
    elif command.startswith("i study at"):

        memory["profile"]["college"] = (
            command.replace("i study at", "")
            .strip()
        )

    # Branch
    elif command.startswith("my branch is"):

        memory["profile"]["branch"] = (
            command.replace("my branch is", "")
            .strip()
        )

    # Goal
    elif command.startswith("i want to"):

        memory["goals"].append(command)

    # Preference
    elif command.startswith("i like"):

        memory["preferences"].append(command)

    # Project
    elif "project" in command:

        memory["projects"].append(command)

    save_long_memory(memory)

    return False
def recall_memory(command):

    memory = load_long_memory()

    command = command.lower()

    if "my name" in command:

        return (
            memory["profile"]
            .get("name", "I don't know your name yet.")
        )

    if "my college" in command:

        return (
            memory["profile"]
            .get("college", "I don't know your college yet.")
        )

    if "branch" in command:

        return (
            memory["profile"]
            .get("branch", "I don't know your branch yet.")
        )

    return None


