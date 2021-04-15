from google_speech import Speech
import speech_recognition as sr
from differents_class import *
from mic import *
from params.assistant import *
from datetime import datetime, timedelta
from jeux.pileouface import *
from jeux.aki import *

from trad.googletrad import *
from wikipedio.wiki import *

infos = Voice_assistant()
listedejeux = ["pile ou face"]
def say_speech(mess, infos):
    speech = Speech(mess, infos.langue)
    speech_vitesse = ("speed", infos.vitesse)
    speech.play(speech_vitesse)

def diff_jeux(infos):
    message = "D'accord, vous voila dans le menu jeu. Choisissez votre jeu, vous pouvez obtenir la liste des differentes options, avec la commande liste des jeux. Si vous voulez quitter dites la commande retour en arriere!"
    say_speech(message, infos)

    while True:
        query = myspeech()
        query = query.lower()
        print(query)
        if (query == "retour en arrière"):
            mess = "Bien, nous revoila dans le menu principal."
            say_speech(mess, infos)
            break

        if (query == "liste des jeux"):
            j = 1
            for i in listedejeux:
                mess = i
                say_speech(str(j), infos)
                say_speech(mess, infos)
                j += 1

        if (query == "pile ou face"):
            pileouface(infos)

        if (query == "akinator"):
            akinatorus(infos)




def cmd(cmd):   
    if (cmd == "bonjour"):
        message = "bonjour" + infos.user_name
        say_speech(message, infos)

    if (cmd == "merci " + infos.name):
        message = "Vous servir est toujours un plaisir " + infos.user_name
        say_speech(message, infos)
    params(cmd, infos)

    if (cmd == "donne l'heure"):
        # mess = ((datetime.now() + timedelta(hours=9)).strftime('%H heures %M minutes m%S secondes'))
        message ="bonjour, il est actuellement " + str(datetime.now())[11:19]
        say_speech(message, infos)

    if (cmd == "jouons à un jeu"):
        print("ok")
        diff_jeux(infos)
    
    if (cmd.startswith('traduis ')):
        translate(cmd, infos)

    if ("wikipédia" in cmd):
        wiki(infos)
    
    

def presentation():
    text = "Bonjour Je suis votre assistant. En quoi puis-je vous aider"
    lang = "fr"
    speech = Speech(text, lang)
    sox_effects = ("speed", infos.vitesse)
    speech.play(sox_effects)
