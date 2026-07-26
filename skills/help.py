from skill_loader import list_skills

SKILL_NAME = "Help"

DESCRIPTION = "Lists all installed skills."

VERSION = "1.0"

KEYWORDS = [
    "help",
    "skills",
    "what can you do"
]
DESCRIPTION = "Lists all installed skills."
VERSION = "1.0"
def handle(command):

    command = command.lower()

    if not any(k in command for k in KEYWORDS):
        return None

    text = "I currently have these skills:\n\n"

    for skill in list_skills():

        text += (
            f"{skill['name']} "
            f"(v{skill['version']})\n"
            f"- {skill['description']}\n\n"
        )

    return text+'''\n I can also be extended with custom skills. 
Give you information on a wide range of topics.
with the help help of inbuilt model.\n'''