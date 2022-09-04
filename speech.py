import pyttsx3

engine = pyttsx3.init()
this = input("What's this?: ")
engine.say(this)
engine.runAndWait()