import instaloader
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import PyPDF2
import operator
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import speedtest
import numpy as np
import pyautogui as p

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=6, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak(" say that again please...")
        return"none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("I am IPA sir , please tell me how can i help you")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('adarsh0610@gmail.com', 'psswrd')
    server.sendmail('adarsh0610@gmail.com', to, content)
    server.close()

#for news update
def news():
    main_url= 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=ddb381fe0a894c4f8090582b16c94790'
    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        # print(f"today's {day[i]} news is: ",head[i])
        speak(f"today's {day[i]} news is: {head[i]}")

def pdf_reader():
    book = open('book.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"total number of pages in this book{pages}")
    speak("sir please enter the page number which you want me to read")
    pg = int(input("please enter the page number: "))
    page =pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

def start():
    p.press('esc')
    speak("verification is successful")
    speak("welcome back adarsh sir")
    wish()
    while True:
    #if 1:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "E:\\Songs"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            #print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+918017848263", "hlo amar ",19,34)

        elif "play songs on youtube" in query:
            kit.playonyt("see you again")

        elif "hello" in query:
            speak("hello sir , how can i help you.")

        elif "how are you" in query:
            speak("i am fine sir , what about you.")
        
        elif "i am also good" in query or "i am good" in query:
            speak("good to hear it sir, how may i help you.")

        elif "what are you doing" in query:
            speak("waiting for your command , sir")

        elif "thank you" in query:
            speak("it's my pleasure sir")

        #elif "email to amar" in query:
        #    try:
        #        speak("what should i say?")
        #        content = takecommand().lower()
        #        to = "adarsh06100411@gmail.com"
        #        sendEmail(to,content)
        #        speak("Email has been sent to amar")

        #    except Exception as e:
        #       print(e)
        #       speak("sorry sir, i am not able to send this mail")

        elif "you can sleep" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

#to close any application
        elif "close notepad" in query:
            speak("ok sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

#to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = "E:\\Songs"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, song[1]))

#to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

#switch the tab
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me the latest news" in query:
            speak("please wait sir, fetching the latest news")
            news()


        elif "email to amar" in query:
            speak("sir, what should i say")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'adarsh0610@gmail.com'
                password = 'PASSWORD'
                send_to_email = 'adarsh06100411@gmail.com'
                speak("okay sir, what is the subject for this email")
                query = takecommand().lower()
                subject = query
                speak("and sir, what is the message for this email")
                query2 = takecommand().lower()
                message = query2
                speak("sir please enter the correct path of the file into the shell")
                file_location = input("please enter the path here")

                speak("please wait, i am sending email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                #setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                # attach the attachment to the MIMEMultipart object
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent")

            else:
                email = 'adarsh0610@gmail.com'
                password = 'PASSWORD'
                send_to_email = 'adarsh06100411@gmail.com'
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_email, message)
                server.quit()
                speak("email has been sent")

#to find my location using IP address

        elif "what is my current location" in query or "what is our current location" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                #city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['country']
                speak(f"i think we are in {country}")
            except Exception as e:
                speak("sorry sir, Due to network issue i am not able to find where we are.")
                pass

# to check a instagram profile

        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir, please enter the user name correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir,here is the profile of the user {name}")
            time.sleep(5)
            speak("sir, would you like to download the profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile pic is saved in our main folder. now i am ready for my next command")
            else:
                pass

# to take a screenshot

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("sir, please hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, screenshot is saved in our main folder. now i am ready for my next command")

        #speak("sir, do you have any other work")

# to read a pdf file

        elif "read pdf" in query:
            pdf_reader()

# to hide files

        elif "hide all files" in query or "hide this folder" in query:
            speak("sir, are you sure that you want me to hide this folder")
            condition = takecommand().lower()
            if "yes" in condition:
                os.system("attrib +h /s /d")
                speak("sir, all the files in this folder are now hidden.")

            elif "leave it" in condition or "leave for now" in condition:
                speak("ok sir")

        elif "visible for everyone" in query or "make it visible" in query:
            speak("sir, are you sure that you want to make this folder visible for everyone.")
            condition = takecommand().lower()

            if "yes" in condition:
                os.system("attrib -h /s /d")
                speak("sir, all the files in this folder are now visible to everyone.")

            elif "leave it" in condition or "leave for now" in condition:
                speak("ok sir")


############## to do basic mathematical calculation

        elif "do some calculations" in query or "can you calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say what you want to calculate, example: 3 plus 3")
                print("listening.....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add, #plus
                    '-' : operator.sub, #minus
                    'x' : operator.mul, #multiplied by
                    'divided' : operator.__truediv__, #divided
                }[op]
            def eval_binary_expr(op1, oper, op2): # 5 plus 2
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1,op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))

# weather forecast

        elif "temperature" in query:
            search = "temperature in bangalore"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

# to search anything 

        elif "activate how to do mode" in query:
            speak("How to do mode is activated")
            while True:
                speak("please tell me what you want to know")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir, how to do mode is deactivated")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1   
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")

# battery percentage

        elif "how much power left" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            if percentage>=75:
                speak("we have enough power to continue our work")
            elif percentage>=40 and percentage<75:
                speak("we should charge our system")
            elif percentage>=15 and percentage<40:
                speak("we don't have enough power please connect to charging")
            elif percentage<15:
                speak("we have very low power, please connect to charging the system will shutdown very soon")


# to check internet speed

        elif "internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

        #try:
         #   os.system('cmd /k "speedtest"')
        #except:
         #   speak("sorry sir, I'm unable to check the internet speed")

#to control volume

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute")

##########
if __name__ == "__main__":


    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 2 #no of persons you want to recognize

    names = ['','adarsh']

    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cam.set(3, 640) #set video framewidth
    cam.set(4, 480) #set video frameheight

        #define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)


    while True:
        ret, img =cam.read()
        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
            )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)
            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])

            #check if accuracy is less than 100 ==> "0" is perfect match

            if (accuracy < 100):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                start()

            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                speak("user authentication is failed")
                break

            cv2.putText(img,str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)

        #cv2.imshow('camera',img)

        k = cv2.waitKey(10) & 0xff #press ESC for exiting video
        if k == 27:
            break

    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()







