import wikipedia
SKILL_NAME = "Wikipedia"
KEYWORDS = [    
    "who is"
]

def handle(command):

    command = command.lower()

    if not command.startswith("who is"):
        return None

    person = command.replace("who is", "").strip()

    try:

        summary = wikipedia.summary(
            person,
            sentences=2
        )

        return summary

    except:

        return "I couldn't find information."