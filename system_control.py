import os
import webbrowser
import subprocess
from avatar import update_status, app


def execute_system_command(command):

    command = command.lower()

    # Chrome
    if "open chrome" in command:
        os.system("start chrome")
        update_status("system.PNG")
        return "Opening Chrome."

    # VS Code
    if "open vscode" in command or "open vs code" in command:
        os.system("code")
        update_status("system.PNG")
        return "Opening Visual Studio Code."

    # YouTube
    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        update_status("system.PNG")
        return "Opening YouTube."
    
    #youtube search
    if command.startswith("search youtube for"):

        query = (
            command.replace(
                "search youtube for",
                "",1
            ).strip()
        )
        print("Search:", query)

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={query}"
        )
        update_status("system.PNG")
        return f"Searching YouTube for {query}"
    # Search
    if (
         command.startswith("google")
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
        update_status("system.PNG")

        return "What should I search for?"
    # Google
    if "open google" in command:
        webbrowser.open("https://google.com")
        update_status("system.PNG")
        return "Opening Google."

    # Downloads
    if "open downloads" in command:
        os.startfile(os.path.expanduser("~/Downloads"))
        update_status("system.PNG")
        return "Opening Downloads folder."

    return None