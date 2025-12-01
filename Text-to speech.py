import pyttsx3
import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
speaker = pyttsx3.init()
voices = speaker.getProperty("voices")
try:
    speaker.setProperty("voice", voices[1].id)
except Exception:
    pass
speaker.setProperty("rate", 150)
speaker.setProperty("volume", 1.0)
def speak(text):
    print("Assistant:", text)
    speaker.say(text)
    speaker.runAndWait()
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio).lower()
        except:
            print("Please say again.")
            return ""
speak("Hello! I'm your assistant.")
try:
    while True:
        command = listen()
        if "hello" in command:
            print("Hello! How can I help?")
        elif "time" in command:
            print("The time is " + datetime.now().strftime("%I:%M %p"))
        elif "your name" in command:
            print("My name is Mini Assistant.")
        elif "youtube" in command:
            print("Opening YouTube.")
            webbrowser.open("https://youtube.com")
        elif "stop" in command or "exit" in command:
            print("Goodbye!")
            break
        else :
            print("I don't know that command yet.")
finally:
    time.sleep(0.15)
    try:
        speaker.stop()
    except:
        pass
        
