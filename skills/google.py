import webbrowser
from urllib.parse import quote

SKILL_NAME = "Google"

KEYWORDS = [
    "google",
    "search"
]

def handle(command):

    command = command.lower()

    if "google" not in command:
        return None

    if command == "open google":
        webbrowser.open("https://google.com")
        return "Opening Google."

    query = (
        command
        .replace("search google for", "")
        .replace("google", "")
        .strip()
    )

    if not query:
        return None

    webbrowser.open(
        f"https://www.google.com/search?q={quote(query)}"
    )

    return f"Searching Google for {query}."