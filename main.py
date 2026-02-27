from config import user_name, assistant_name
from voice import speak
from listener import take_command
from brain import generate_response

WAKE_WORDS = ["tony", "toni"]
SLEEP_WORDS = ["sleep", "go to sleep"]

def main():

    active_mode = False
    speak(f"{assistant_name} is ready.")

    while True:
        text = take_command()

        if not text:
            continue

        print("Heard:", text)
        

        # ----------- STANDBY MODE -----------
        if not active_mode:
            if any(word in text for word in WAKE_WORDS):
                active_mode = True
                speak("Yes, I am listening.")
            continue
        # ----------- ACTIVE MODE ------------

        # Sleep command
        if any(word in text for word in SLEEP_WORDS):
            speak("Going to standby mode.")
            active_mode = False
            continue
        # Shutdown completely
        if any(word in text for word in ["shut down", "deactivate"]):
            speak("Do you want to terminate the program?")
            confirm = take_command()
            if any(word in confirm for word in ["yes", "terminate"]):
                speak("Terminating program.")
                break



        # Normal command
        response = generate_response(text)
        speak(response)


if __name__ == "__main__":
    main()