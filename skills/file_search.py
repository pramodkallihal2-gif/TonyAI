import os
SKILL_NAME = "File Search"
KEYWORDS = [
    "open folder"
]

def handle(command):

    command = command.lower()

    if not command.startswith("open folder"):
        return None

    folder = command.replace("open folder", "").strip()

    if os.path.exists(folder):

        os.startfile(folder)

        return "Opening folder."

    return "Folder not found."