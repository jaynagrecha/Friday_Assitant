from sys import path
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import io
import smtplib
from PyDictionary import PyDictionary
import pandas as pd
from googlesearch import search
from fpdf import FPDF
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate



dictionary=PyDictionary()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
newVoiceRate = 210
engine.setProperty('rate',newVoiceRate)

def WishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >=0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("It's Friday here. How may I help you sir?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2.0
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        # print(e)
        speak("Please Repeat, Sir!")
        print("Please Repeat Sir!")
        return "None"       
    return query

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jaynagrecha98@gmail.com','oztdccomkairehwt')
    server.sendmail(to, to, content)
    server.close()

# def convert_to_pdf():
#     pdf = FPDF()   
#     pdf.add_page()
#     pdf.set_font("Arial", size = 15)
#     f = open("file1.txt", "r")
#     for x in f:
#         pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
#     pdf.output("file1.pdf")


# def email(to,content):
    
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('jaynagrecha98@gmail.com','oztdccomkairehwt')
#     server.sendmail('jaynagrecha33@gmail.com',to, content)
#     server.close()
    


if __name__ == "__main__":
    WishMe()
    while True:
    # if 1:
        query = TakeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching in Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia,")
            speak(results)
        elif 'open youtube' in query:
            speak("Opening YouTube.")
            url = 'https://youtube.com'
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            # webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening Google.")
            url = 'https://google.com'
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            # webbrowser.open("google.com")
        elif 'open my personal website' in query:
            speak("Opening Lucifer Website.")
            url = 'http://luc1f3r.epizy.com'
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            # webbrowser.open("luc1f3r.epizy.com")
        elif 'play music' in query:
            speak("Playing Songs From Your Folder!")
            music_dir = 'W:\\Python Work\\Python Projects\\Friday\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The Current Ti  me is {strTime}, sir.")
            speak(f"The Current Time is {strTime}, sir.")
        elif 'open sublime' in query:
            speak("Opening Sublime Text Editor!")
            sublime_path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(sublime_path)
        elif 'open putty' in query:
            speak("Opening Putty To Connect To A Sever!")
            putty_path = "C:\\Program Files\\PuTTY\\putty.exe"
            os.startfile(putty_path)
        elif 'email to me' in query:
            try:
                speak("What should I send sir?")
                content = TakeCommand()
                to = "jaynagrecha33@gmail.com"
                sendEmail(to, content)
                print("Email Has Been Sent Sir.")
                speak("Email Has Been Sent Sir.")
            except Exception as e:
                print(e)
                speak("Sorry Sir there was a problem in sending the email")
        elif 'record' in query:
            query = query.replace("record", "")
            speak("Recording Started, Sir!")
            f = open("file1.txt", "a", encoding="utf-8")
            data = transliterate(query, sanscript.IAST, sanscript.GUJARATI)
            # query = query.replace("record", "")
            f.write(data)
            # convert_to_pdf()
            f.close()
            # convert_to_pdf()
        elif 'show contacts' in query:
            df = pd.read_csv("contacts.csv", usecols=['Name','Email'])
            print(df)
            # contacts = df.iloc[0].values.tolist()
            contacts = df.values.tolist()
            # contactnames = df['Name'].values.tolist()
            # for i in range(len(contactnames)):
            #     print(contactnames[i])
            contact1 = df['Name'].iloc[0]
            contact2 = df['Name'].iloc[1]
            contact3 = df['Name'].iloc[2]
            contact4 = df['Name'].iloc[3]
            contact5 = df['Name'].iloc[4]
            contact6 = df['Name'].iloc[5]
            contact7 = df['Name'].iloc[6]
            contact8 = df['Name'].iloc[7]
            contact9 = df['Name'].iloc[8]
            contact10 = df['Name'].iloc[9]
            #contact11 = df['Name'].iloc[10]

            # contactmails = df['Email'].values.tolist()
            # for i in range(len(contactmails)):
            #     print(contactmails[i])
            con1 = df['Email'].iloc[0]
            con2 = df['Email'].iloc[1]
            con3 = df['Email'].iloc[2]
            con4 = df['Email'].iloc[3]
            con5 = df['Email'].iloc[4]
            con6 = df['Email'].iloc[5]
            con7 = df['Email'].iloc[6]
            con8 = df['Email'].iloc[7]
            con9 = df['Email'].iloc[8]
            con10 = df['Email'].iloc[9]
            #con11 = df['Email'].iloc[10]
            # print(contact1)  
            # print(contact2)
            # print(contact3)
            # print(df['Name'].iloc[0])
            try:
                speak("Whom do you want to send an email, sir?")
                to = TakeCommand()
                if to == contact1:
                    to = con1
                    speak("What should I send, sir?")
                    content = TakeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent successfully to the contact, sir")
                elif to == contact2:
                    to = con2 
                    speak("What should I send, sir?")
                    content = TakeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent successfully to the contact, sir")
                elif to == contact3:
                    to = con3 
                    speak("What should I send, sir?")
                    content = TakeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent successfully to the contact, sir")
                elif to == contact4:
                    to = con4 
                    speak("What should I send, sir?")
                    content = TakeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent successfully to the contact, sir")
                elif to == contact5:
                    to = con5 
                    speak("What should I send, sir?")
                    content = TakeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent successfully to the contact, sir")
                elif to == contact6:
                    to = con6 
                    speak("What should I send, sir?")
                    content = TakeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent successfully to the contact, sir")
                elif to == contact7:
                    to = con7 
                    speak("What should I send, sir?")
                    content = TakeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent successfully to the contact, sir")
                elif to == contact8:
                    to = con8 
                    speak("What should I send, sir?")
                    content = TakeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent successfully to the contact, sir")
                elif to == contact9:
                    to = con9 
                    speak("What should I send, sir?")
                    content = TakeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent successfully to the contact, sir")
                elif to == contact10:
                    to = con10
                    speak("What should I send, sir?")
                    content = TakeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent successfully to the contact, sir")
                # elif to == contact11:
                #     to = con11
                #     speak("What should I send, sir?")
                #     content = TakeCommand()
                #     sendEmail(to, content)
                #     speak("Email has been sent successfully to the contact, sir")
            except Exception as e:
                print(e)
                speak("Sorry Sir, there was a problem in sending the email to the contact!")

            
            # if to == contact1:
            #     speak(f"You are sending an email to {to}")
            #     print(f"You are sending a mail to {to}")
            #     speak(contact1)
            # elif contact2 in query:
            #     print(f"You are sending an email to {contact2}")
            #     speak(contact2)
            # elif contact3 in query:
                # print(f"You are sending an email to {contact3}")
                # speak(contact3)
            # content = TakeCommand()

        elif 'google search for' in query:
            speak("Searching on Google...")
            query = query.replace("google search for", "")
            for j in search(query,tld="com",num=10, stop=10, pause=2):
                print(j)
                speak(j)

        elif 'google search' in query:
            speak("These Are The Results...")
            query = query.replace("google search","")
            # for term in query:
                # url = "https://www.google.com.tr/search?q={}".format(term)
            url = "https://www.google.com.tr/search?q={}".format(query)
            webbrowser.open_new_tab(url)
                # webbrowser.open(url)

        # elif 'power off' in query:
        #     speak("Shutting Down Sir. Happy To Help. Bye!")
        #     exit()
        # if 'friday what is the meaning of' in query:
        #     speak("Searching in Dictionary...")
        #     dictionary=PyDictionary()
        #     query = query.replace("friday what is the meaning of", "")
        #     results = dictionary.meaning(query)
        #     speak("According to the Dictionary,")
        #     speak(results)
            
        # else:
        #     speak("This Functionality is Yet To Be Added Into Me Sir")