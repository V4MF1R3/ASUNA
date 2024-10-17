import datetime
import speech_recognition as sr
from speech_generator import text_to_speech
from automation import Inflow
from news import get_news

r = sr.Recognizer()

current_time = datetime.datetime.now().time()
print(current_time)

response = ""


def listen():
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        global response
        response = r.recognize_google(audio)
        print(response)


if current_time >= datetime.time(5, 0) and current_time < datetime.time(12, 0):
    text_to_speech("Good morning, Mr. Pant! What can I do for you.")
elif current_time >= datetime.time(12, 0) and current_time < datetime.time(17, 0):
    text_to_speech("Good afternoon, Mr Pant! What can I do for you.")
else:
    text_to_speech("Good evening, Mr Pant! What can I do for you.")

listen()

if "information" in response:
    text_to_speech("You need information to which topic?")
    listen()
    text_to_speech(f"Searching {response} in wikipedia")
    assist = Inflow()
    text_to_speech(assist.get_info(response))

elif "play" in response:
    index = response.find("play")
    if index != -1:
        query = response[index + len("play") :].strip()
    text_to_speech(f"playing {query} in youtube")
    assist = Inflow()
    assist.player(query)

elif "news" or "headlines" or "headline" in response:
    text_to_speech("here are the latest headlines.")
    text_to_speech(get_news())
