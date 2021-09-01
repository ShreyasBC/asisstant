
import os
import time

import cv2
import pyttsx3
import requests
import speech_recognition as sr
from GoogleNews import GoogleNews

pyttsx3.speak("hello user welcome")
pyttsx3.speak("this is friday how may i help you")
try:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        data = r.recognize_google(audio)
        time.sleep(3)
        print("done")
        print("you said:" + r.recognize_google(audio))
        try:
            if ("Notepad" in data):
                os.system(" start notepad")
                time.sleep(3)
            if ("PowerPoint" in data):
                os.system(" start powerpnt")
                time.sleep(3)
            if ("Chrome" in data):
                os.system(" start chrome")
                time.sleep(3)
            if ("ms edge" in data):
                os.system(" start msedge")
                time.sleep(3)
            if ("calculator" in data):
                os.system(" start calc")
                time.sleep(3)
            if ("update" in data):
                pyttsx3.speak("which region news do you wanna know about")
                r1 = sr.Recognizer()
                with sr.Microphone() as source1:
                    audio1 = r1.listen(source1)
                    data1 = r1.recognize_google(audio1)
                    print("done")
                    print("you said:" + r1.recognize_google(audio1))
                    g_news = GoogleNews()
                    g_news = GoogleNews(period="1d")
                    g_news.search(data1)
                    result = g_news.result()
                    for i in result:
                        print("-" * 50)
                        print("Tittle -- ", i["title"])
                        my_text = i['title']
                        pyttsx3.speak(my_text)
                        print("date/time--", i["date"])
                        print("Description --", i["desc"])
                        print("Link -- ", i["link"])
            if ("camera" in data):
                vid = cv2.VideoCapture(0)

                while (1):
                    retr, frame = vid.read()
                    cv2.imshow("camera", frame)

                    if cv2.waitKey(1) & 0xff == ord("q"):
                        break

                vid.release()
                cv2.destroyAllWindows()

            if ("weather" in data):
                api_key = "0a357a04b57e705994649a7a36b25bfc"

                base_url = "http://api.openweathermap.org/data/2.5/weather?"

                pyttsx3.speak("which place weather do you wanna know about")
                r2 = sr.Recognizer()
                with sr.Microphone() as source2:
                    audio2 = r2.listen(source2)
                    data2 = r2.recognize_google(audio2)
                    time.sleep(3)
                    print("done")
                    print("you said:" + r2.recognize_google(audio2))
                    city_name = data2

                    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

                    response = requests.get(complete_url)

                    x = response.json()

                    if x["cod"] != "404":
                        y = x["main"]

                        current_tempreture = y["temp"]

                        current_pressure = y["pressure"]

                        current_humidty = y["humidity"]

                        z = x["weather"]

                        weather_description = z[0]["description"]

                        print(f"Temperature(in kelvin )= {current_tempreture}")
                        print(f"humidity(in percentage) = {current_humidty}")
                        print(f"atmosphearic pressure(in hpa unit) = {current_pressure}")
                        print(f"description = {weather_description}")
                        pyttsx3.speak("Temperature(in kelvin )=")
                        pyttsx3.speak(current_tempreture)
                        pyttsx3.speak("humidity(in per) =")
                        pyttsx3.speak(current_humidty)
                        pyttsx3.speak("atmosphearic pressure(in hpa unit) = ")
                        pyttsx3.speak(current_pressure)
                        pyttsx3.speak("description = ")
                        pyttsx3.speak(weather_description)

            if ("exit" in data):
                os.system(" exiting")

        except:
            print("couldn't hear you try again")
            pyttsx3.speak("couldn't hear you try again")
except:
    print("couldn't hear you try again")
    pyttsx3.speak("couldn't hear you try again")
