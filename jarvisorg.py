import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
from wikipedia.wikipedia import languages
import pyjokes
from googletrans import Translator
import requests
import pyautogui
import time



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#text to speech




def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2,phrase_time_limit=5)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please....")
        return"none"
    return query

def wish():
    hour = int (datetime.datetime.now().hour)
    tt = time.strftime("%I : %M %p")
    if hour>=0 and hour<=12:
        speak(f"Good morning, its{tt}")
    elif hour>12 and hour<18:
        speak(f"good afternoon,its {tt}")
    else:
        speak(f"Good Evening, its {tt}")
        
    
    speak("Jarvis on your service sir . Please tell me how can I help you sir")
    
def sendEmail(address,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com','your name')
    server.sendmail('RecieverAddress@gmail.com',address,content)
    server.close()




if __name__ == "__main__":
    wish()
    while True:
    

        query = takecommand().lower()

        #building task

        if "open notepad" in query:
            speak("opening notepad sir")
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        if "close notepad" in query:
            speak("closing notepad sir")
            os.system("taskkill /f /im notepad.exe")

        if "open chrome" in query:
            speak("opening chrome sir")
            npath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)

        if "close chrome" in query:
            speak("closing chrome sir")
            os.system("taskkill /f /im chrome.exe")


        if "open photoshop" in query:
            speak("opening photoshop sir")
            npath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\photoshop.exe"
            os.startfile(npath)

        if "close photoshop" in query:
            speak("closing photoshop sir")
            os.system("taskkill /f /im photoshop.exe")


        if "open visual code" in query:
            speak("opening visual studio code")
            npath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(npath)

        if "close visual code" in query:
            speak("closing visual code sir")
            os.system("taskkill /f /im code.exe")


        if "open word" in query:
            speak("opening MS word")
            npath = "C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE"    
            os.startfile(npath)

        if "close word" in query:
            speak("closing MS word sir")
            os.system("taskkill /f /im WINWORD.exe")


        if "open command prompt" in query:
            speak("opening command prompt sir")
            npath = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(npath)

        if "close command prompt" in query:
            speak("closing command prompt sir")
            os.system("taskkill /f /im cmd.exe")


        
        if "play music" in query:
            music_dir = "C:\\Users\\ASUS\\Music"
            songs = os.listdir(music_dir) 
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir,song))


        if "tell ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your ip address is {ip}")


        if "wikipedia" in query:
            speak("searching wikipedia......")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(result)
            print(result)

                

        if "open youtube" in query:
            speak("what you what to play")
            cmd = takecommand().lower()
            kit.playonyt(f"{cmd}")

        if "send email" in query:
            try:
                speak("Enter email address to whom you want to send email")
                address = input("Enter email address to whom you want to send email")
                speak("What message should  I send")
                content = takecommand().lower()
                sendEmail(address,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir  I am unable to send message")


        if "no thanks" in query:
            speak("Thankyou sir , Have a great day")
            sys.exit()

        if "tell joke" in query:
            joke = pyjokes.get_joke(languages = 'en')
            speak(joke)

        if "translate language" in query:
           
            speak("please enter the text you want to translate")
            mes = str(input("Enter your message")) 
            translater = Translator()
            text = translater.translate(mes,src = 'en',dest = "ja")
            print(text)

        if "shut down system" in query:
            os.system("shutdown /s /t 5")

        if "restart system" in query:
            os.system("shutdown /r /t 5")

        if "sleep" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        if "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        
        if "secret message" in query:
            speak("There is a secret message for you Rashi mam")
            kit.playonyt(f"tujhme rab dikhta hai")

        


        speak("sir do you have any more work for me")