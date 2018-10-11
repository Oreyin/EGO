#!/usr/bin/env python3
 
import speech_recognition as sr
from time import ctime
import time
import os
import subprocess
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
   if "ego load steam" in data or "load steam" in data or "open steam" in data or "ego open steam" in data:
	subprocess.call("steam")

   if "ego" in data:
	speak("Yes Sir?")
 
   if "what time is it" in data:
        speak(ctime())

   if "ego open firefox" in data or "ego open fire fox" in data or "ego open Firefox" in data:
	speak("Opening Firefox")
	webbrowser.open("https://www.google.com/", new=0, autoraise=True)

   if "ego how smart are you" in data:
	speak("I have the intelligence of a young meat person.")

   if "thanks" in data or "thanks ego" in data:
	speak("You're welcome sir")

   if "search" in data:
	data = data.split(" ")
	
	for i in enumerate(data, start = 1te):
	    search += data[i]

	speak("Searching for " + search)
	webbrowser.open("https://www.google.nl/maps/place/" + search + "/&amp;", new=0, autoraise=True)

   if "find me" in data or "look up" in data or "ego search" in data:
	data = data.split(" ")
	
	for i in enumerate(data, start = 2):
	    search += data[i]

	speak("Searching for " + search)
	webbrowser.open("https://www.google.nl/maps/place/" + search + "/&amp;", new=0, autoraise=True)
	
   if "ego find me" or "ego look up" in data:
	data = data.split(" ")

	for i in enumerate(data, start = 3):
	    search += data[i]

	speak("Searching for " + search)
	webbrowser.open("https://www.google.nl/maps/place/" + search + "/&amp;", new=0, autoraise=True)

   if "open notepad" in data or "ego open notepad" in data:
	if os.name == "Windows":
	    subprocess.call("notepad")
	else if os.name == "Ubuntu"
	    subprocess.call("gedit")
	    
   if "where is" in data:
	data = data.split(" ")

	for i in enumerate(data, start = 3):
	    location += data[i]

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

