from email.mime import text

from config import user_name, assistant_name
from voice import speak
from listener import take_command
from brain import generate_response
from memory import load_long_memory, save_long_memory
import sys
from avatar import update_status, app

WAKE_WORDS = ["tony"]
SLEEP_WORDS = ["sleep", "go to sleep","hold"]

def main():

    active_mode = False
    waiting_for_shutdown = False
    update_status("🤠 Starting...")
    speak(f"{assistant_name} is ready.")

    while True:
        update_status("🎤 Listening...")
        app.processEvents()
        text = take_command()

        if not text:
            continue

        # Waiting for shutdown confirmation
        if waiting_for_shutdown:

            if any(word in text for word in ["yes", "yeah", "confirm", "bye tony", "goodbye"]):
                update_status("😫 Terminating program...")
                speak("Terminating program.")
                return

            elif any(word in text for word in ["no", "cancel", "don't"]):
                update_status("🤩 Shutdown cancelled.")
                speak("Shutdown cancelled.")
                waiting_for_shutdown = False
                continue

            else:
                update_status("🤔 Unclear response.")
                speak("Please say yes or no.")
                continue
        

        # ----------- STANDBY MODE -----------
        if not active_mode:
            if any(word in text for word in WAKE_WORDS):
                active_mode = True
                update_status("🎤 Listening...")
                speak("Yes, sir. How can I assist you?")
            continue
        # ----------- ACTIVE MODE ------------

        # Sleep command
        if any(word in text for word in SLEEP_WORDS):
            update_status("💤 Sleeping...")
            speak("Going to standby mode.")
            active_mode = False
            waiting_for_shutdown = False
            continue
        # Shutdown completely
        if any(word in text for word in [
            "turn off",
            "shutdown",
            "shut down",
            "terminate",
            "exit"
        ]):
            update_status("🥲 Really.... shutdown!")
            speak("Do you want to terminate the program?")
            waiting_for_shutdown = True
            continue


        update_status("🧠 Thinking...")
        # Normal command
        response = generate_response(text)
        speak(response)


if __name__ == "__main__":
    main()
def update_memory(command):

    command = command.lower()

    memory = load_long_memory()

    # Name
    if command.startswith("my name is"):
        memory["profile"]["name"] = (
            command.replace("my name is", "")
            .strip()
            .title()
        )

    # College
    elif "college" in command:
        memory["profile"]["college"] = command

    # Branch
    elif "cse" in command or "computer science" in command:
        memory["profile"]["branch"] = "CSE"

    # Goals
    elif command.startswith("i want to"):
        memory["goals"].append(command)

    # Preferences
    elif command.startswith("i like"):
        memory["preferences"].append(command)

    # Projects
    elif "project" in command:
        memory["projects"].append(command)

    save_long_memory(memory)