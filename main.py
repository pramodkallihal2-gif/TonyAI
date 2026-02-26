from config import user_name, assistant_name
from voice import speak
from listener import take_command
from brain import generate_response

def greet():
    speak(f"Hello {user_name}. I am {assistant_name}. How can I help you?")

def main():
    greet()

    while True:
        command = take_command()

        if command == "":
            continue

        if "exit" in command or "bye" in command:
            speak(f"Goodbye {user_name}")
            break

        response = generate_response(command)
        speak(response)

if __name__ == "__main__":
    main()