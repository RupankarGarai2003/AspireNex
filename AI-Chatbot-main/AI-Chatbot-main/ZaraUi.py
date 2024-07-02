##  import all the library you want to use or execute


from ctypes import c_uint16
import ctypes
import subprocess
import bs4
import pyttsx3#pip install pyttsx3
import requests 
import speech_recognition as sr #pip install speechRecognition
import datetime
from wikipedia import wikipedia as wiki #pip install wikipedia
import webbrowser
import os
import smtplib  #pip install secure--smtplib
import time
import keyboard #pip install keyboard
import sys
import os.path
import pyjokes
from requests import get
import json
import pywhatkit
import instaloader
import pyautogui
from wikipedia import wikipedia
import winshell
import operator
from bs4 import BeautifulSoup 
import PyPDF2
import random
from pywikihow import WikiHow, search_wikihow
import psutil
import speedtest
from wikipedia.wikipedia import WikipediaPage, search  ##pip install speedtest-cli
# from PyDictionary import PyDictionary as Diction
# from playsound import playsound
import tkinter
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from ZARAGUI import Ui_ZaraUi



engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 250) # This one is required to slow down the speech frequency.
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[len(voices) -1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    # speak("---------------Initializing Zara----------------")
    # speak("---------------Starting all systems applications-----------------")
    # speak("---------------Installing and checking all drivers---------------")
    # speak("---------------Caliberating and examining all the core processors---------------")
    # speak("---------------Checking the internet connection---------------")
    # speak("---------------Wait a moment sir---------------")
    # speak("---------------All drivers are up and running---------------")
    # speak("---------------All systems have been activated---------------")
    # speak("---------------Now I am online---------------")
    
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%H:%M:%S")
    
    if hour>=0 and hour<=12:
        speak(f"Good Morning! Sayan , its {tt} ")

    elif hour>=12 and hour<=18:
        speak(f"Good Afternoon! Sayan , its {tt}") 

    else:
        speak(f"Good Evening! Sayan , its {tt}")

    speak("I am Zara. Sayani tell me how may I help you")       

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')                             #***** You have to Edit this
    server.sendmail('youremail@gmail.com', to, content)                              #***** And edit this too
    server.close()
    
    
def pdf_reader():
    book = open('py3.pdf', 'rb')
    pdfReader = PyPDF2.PdffileReader(book)    #pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book (pages) ")
    speak(f"sir please enter the page number i have to read")
    pg = int(input("please enter the page number : "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)
    
def search_wikihow(query, max_results=10, lang='en'):
    return list(WikiHow,search(query, max_results, lang))
        
#def run_zara():
  #  command = takeCommand()
  #  print(command)
  #  if 'play'in command:
  #      song = command.replace('play', '')
  #      speak('playing' + song)
  #      pywhatkit.playonyt(song)


 

          
#News
def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]
    
#location
def location():
    speak("Wait boss, let me check")
    try:
        IP_Address = get('https://api.ipify.org').text
        print(IP_Address)
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        print(url)
        geo_request = get(url)
        geo_data = geo_request.json()
        city = geo_data['city']
        state = geo_data['region']
        country = geo_data['country']
        tZ = geo_data['timezone']
        longitude = geo_data['longitude']
        latitude = geo_data['latitude']
        org = geo_data['organization_name']
        print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latitude+" "+org)
        speak(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
        speak(f"and boss, we are in {tZ} timezone the latitude os our location is {latitude}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
    except Exception as e:
        speak("Sorry boss, due to network issue i am not able to find where we are.")
        pass    

#Temperature
def temperature():
        IP_Address = get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        geo_request = get(url)
        geo_data = geo_request.json()
        city = geo_data['city']
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = get(url_1)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        speak(f"current {search} is {temp}")
        
#Random Advise
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']







class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.TaskExecution()
            
     
     
    def YouTubeAuto(self):
        
        speak('whats your command ?')
        command = self.takeCommand()
        
        if 'pause' in command:
            keyboard.press('space bar')
            
        elif "restart" in command:
            keyboard.press('0')
            
        elif "mute" in command:
            keyboard.press('m')
            
        elif "skip" in command:
            keyboard.press('l')
            
        elif "back" in command:
            keyboard.press('j')
            
        elif "full screen" in command:
            keyboard.press('f')
            
        elif "film mode" in command:
            keyboard.press('t')
            
            speak("done sir")
        
        
    def ChromeAuto(self):
        speak("Chrome Automation started !")
        
        command = self.takeCommand()
        
        if 'close the tab' in command:
            keyboard.press_and_release('ctrl + w')
            
        elif'open new tab' in command:
            keyboard.press_and_release('ctrl + t')
            
        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')
            
        elif 'histry' in command:
            keyboard.press_and_release('ctrl + n')
            
    #dictionary        
    def Dict(self):
        speak("Activated Dictionary")
        speak("Tell Me The Problem")
        problem1 = self.takeCommand()
        
        if 'meaning' in problem1:
            problem1 = problem1.replace("what is the", "")
            problem1 = problem1.replace("zara", "")
            problem1 = problem1.replace("of","" )
            problem1 = problem1.replace("meaning", "")
            result = Diction.meaning(problem1)
            speak(f"The Meaning For {problem1} is {result}")
            
        elif 'synonym' in problem1:
            problem1 = problem1.replace("what is the", "")
            problem1 = problem1.replace("zara", "")
            problem1 = problem1.replace("of", "")
            problem1 = problem1.replace("synonym", "")
            result = Diction.synonym(problem1)
            speak(f"The Synonym For {problem1} is {result}")       
            
        elif 'antonym' in problem1:
            problem1 = problem1.replace("what is the", "")
            problem1 = problem1.replace("zara", "")
            problem1 = problem1.replace("of", "")
            problem1 = problem1.replace("antonym", "")
            result = Diction.antonym(problem1)
            speak(f"The Antonym For {problem1} is {result}")  
            
        speak("Exited Dictionary")
    
    #music   
    def Music(self):
      speak("Tell Me The Name Of The music")
      musicName = self.takeCommand()
      
      if 'Dharia' in musicName:
          os.startfile('D:\\music\\Dharia.mp3')
          
      else:
          pywhatkit.playonyt(musicName)
          
          speak("Your Song Has Been Started, Enjoy Sir")
     
     
     
        
    def takeCommand(self):
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Talk to zara...")
            r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source)
        # audio = r.listen(source)
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)  
            speak("say that again please...")  
            print("Say that again please...")  
            return "None"
        query = query.lower()
        return query  
  
          
