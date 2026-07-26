
SKILL_NAME = "Weather"
KEYWORDS = [
    "weather"
]
VERSION = "1.0"
DESCRIPTION = "Provides weather information for a specified location."

def handle(command):

    command = command.lower()

    if "weather" not in command:
        return None

    return "Weather feature is under development."