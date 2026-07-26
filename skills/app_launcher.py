import subprocess
SKILL_NAME = "App Launcher"
KEYWORDS = [
    "open"
]
DESCRIPTION = "Launches applications on your computer."
VERSION = "1.0"

def handle(command):

    command = command.lower()

    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "instagram": "C:\\Users\\pramo\\AppData\\Local\\Programs\\Instagram\\Instagram.exe",
        "whatsapp": "C:\\Users\\pramo\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
        "chatgpt": "C:\\Users\\pramo\\AppData\\Local\\Programs\\ChatGPT\\ChatGPT.exe"
    }

    for app in apps:

        if f"open {app}" == command:

            subprocess.Popen(apps[app])

            return f"Opening {app.title()}."

    return None