#This logic is written to perform openig of any application using voice assistant

import speech_recognition as sr
from gtts import gTTS
import os,time,random,playsound



sr.Microphone()
rec = sr.Recognizer()
rec.energy_threshold = 3000

def respond(text):
    tts = gTTS(text=text,lang='en')
    voice_data = 'audio.mp3'
    tts.save(voice_data)
    print(text)
    playsound.playsound(voice_data)
    os.remove(voice_data)

def record():
    with sr.Microphone() as source:
        voice_data = rec.listen(source)
        try:
            audio = rec.recognize_google(voice_data)
            respond(audio)
        except:
            respond("error")    
record()
