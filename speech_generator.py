from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
import pygame

# Initialize pygame mixer
pygame.mixer.init()


# Function to play gTTS audio with speed control
def text_to_speech(text, lang="en", speed=1.25):
    mp3_fp = BytesIO()
    tts = gTTS(text=text, lang=lang)
    tts.write_to_fp(mp3_fp)

    # Load the audio into pydub
    mp3_fp.seek(0)
    audio = AudioSegment.from_file(mp3_fp, format="mp3")

    # Adjust speed using pydub
    faster_audio = audio.speedup(playback_speed=speed)

    # Export the modified audio to a BytesIO object
    faster_mp3_fp = BytesIO()
    faster_audio.export(faster_mp3_fp, format="mp3")

    # Play the modified audio using pygame
    faster_mp3_fp.seek(0)
    pygame.mixer.music.load(faster_mp3_fp, "mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue


if __name__ == "__main__":
    text = "Hi, this is a test to show that text to speech is working."
    text_to_speech(text)
