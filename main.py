import time
import webbrowser
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer

def say(text):
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    mixer.init()
    mixer.music.load("speech.mp3")
    mixer.music.play()

    # Wait for speech playback to finish
    while mixer.music.get_busy():
        time.sleep(0.1)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = r.listen(source)
            print("Recognizing...")
            user_query = r.recognize_google(audio, language="en-in")
            print(f"User said: {user_query}")
            return user_query
        except Exception as e:
            return "Please speak clearly."

say("Hello, I am not a robot. I am your personal assistant.")

while True:
    text = takeCommand()
    # say(text)

    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.org"], ["google", "https://www.google.com"]]

    for site in sites:
        if f"open {site[0]}".lower() in text.lower():
            say(f"Opening {site[0]}, sir....")
            webbrowser.open(site[1])
