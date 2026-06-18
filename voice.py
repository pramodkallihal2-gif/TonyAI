import asyncio
import edge_tts
import pygame
import uuid
import os
import time

VOICE = "en-US-GuyNeural"

pygame.mixer.init()

async def generate_voice(text, filename):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )
    await communicate.save(filename)

def speak(text):

    print(f"Assistant: {text}")

    filename = f"voice_{uuid.uuid4().hex}.mp3"

    asyncio.run(generate_voice(text, filename))

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()

    try:
        os.remove(filename)
    except:
        pass