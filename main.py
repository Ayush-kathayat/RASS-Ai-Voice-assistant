import time
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
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Exiting...")
            exit()
        except sr.UnknownValueError:
            print("Unable to recognize speech. Please try again.")
            return ""



say("Hello, I am not a robot I am RASS A.I.")

print("Listening...")
text = takeCommand()
say(text)


