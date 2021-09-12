import webbrowser
import pyttsx3
import wikipedia
import os
import random
import datetime
import smtplib
import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)
# print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening to user.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=5)
    try:
        print("Recognizing please wait...")
        query = r.recognize_google(audio,language="en-in")
        print("User Said",query)
    except Exception as e:
        print("Say that again..!")
        return "none"
    return query

def wishme():
    hour=int(datetime.datetime.now().hour)
    if 0<=hour<12:
        speak("Good Morning....!")
    elif 12<=hour<18:
        speak("Good Afternoon...!")
    else:
        speak("Good Evening....!")
    speak("I am jarvis sir,Please tell me how may I help you")
if __name__=='__main__':
    wishme()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia..wait ")
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open("www.goole.com")
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")
        elif 'open music' in query:
            songs=os.listdir(r'C:\Users\RAJ\Music\songs')
            num=random.randint(0,len(songs)-1)
            os.startfile(os.path.join(r'C:\Users\RAJ\Music\songs',songs[num]))
        elif 'what is the time 'in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtime}")
        elif "open vs code" in query:
            os.startfile(r"C:\Users\RAJ\AppData\Local\Programs\Microsoft VS Code\Code.exe")
        elif "send email" in query:
            speak("from which email id i can send")
            sender=takecommand()
            speak("Tell me password of this account")
            password=takecommand()
            speak("to which email id")
            to=takecommand()
            speak("what should i write please tell me")
            message=takecommand()
            server=smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(sender,password)
            server.sendmail(sender,to,message)
            speak("Email has been sent successfully")
            server.quit()
        else:
            speak("sorry sir, cant process this command i am still in upgrading mode...")



