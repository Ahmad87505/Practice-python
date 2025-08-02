import datetime
import pyttsx3
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def greet_user():
    present_time = datetime.datetime.now()
    current_time = present_time.time()
    current_hour = current_time.hour
    current_date = present_time.date()
    current_day = present_time.strftime("%A")

    if 5 <= current_hour < 12:
        speak("Good Morning")

    elif 12 <= current_hour < 17:
        speak("Good Noon")
    elif 17 <= current_hour < 20:
        speak("Good Evening")
    else:
        speak("Good Night")
if __name__=='__main__':
    greet_user()