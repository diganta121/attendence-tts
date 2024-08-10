# take attendence easily
from gtts import gTTS
from time import sleep
import os
import pyglet.media


def speak(text):
    # text to audio

    tts = gTTS(text=text, tld="in", lang="en", slow=False, lang_check=False,timeout=10000)

    filename = "temp.mp3"
    tts.save(filename)

    audio = pyglet.media.load(filename, streaming=False)
    audio.play()

    sleep(audio.duration)
    os.remove(filename)
