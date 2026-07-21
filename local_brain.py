import datetime
from memory import load_long_memory
from avatar import update_status

def local_brain(command):

    command = command.lower()
    if "my memory" in command:

        memory = load_long_memory()
        update_status("recall.PNG")

        return (
            f"Your name is {memory['profile'].get('name', 'unknown')}. "
            f"You are working toward {', '.join(memory['goals'])}."
        )
    # Greetings
    words = command.split()

    if any(word in words for word in ["hello", "hi", "hey"]):
        update_status("greet.PNG")
        return "Hello. How can I help you?"

    # Time
    if "time" in command:
        update_status("time.PNG")
        return datetime.datetime.now().strftime(
            "The time is %I:%M %p"
        )

    # Date
    if "date" in command:
        update_status("date.PNG")
        return datetime.datetime.now().strftime(
            "Today is %A, %d %B %Y"
        )
    return None