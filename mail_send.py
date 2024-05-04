import pyttsx3
import speech_recognition as sr
import webbrowser
import smtplib
import datetime

chrome = webbrowser.Chrome(r"c:\Program Files (x86)\Google\Chrome\Application\new_chrome.exe")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greet_user():
    hour = int(datetime.datetime.now().hour)
    if(hour >=0 and hour <12):
        speak("good morning")
    elif(hour >=12 and hour <18):
        speak("good afternoon")
    else:
        speak("good evening")
    
    speak("I am Alexa. welcome to Alexa's world")
    speak("Ma'am, how may i help you?")
    

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
        
    try:
        print("recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        speak("say that again please.....")
        return "none"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mondaljoyitree18@gmail.com', 'wjmf dldh qdnw wjwv')
    server.sendmail('mondaljoyitree18@gmail.com', to, content)
    server.close()

def mailsend():
    greet_user()
    query=takecommand().lower()
    if 'email to joyitree' in query or 'mail to joyitree':
            try:
                speak("what should i say?")
                content=takecommand().lower()
                to="joyitree2022@gmail.com"
                sendEmail(to,content)
                speak('email has been sent')
            
            except Exception as e:
                print(e)
                speak("i am sorry ma'am, I can't send the mail.")
        

if __name__ =="__main__":
    mailsend() 
    