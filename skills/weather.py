
SKILL_NAME = "Weather"
KEYWORDS = [
    "weather"
]

def handle(command):

    command = command.lower()

    if "weather" not in command:
        return None

    return "Weather feature is under development."