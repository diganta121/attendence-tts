import pyglet.media
from gtts import gTTS
import os
import time

def speak(text):
    # text to audio

    tts = gTTS(text=text, tld="in", lang="en", slow=False, lang_check=False,timeout=10000)

    filename = "temp.mp3"
    tts.save(filename)

    audio = pyglet.media.load(filename, streaming=False)
    audio.play()

    time.sleep(audio.duration)
    os.remove(filename)

if __name__ == '__main__':
    speak('hello speech test')
