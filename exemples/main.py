import pyttsx3
import webbrowser
import speech_recognition as sr
import wolframalpha
import sys
from random import *
import datetime
import requests
import json

engine = pyttsx3.init()
voices = engine.getProperty ('voices')
global command
command = ['temps',
            'donne l\'heure',
            'ouvre youtube',
            'ouvre streaming',
            'recherche',
            'merci',
            'tu m\'entends'
        ]

def voice(audio):
    engine.say(audio)
    engine.runAndWait()

def randchar():
    rnd = ['Oui je vous entend  monsieur',
            'Et vous vous m\'entendez. Ou je dois vous commander un appareil auditif',
            # 'Ho ferme ta gueule, ou je te monte en l\'air',
            'Bien evidement monsieur',
            # 'Ta gueule',
            'Arraite de faire le fiere t\'es pas tony stark'
        ]
    global liste
    liste = choice(rnd)

def meteo():
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&units=metric&q='
    global city
    city= "Paris"
    url = api_address + city
    json_data = requests.get(url).json()
    global format_add
    format_add= json_data['main']['temp']

def mycommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
     try:
        query = r.recognize_google(audio, language='fr-in')
        global vocale
        vocale = query.split()
     except sr.UnknownValueError:
        query = str(input('Command: '))
     return query

def main():
    meteo()
    randchar()
    temperature = str(format_add)[0:2]
    datehour = str(datetime.datetime.now().hour)
    dateminute = str(datetime.datetime.now().minute)
    date = str('il est '+ datehour + 'heure '+ dateminute)

    print(command)
    voice('Bienvenue Raphael. En quoi puis-je vous aider')
    while True:
        query = mycommand()
        query = query.lower()
        if command[6] in query:
            voice(liste)
        if command[0] in query:
           voice('il fait actuellement' + temperature + 'degrais a ' + city)
        if command[1] in query:
            if datehour == '0':
                datehour = 'minuit'
            voice(date)
        if command[2] in query:
            voice('avez vous une prerference')
            search = mycommand()
            if 'non' in search:
                voice ('je vous ouvre you tube tout de suite')
                webbrowser.open_new('https://www.youtube.com/')
            elif 'oui' in search:
                voice ('Quelle youtubeur voulez-vous')
                youtuber = mycommand()
                voice ('je lance ' + youtuber)
                webbrowser.open_new('https://www.youtube.com/results?search_query=%s'%youtuber)
        if command[3] in query:
            voice('je vous ouvre time tou watch tout de suite')
            webbrowser.open_new('https://www.disneyplus.com/fr-fr/home')
        if command[4] in query:
            voice ('que rechercher vous?')
            search = mycommand()
            voice('je vous ouvre les recherche que j\'ai trouver pour %s tout de suite' %search)
            webbrowser.open_new('http://google.com/search?q=%s'%search)
        elif command[5] in query:
            voice('je vous remercie. A bientot')
            sys.exit()

if __name__ == '__main__':
    main()