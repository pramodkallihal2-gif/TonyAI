
SKILL_NAME = "Reminder"
KEYWORDS = [
    "remind me"
]

def handle(command):

    command = command.lower()

    if "remind me" not in command:
        return None

    return "Reminder feature coming soon."