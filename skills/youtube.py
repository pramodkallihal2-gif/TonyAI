import webbrowser
from urllib.parse import quote
SKILL_NAME = "YouTube"

KEYWORDS = [
    "youtube",
    "play",
    "video"
]
DESCRIPTION = "Searches and plays videos on YouTube."
VERSION = "1.0"

def handle(command):

    command = command.lower()

    if "youtube" not in command:
        return None

    # Open YouTube
    if command in ["youtube", "open youtube"]:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube."

    # Search YouTube
    if "search youtube for" in command:
        query = command.replace("search youtube for", "").strip()

    elif "play" in command:
        query = command.replace("play", "").replace("on youtube", "").strip()

    else:
        return None

    webbrowser.open(
        f"https://www.youtube.com/results?search_query={quote(query)}"
    )

    return f"Searching YouTube for {query}."