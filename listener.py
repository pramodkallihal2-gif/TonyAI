import sounddevice as sd
import numpy as np
import webrtcvad
from faster_whisper import WhisperModel

model = WhisperModel("medium", compute_type="int8")

vad = webrtcvad.Vad()
vad.set_mode(2)  # 0-3 (higher = stricter)

SAMPLE_RATE = 16000
FRAME_DURATION = 30  # ms
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION / 1000)


def take_command():

    print("Listening...")

    audio = sd.rec(
        int(SAMPLE_RATE * 3),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    audio = audio.flatten()

    # ----- Voice Activity Detection -----
    speech_detected = False

    for i in range(0, len(audio), FRAME_SIZE):
        frame = audio[i:i + FRAME_SIZE]

        if len(frame) < FRAME_SIZE:
            break

        if vad.is_speech(frame.tobytes(), SAMPLE_RATE):
            speech_detected = True
            break

    if not speech_detected:
        return None

    # ----- Transcription -----
    audio_float = audio.astype("float32") / 32768.0

    segments, _ = model.transcribe(audio_float, language="en")

    text = ""
    for seg in segments:
        text += seg.text

    text = text.strip().lower()

    # Ignore very short hallucinations
    if len(text) < 3:
        return None

    return text