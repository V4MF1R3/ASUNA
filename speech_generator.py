from gtts import gTTS
from io import BytesIO
import pygame

# pygame mixer for playing sound
pygame.mixer.init()


# Function to play gTTS audio directly
def text_to_speech(text, lang="en"):

    mp3_fp = BytesIO()

    tts = gTTS(text=text, lang=lang)
    tts.write_to_fp(mp3_fp)

    mp3_fp.seek(0)

    pygame.mixer.music.load(mp3_fp, "mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue


if __name__ == "__main__":

    text = "Hi, this is a test to show that text to speech is working."
    text_to_speech(text)
