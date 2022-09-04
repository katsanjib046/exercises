import speech_recognition
import pyttsx3

engine = pyttsx3.init()
# Obtain audio from the microphone
recognizer=speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something:")
    audio=recognizer.listen(source)
    # Recognize speech using Google Speech Recognition
    words=recognizer.recognize_google(audio)
    print(words)
# Respond to speech
if "hello it's me" in words :
    engine.say("Hello to you too, Rojina!")
    engine.runAndWait()
elif "hello" in words:
    engine.say("Hello to you too, Sanjib!")
    engine.runAndWait()
else: 
    engine.say("Sorry, I couldn't understand you.")
    engine.runAndWait()