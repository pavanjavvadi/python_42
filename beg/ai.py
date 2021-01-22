import speech_recognition as sr
import webbrowser,time,playsound,os,random
from gtts import gTTS
from datetime import datetime


sr.Microphone(device_index=1)
rec = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            rainy_speak(ask)
        audio = rec.listen(source)
        voice_data=''
        try:
            voice_data = rec.recognize_google(audio)
        except sr.RequestError:
            rainy_speak("sorry, my service is down")
        except sr.UnknownValueError:
            rainy_speak("Sorry i didn't get that.Please, try again.")    
        return voice_data        

def rainy_speak(audio_file):
    tts = gTTS(text=audio_file,lang='en')
    rand = random.randint(1,100000)
    audio_file_name = 'audio-'+str(rand)+'.mp3'
    tts.save(audio_file_name)
    print(audio_file)
    playsound.playsound(audio_file_name)
    os.remove(audio_file_name)


def respond(voice_data):
    if 'what is your name' in voice_data:
        rainy_speak("My Name is Rainy")
    if 'what time it is' in voice_data:
        current_time = datetime.now().strftime("%H:%M:%S")
        rainy_speak(current_time)    
    if 'search' in voice_data:
        search = record_audio('what do you want to search?') 

        webbrowser.open('https://www.google.com/search?q='+ search)  
        rainy_speak("Here is what i found")      
    if 'exit' in voice_data:
        rainy_speak("Thanks for using rainy AI")
        exit()
rainy_speak("Hi, i am rainy.How may i help you?")
time.sleep(1)
while True:
    voice_data = record_audio()
    respond(voice_data)




"""
pip install gTTS,
pip install playsound,
pip install speechrecoginition
"""