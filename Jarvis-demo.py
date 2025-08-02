import os
import pyttsx3
import speech_recognition as sr
import webbrowser




from speech_recognition import Microphone


def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source,0,4)
    try:
         print("Understanding...")
         query=r.recognize_google(audio,language='en-in')
         print(f"You said {query}")
    except Exception as e:
        print('Say that again')
        return"none"
    return query
if __name__=='__main__':
   while True:
      query=takeCommand().lower()
      if "wake up" in query:
         from Greet_me import greet_user
         greet_user()

         while True:
             query=takeCommand().lower()
             if "go to sleep" in query:
                 speak('Ok Sir,You can call anytime')
                 break
             elif "hello" in query:
                 speak('Hello Sir!How are you?')
             elif "i m fine" in query:
                 speak('Thats great Sir')
             elif "how are you" in query:
                 speak('Perfect sir')
             elif "open youtube" in query:
                 speak('Opening youtube')
                 webbrowser.open('https://www.youtube.com')
             elif "open google" in query:
                 speak("Opening Google")
                 webbrowser.open("https://www.google.com")
             elif "open downloads" in query:
                 speak('opening download folder')
                 os.startfile(r"C://Users//User//Downloads")
             else:
                 speak("I do not understand")






























