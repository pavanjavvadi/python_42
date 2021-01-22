import speech_recognition as sr 
import webbrowser

sr.Microphone(device_index=1)
rec = sr.Recognizer()
rec.energy_threshold=5000

with sr.Microphone() as source:
    print("Speak!")
    audio = rec.listen(source)

    try:
        text = rec.recognize_google(audio)
        print("You said: "+ text)
        webbrowser.open('https://www.google.com/search?q='+ text)

    except:
        print("can't recognize")