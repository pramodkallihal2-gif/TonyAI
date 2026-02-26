import pyttsx3

def speak(text):
    print("Assistant:", text)

    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 165)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()