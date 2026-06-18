import speech_recognition as sr

recognizer = sr.Recognizer()

def take_command():

    try:

        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            print("Listening...")

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        text = recognizer.recognize_google(audio)

        text = text.lower()

        print("Heard:", text)

        return text

    except sr.WaitTimeoutError:
        return None

    except sr.UnknownValueError:
        return None

    except Exception as e:
        print("STT Error:", e)
        return None