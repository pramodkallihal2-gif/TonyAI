from email.mime import text

from config import user_name, assistant_name
from voice import speak
from listener import take_command
from brain import generate_response
import sys

WAKE_WORDS = ["tony", "toni"]
SLEEP_WORDS = ["sleep", "go to sleep"]

def main():

    active_mode = False
    waiting_for_shutdown = False
    speak(f"{assistant_name} is ready.")

    while True:
        text = take_command()

        if not text:
            continue

        # Waiting for shutdown confirmation
        if waiting_for_shutdown:

            if any(word in text for word in ["yes", "yeah", "confirm", "bye tony", "goodbye"]):
                speak("Terminating program.")
                return

            elif any(word in text for word in ["no", "cancel", "don't"]):
                speak("Shutdown cancelled.")
                waiting_for_shutdown = False
                continue

            else:
                speak("Please say yes or no.")
                continue
        

        # ----------- STANDBY MODE -----------
        if not active_mode:
            if any(word in text for word in WAKE_WORDS):
                active_mode = True
                speak("Yes, sir. How can I assist you?")
            continue
        # ----------- ACTIVE MODE ------------

        # Sleep command
        if any(word in text for word in SLEEP_WORDS):
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
            speak("Do you want to terminate the program?")
            waiting_for_shutdown = True
            continue



        # Normal command
        response = generate_response(text)
        speak(response)


if __name__ == "__main__":
    main()