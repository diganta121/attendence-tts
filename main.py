# take attendence easily
from gtts import gTTS
from time import sleep
import os
import pyglet.media
import csv

def speak(text):
    # text to audio

    tts = gTTS(text=text, tld="in", lang="en", slow=False, lang_check=False,timeout=10000)

    filename = "temp.mp3"
    tts.save(filename)

    audio = pyglet.media.load(filename, streaming=False)
    audio.play()

    sleep(audio.duration)
    os.remove(filename)

def read_csv(filename):
    data = []

    with open(filename,'r') as f:
        rdr = csv.reader(f)
        for i in rdr:
            data.append(i)
    return data

def bin_search(data,c,x):
    '''binary search for x in data in col c
    consider data as 2d list [[a,1],[b,2]]'''
    ul = len(data)
    ll = 0
    mid = ul//2
    while ul > ll:
        mid = (ul - ll)//2 +ll #??
        if data[mid][c] > x:
            ll = mid +1
        elif data[mid][c] < x:
            ul = mid -1
        elif data[mid][c] == x:
            return mid
    return -1

def mark_absent(data,reg_id):
    #data[1]
    #get id using bin_search and update data
    pass




filename = input("file name: ").strip()