# if __name__ == "__main__":
    def TaskExecution(self):
    
        wishMe()
        interrogative =["whom", "whose", ]       # Interrogative Words or the words which are used in questions
        ytq = ["play", "song",]    # Interrogative Words or the words which are used in questions
        
        
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe")) # So that it opens only in Chrome Browser
        # chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe%s"
        
        while True:
        # if 1:
            self.query = self.takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in self.query:                                                    ## anything search in wikipedia
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")                                 
                wiki = wikipedia.summary(query,3)
                speak(f"According to Wikipedia :{wiki}")
        
                
            elif any(words in self.query for words in interrogative):       # Required to understand if the query is a question then it will search on google
                webbrowser.get('chrome').open("google.com/search?q="+query)
            
            
            elif 'open stack overflow' in self.query:                                  ##(open stackoverflow)
                speak("opening stackoverflow")
                webbrowser.open("stackoverflow.com")
                
            elif "close stackoverflow" in self.query:                                   #close stackoverflow
                speak("closing stackoverflow")
                os.system("TASKKILL /F /im chrome.exe")
                
            elif "open notepad" in self.query:                                               # open notepad
                codepath = " C:\\Windows\\System32\\Notepad.exe"
                os.startfile(codepath)
                
            elif "open github" in self.query:                                           #open github
                    speak("opening github")
                    webbrowser.open_new_tab('https://www.github.com')
                    
            elif "close github" in self.query:                                          #close stackoverflow
                speak("closing github")
                os.system("TASKKILL /F /im chrome.exe")
                
            elif 'open twitter' in self.query:
                print("Opening twitter...")
                speak("Opening twitter...")
                webbrowser.get().open('http://www.twitter.com')
            
                        
            elif "open hackerrank" in self.query:                                        #open hackerrank
                speak("opening hackerrank")
                webbrowser.open_new_tab('https://www.hackerrank.com')
                
            elif "close hackerrank" in self.query:                                      #close hackerrank
                    speak("closing hackerrank")
                    os.system("TASKKILL /F /im chrome.exe")
                
            elif "open amazon" in self.query:                                           #open amazon
                speak("opening amazon")
                webbrowser.open_new_tab('https://www.amazon.com')
            
            elif "close amazon" in self.query:                                            # close amazon
                speak("closing amazon")
                os.system("TASKKILL /F /im chrome.exe")
                
            elif "open flipkart" in self.query:                                          #open flipkart     
                speak("opening flipkart")
                webbrowser.open_new_tab('https://www.flipkart.com')
                
            elif "close flipkart" in self.query:                                          #close flipkart
                speak("closing flipkart")
                os.system("TASKKILL /F /im chrome.exe")
                
            elif 'open vsc' in self.query:                                               ##(open code function)
                    speak("opening vsc")
                    codePath = "D:\\Microsoft VS Code\\Code.exe"                   
                    os.startfile(codePath) 
                    
            elif "close vsc" in self.query:                                               # close vs code
                speak("closing vsc")
                os.system("TASKKILL /F /im Code.exe")
                    
            elif 'open bluestack' in self.query:
                application = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
                os.startfile(application)
                    
        # elif 'open google' in self.query:                                           ##(open google function)
                # webbrowser.open_new_tab("https://www.google.com")       
                # speak("Google chrome is open now")
                # time.sleep(5)
            
            
            elif "open my facebook account" in self.query:                           # facebook account
                speak("opening your facebook account sir")
                webbrowser.open_new_tab('https://www.facebook.com/sayan.gupta.906')
                
            elif "close facebook" in self.query:                                     # close facebook
                speak("closing facebook")
                os.system("TASKKILL /F /im chrome.exe")

            elif  'google search' in self.query:                                          ##(for specific search on google)
                import wikipedia as googleScrap
                query = query.replace("google" , "")
                query = query.replace("Zara" , "")
                query = query.replace("google search", "")
                speak("This Is What I Found On the Web")
                pywhatkit.search(query)
                
                try:
                    result = googleScrap.summery(query,3)
                    speak(result)
                    
                except:
                    speak("There Is No Data Available")
                
            elif "close google" in self.query:
                speak("closing google")
                os.system("TASKKILL /F /im chrome.exe")
                
            elif 'open gmail' in self.query:                                      ##(open gmail function)
                    webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")                        
                    speak("Google Mail open now")
                    time.sleep(5)
                    
            elif "close gmail" in self.query:
                speak("closing gmail")
                os.system("TASKKILL /F /im chrome.exe")
                    
            elif 'open youtube' in self.query:                                                 ##(open youtube function)
                    webbrowser.open_new_tab("https://www.youtube.com")          
                    speak("youtube is open now")
                    time.sleep(5)
                    
            elif "close youtube" in self.query:
                speak("closing youtube")
                os.system("TASKKILL /F /im chrome.exe")
                    
            elif "open command prompt" in self.query:                             #open cmd
                    speak("opening command prompt")
                    os.system("start cmd")
                    
            elif "close command prompt" in self.query:
                speak("closing command prompt")
                os.system("TASKKILL /F /im cmd.exe")
                    
                    
            elif 'launch' in self.query:                                 # launch any website
                speak("Tell Me The Name of The website")
                name = self.takeCommand()
                web = 'https://www.' + name + '.com'
                webbrowser.open(web)
                speak("done sir.")
                
            elif 'youtube search' in self.query:                         # yt search
                speak("ok sir, This is What i found for your search")
                query = query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open(web)
                speak("done sir")
                
                
                
        # YOUTUBE AUTOMATION       
            elif "youtube tool" in self.query:                           #controll youtube
                self.YouTubeAuto()
                
            if 'pause' in self.query:
                keyboard.press('space bar')
            
            elif "restart" in self.query:
                keyboard.press('0')
            
            elif "mute" in self.query:
                keyboard.press('m')
            
            elif "skip" in self.query:
                keyboard.press('l')
            
            elif "back" in self.query:
                keyboard.press('j')
            
            elif "full screen" in self.query:
                keyboard.press('f')
            
            elif "film mode" in self.query:
                keyboard.press('t')
                
                
                
                
        # CHROME AUTOMATION  
            elif 'Chrome Automation' in self.query:
                self.ChromeAuto()
                
            if 'close the tab' in self.query:
                keyboard.press_and_release('ctrl + w')
            
            elif'open new tab' in self.query:
                keyboard.press_and_release('ctrl + t')
                
            elif 'open new window' in self.query:
                keyboard.press_and_release('ctrl + n')
                
            elif 'histry' in self.query:
                keyboard.press_and_release('ctrl + n')


            elif 'dictionary' in self.query:
                self.Dict()
                
            elif 'music' in self.query:
                self.Music()
                
            elif 'alarm' in self.query:
                speak("Enter The time")
                time = input(": Enter The Time :")
                
                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")
                    
                    if now == time:
                        speak("Time To Wake Up Sir")
                        playsound('Tones-and-I-Dance-Monkey.mp3')
                        speak("Alarm Closed")
                        
                    elif now > time:
                        break
                    
            
            elif "temperature" in self.query:
                  temperature()
                    
                    
            elif ' video downloader' in self.query:
                root = Tk()
                root.geometry('500x300')
                root.resizable(0,0)
                root.title("YouTube Video Downloader")
                speak("Enter Video URL Hare :")
                Label(root, text = "YouTube Video Downloader", font = "arial 15 bold").pack()
                link = StringVar()
                Label(root, text = "Paste The Video URL Hare", font = "arial 15 bold").place(x= 160,y= 60)
                Entry(root, width = 70, textvariable = link).place(x= 32, y= 90)
                
                def VideoDownloader():
                    url = YouTube(str(link.get()))
                    video = url.streams.first()
                    video.download()
                    Label(root, text = "Downloaded", font = 'arial 15').place(x= 180, y= 210)
                    
                Button(root,text = "Download", font= 'arial 15 bold', bg = 'pale violet green', padx = 2 , command = VideoDownloader).place(x= 180,y= 150)
                
                root.mainloop() 
                speak("Video Downloaded")  
                
                
                
                
            elif 'movie time ' in self.query:
                    speak("here , your favourite marvel iron man movies are here,kick off with these")
                    stMsgs = ('https://www.jiocinema.com/watch/movies/iron-man/0/0/05f9acb08d7c11e89e8fede614b72917/0/0'),('https://www.jiocinema.com/watch/movies/iron-man-2/0/0/fe2cd7f087cc11e89e8fede614b72917/0/0'),('https://www.jiocinema.com/watch/movies/iron-man-3/0/0/23fe3d7087cd11e89e8fede614b72917/0/0'),('https://www.jiocinema.com/watch/movies/marvel-s-avengers--age-of-ultron/0/0/4ae50b404c7511e9903837af22bc175d/0/0'),('https://www.jiocinema.com/watch/movies/marvel-s-the-avengers/0/0/450bcb10890611e89e8fede614b72917/0/0'),('https://www.primevideo.com/detail/0I5LRK6CE9IXBRYT4BB0KXMKP5/ref=atv_dp_season_select_s2')
                    webbrowser.open(random.choice(stMsgs)) 

                        
                    
                
                
                
                
                
                
                
            elif 'repert my word' in self.query:
                speak("speak the word !")
                jj = self.takeCommand()
                speak(f"You Said : {jj}")
                                
            elif 'tell me the time' in self.query:                                                           ##(the time function)
                strTime = datetime.datetime.now().strftime("%H:%M:%S")                                        
                speak(f"Sir, the time is {strTime}")
                
                
            elif 'email to sayan' in self.query:                                         ##(send mail function)
                try:
                    speak("What should I say?")
                    content = self.takeCommand()
                    to = "sayanyourEmail@gmail.com"                   
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend sayan bhai. I am not able to send this email") 
                    
                            
            elif"you are beautiful" in self.query:
                speak("i am blushing sir, please do not tease me but thank you sir")
                
                        
            elif "who made you" in self.query or "who created you" in self.query or "who discovered you" in self.query:      ##(who made YOU function)
                    speak("I was built by SAYAN")                  
                    print("I was built by SAYAN")
                    
                        
            elif 'who are you' in self.query or 'what can you do' in self.query:       ##(who are you function)               
                    speak('I am zara version 1 point O your personal assistant. I am programmed to minor tasks like'
                        'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                        'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
                    
                
            elif 'who is your best friend' in self.query:                      ##(for best friend)
                    speak('Sweta roy is my best friend')
                    
            elif "how are you" in self.query:                                            ##(how are you)
                    speak("I'm fine sir, how can i help you ")                  

            elif  "fine" in self.query:
                speak("that's great to hare from you. ")
                
            elif "thanks" in self.query:
                speak("it's my pleaser sir.")         
                    
            elif "i love you" in self.query:                               #i love you
                speak("It's hard to understand")
                
            elif "will you be my gf" in self.query or "will you be my bf" in self.query:             #will you be my gf
                speak("I'm not sure about, may be you should give me some time")

            elif 'reason for you' in self.query:                                              ##reason for you
                    speak("I was created as a Minor project by Mister Sayan")
                    
            elif "why you came to this world" in self.query:                                       ##why you came to this world
                    speak("Thanks to Sayan. further It's a secret")
                
            elif "who i am" in self.query:                                                      # who i am
                        speak("If you talk then definitely your human.")
                
            elif 'tell me a joke' in self.query:                                                        ## joke
                    speak(pyjokes.get_joke())

            elif "who are my parents" in self.query:                                          #parents name called
                    speak('Mahua gupta and Ananda gupta are my parents')
                    
            elif "send message" in self.query:                                                      # send message on whats app
                pywhatkit.sendwhatmsg("+91sending number", "this is best project",2,25)
                    
            elif "hello" in self.query:
                speak("hello sir , may i help you with something")
                
            elif "ip address" in self.query:                                                    # ip addressS
                #from requests import get
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")
                    
            elif 'location' in self.query:                                                    # location
                location()
                    
                    
            elif "instagram profile" in self.query or "profile on instagram" in self.query:                             # instagram profile
                speak("sir please enter the user name correctly.")
                name = input("enter user name hare:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account.")
                condition = self.takeCommand().lower()
                if "yes" in condition:
                    ig = instaloader.Instaloader()  #pip3 install instaloader
                    ig.download_profile(name, profile_pic_only = True)
                    speak("i am done sir , profile picture is saved in our main folder")
                else:
                    pass
                
                
            elif "take screenshot" in self.query or "take a screenshot" in self.query:                                 # take screen shot
                    speak("sir , please tell me the name of the screen shot file")
                    name = self.takeCommand().lower()
                    speak("please sir hold the screen for few seconds , i am taking screenshot.")
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak(" i am done sir , the screenshot is saved in our main folder. now i am ready for you next command.")
                    
            elif 'news' in self.query:
                speak(f"I'm reading out the latest news headlines, sir")
                speak(get_latest_news())
                speak("For your convenience, I am printing it on the screen sir.")
                print(*get_latest_news(), sep='\n')
                
            elif "advice" in self.query:                                                                  #advice
                speak(f"Here's an advice for you, sir")
                advice = get_random_advice()
                speak(advice)
                speak("For your convenience, I am printing it on the screen sir.")
                print(advice)
                
            elif 'temperature' in self.query:                                                              #temperature
                temperature() 
                
                
            elif "write a note" in self.query:                                                                 # write a note   
                    speak("What should i write,sir")
                    note = self.takeCommand()
                    file = open('zara.txt', 'w')
                    speak("Sir, Should i include date and time")
                    snfm = self.takeCommand()
                    if 'yes' in snfm or 'sure' in snfm:
                        strTime = datetime.datetime.now().strftime("%m-%d-%Y %H:%I%p")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)
                        
            elif "show note" in self.query:                                                                    # show note
                speak("Showing Notes")
                file = open("zara.txt", "r")
                print(file.read())
                speak(file.read(6))
                
                
            elif 'lock window' in self.query:                                                                  # lock window
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'shutdown system' in self.query:                                                             # shoutdown system
                    speak("Hold On a Sec ! Your system is on its way to shut down")
                    subprocess.call('shutdown / p /f')
                    
            elif 'empty recycle bin' in self.query:                                                            # empty recycle bin
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")

            elif 'switch the window' in self.query:                                                             # switch the window
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(2) 
                pyautogui.keyUp("alt")
                
            elif 'read pdf' in self.query:                                                                      # read pdf
                pdf_reader()
                
            
                
            elif "hide all file" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:         # hide all files or folder
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takeCommand().lower()
            if "hide" in self.query:
                    os.system("attrib +h /s /d")
                    speak("sir , all the file in this folder are now hidden")
                    
            elif "visible" in self.query:                                                                         # visible the hidden folder or file
                    os.system("attrib -h /s /d")
                    speak("sir, all the files in this folder are now visible for everyone")
                    
            elif "leave it" in self.query or "leave it for now" in self.query:                                     # for leave it
                    speak("ok sir")
                    
            
                    
            elif 'activate how to do mod' in self.query:                                         # activate how to mode
                    speak("how to do mode is activate")
                    while True:
                        speak("please tell me what you want to know")
                        how = self.takeCommand()
                        try:
                            if "exit" in how or 'close' in how:
                                speak("okay sir, how to do mode is closed")         #pip install pywikihow
                                break
                            else:
                                max_results = 1
                                how_to = search_wikihow(how, max_results)
                                assert len(how_to) == 1
                                how_to[0].print()
                                speak(how_to[0].summary)
                        except Exception as e:
                            speak("sorry sir, i am not able to find this sir")
                        
                        
            elif "remember that" in self.query:                                                  # remember that
                speak('what should i remember sir ?')
                data = self.takeCommand()
                speak("you said me to remember that" +data)
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()
                
            elif 'do you know anything' in self.query:                                    # do you know anythings
                remember = open('data.txt', 'r')
                speak("you said me to that" +remember.read())
                
                
            elif 'what day is it' in self.query:                                            # what day is it
                day = datetime.datetime.today().weekday() + 1
                Day_dict = {1: 'Monday' , 2: 'Tuesday' , 3: 'Wednesday' , 4: 'Thursday' , 5: 'Friday' , 6: 'Saturday' , 7: 'Sunday'}
                if day in Day_dict.keys():
                    day_of_the_week = Day_dict[day]
                    print(day_of_the_week)
                    speak("the day is" + day_of_the_week)
                    time.sleep(2)
                else:
                    speak("i am sorry sir, i did not understand your request")
                    
                    
            elif "how much power left" in self.query or "how much power we have" in self.query:             # battery power check
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system have {percentage} percent battery")
                if percentage>= 75:
                    speak("we have enough power to continue our work")
                elif percentage>=40 and percentage<=75:
                    speak("we should connect our system to charging point to charge our battery")
                elif percentage>=15 and percentage<=30:
                    speak("we do not have enough power to continue our work , please connect to charging")
                elif percentage>=15:
                    speak("we have very low power , please connect to charging , the system will shutdown very soon")
                    
                    
            elif"internet speed" in self.query:                                           #internet speed
                #import speedtest  
                speak("Checking speed.....")                                              
                st = speedtest.Speedtest()
                d1 = st.download()
                cD = int(d1/800000)
                up = st.upload()
                cU = int(up/800000)
                speak(f"sir we have {d1} mbp s downloading speed and {up} mbp s uploading speed")
                
                
            # volume controll (up, down, mute)    
            elif "volume up" in self.query:
                pyautogui.press('volume up')
                
            elif "volume down" in self.query:
                pyautogui.press("volume down")
                
            elif "volume mute" in self.query:                                           # volume mute
                pyautogui.press("volume mute")
                        
            
                    
                                    
            elif 'change background' in self.query:
                ctypes.windll.user32.SystemParametersInfoW(20,
                                                            0,
                                                            "Location of wallpaper",
                                                            0)
                speak("Background changed successfully")
                
                
                
            elif "you can sleep" in self.query:                                                           #sleep function 
                        speak("okay sir , i am going to sleep you can call me anytime.") 
                        speak("Just Say Wake Up Zara !")              
                        break    
                        
            if  "stop" in self.query or "abort" in self.query:                                                    ##(stop function.)
                            speak('your personal assistant zara is shutting down,Good bye')
                            print('your personal assistant zara is shutting down,Good bye')
                            break



startExecution = MainThread()



class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ZaraUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        
        
    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:/jarvisgol.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.ZARAGUI.setText(label_date)
    
        
        
app = QApplication(sys.argv)
zara = Main()
zara.show()
exit(app.exec_())






    # if __name__ == "__main__":
    #    while True:
    #        permission = takeCommand()                      ## this function will also add
    #         if "wake up" in query:
    #            TaskExecution()
    #          elif "goodbye" in query:
    #            speak("thanks for using me sir , have a good day")
    #            sys.exit()
    #          else:
    #            speak("sorry")






    
    # wolffarmalpha is =JKE6L4-UR6JV692AR