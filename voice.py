import asyncio
import edge_tts
import pygame
import pyttsx3
import uuid
import os
import time

VOICE = "en-GB-SoniaNeural"

pygame.mixer.init()

engine = pyttsx3.init()
engine.setProperty("rate", 180)


async def generate_voice(text, filename):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )
    await communicate.save(filename)


def offline_speak(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):

    print(f"Assistant: {text}")

    filename = f"voice_{uuid.uuid4().hex}.mp3"

    try:

        asyncio.run(
            generate_voice(text, filename)
        )

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()

        try:
            os.remove(filename)
        except:
            pass

    except Exception as e:

        print("Edge-TTS unavailable. Switching to offline voice.")
        offline_speak(text)