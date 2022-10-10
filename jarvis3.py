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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import time
from email import encoders 





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#text to speech
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=da91786b005845c4b73f0ddf7fe1b466'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","Eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")



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
            speak("Sir what should I send")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'kipmatscse@gmail.com'
                password = 'ashtavakra'
                speak("Enter the person's email to which you want to send mail")
                send_to_email = input("Enter the email to which you want to send your mail") 
                speak("Sir what is the subject for this message")
                query = takecommand().lower()
                subject = query
                speak("Sir What message should i send")
                query2 = takecommand().lower()
                message = query2
                speak("Please enter the file path which you want to send")
                file_location = input("Please Enter the path here")
                
                speak("Please wait sir I am sending the mail")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message,'plain'))

                filename =  os.path.basename(file_location)
                attachment = open(file_location,"rb")
                part = MIMEBase('application','octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',"attachment; filename = %s" % filename)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(email,password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("Email has been sent")

            if "text mail" in query:
                email = 'kipmatscse@gmail.com'
                password = 'ashtavakra'
                speak("Enter the email address to which you want to send mail")
                send_to_email = str(input("Enter the email address to which you want to send mail"))
                message = query

                server = smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.login('kipmatscse@gmail.com','ashtavakra')
                server.sendmail(email,send_to_email,message)
                server.close()




            


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

        if "news" in query:
            speak("Please wait sir, fetching the latest news")
            news()



        speak("sir do you have any more work for me")