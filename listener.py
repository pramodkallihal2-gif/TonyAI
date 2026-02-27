import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

model = Model("vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model, 16000)

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def take_command():
    print("Listening...")

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback
    ):
        while True:
            data = q.get()
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "")
                if text != "":
                    print("You:", text)
                    return text.lower()