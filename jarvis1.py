import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
from translate import Translator
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
from wikipedia.wikipedia import languages
import pyjokes
import googletrans



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

    if hour>=0 and hour<=12:
        speak("Good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("Good Evening")
    speak(" Alice on your service sir . Please tell me how can I help you sir")
def sendEmail(address,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kipmatscse@gmail.com','ashtavakra')
    server.sendmail('amanojha00345@gmail.com',address,content)
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

        if "open chrome" in query:
            speak("opening chrome sir")
            npath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(npath)

        if "open photoshop" in query:
            speak("opening photoshop sir")
            npath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\photoshop.exe"
            os.startfile(npath)

        if "open visual code" in query:
            speak("opening visual studio code")
            npath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(npath)

        if "open word" in query:
            speak("opening MS word")
            npath = "C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE"    
            os.startfile(npath)

        if "open command prompt" in query:
            speak("opening command prompt sir")
            npath = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(npath)

        
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


        if "open wikipedia" in query:
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
            speak("Tell me from which language you what to translate")
            initial = takecommand().lower()
            speak("Tell me to which language you want to translate")
            translated = takecommand().lower()
            speak("Tell me the message you want to translate")
            mes = takecommand().lower()
            translator = Translator()
            text_to_translate = translator.translate("hello how are you???",dest='hi')
            text = text_to_translate.text
            speak(text)
 




        speak("sir do you have any more work for me")