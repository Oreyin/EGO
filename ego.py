#!/usr/bin/env python3
 
import speech_recognition as sr
from time import ctime
import time
import os
import webbrowser
from gtts import gTTS
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data

def ego(data):
   if "how are you" in data:
	speak("I am fine")

   if "ego" in data:
	speak("Yes Sir?")
 
   if "what time is it" in data:
        speak(ctime())

   if "ego open firefox" in data or "ego open fire fox" in data or "ego open Firefox" in data:
	speak("Opening Firefox")
	webbrowser.open("https://www.google.com/", new=0, autoraise=True)

   if "ego how smart are you" in data:
	speak("Not very")

   if "thanks" in data or "thanks ego" in data:
	speak("You're welcome sir")

   if "where is" in data:
	data = data.split(" ")
	location = data[2]
	speak("Hold on, I will show you where " + location + " is.")
	webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;", new=0, autoraise=True)
 
# initialization
time.sleep(2)
awake = 1
speak("Hello sir, what can I do for you?")
while 1:
    data = recordAudio()

    if "ego sleep" in data or "ego go to sleep" in data or "go to sleep ego" in data:
	awake = 0

    if "ego wake up" in data or "wake up ego" in data:
	awake = 1

    if (awake == 1):
	ego(data)

