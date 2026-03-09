import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import requests
from faster_whisper import WhisperModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Deepgram API
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

# Local fallback
local_model = WhisperModel("small", compute_type="int8")


def record_audio():
    samplerate = 16000
    duration = 3

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    return samplerate, audio


def deepgram_stt(samplerate, audio):

    wav.write("temp.wav", samplerate, audio)

    url = "https://api.deepgram.com/v1/listen"

    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}",
        "Content-Type": "audio/wav"
    }

    with open("temp.wav", "rb") as f:
        response = requests.post(url, headers=headers, data=f)

    if response.status_code == 200:

        result = response.json()

        try:
            text = result["results"]["channels"][0]["alternatives"][0]["transcript"]
            return text.lower()
        except:
            return None

    return None


def local_stt(audio):

    audio = audio.flatten().astype("float32") / 32768.0

    segments, _ = local_model.transcribe(audio, language="multi", beam_size=5)

    text = ""

    for seg in segments:
        text += seg.text

    return text.strip().lower()


def take_command():

    print("Listening...")

    samplerate, audio = record_audio()

    # Try Deepgram first
    text = deepgram_stt(samplerate, audio)

    if text:
        print("Heard:", text)
        return text

    # Fallback to local whisper
    text = local_stt(audio)

    if text:
        print("Heard (offline):", text)

    return text