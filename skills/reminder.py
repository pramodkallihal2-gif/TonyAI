
SKILL_NAME = "Reminder"
KEYWORDS = [
    "remind me"
]
VERSION = "1.0"
DESCRIPTION = "Sets reminders for tasks or events."
def handle(command):

    command = command.lower()

    if "remind me" not in command:
        return None

    return "Reminder feature coming soon."