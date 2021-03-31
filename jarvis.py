from google_speech import Speech
import speech_recognition as sr
from differents_class import *
from mic import *
from params.assistant import *

infos = Voice_assistant()

def say_speech(mess, infos):
    speech = Speech(mess, infos.langue)
    speech_vitesse = ("speed", infos.vitesse)
    speech.play(speech_vitesse)


def cmd(cmd):   
    if (cmd == "bonjour"):
        message = "bonjour" + infos.user_name
        say_speech(message, infos)

    if (cmd == "merci " + infos.name):
        message = "Vous servir est toujours un plaisir " + infos.user_name
        say_speech(message, infos)
    params(cmd, infos)



def presentation():
    text = "Bonjour Je suis votre assistant. En quoi puis-je vous aider"
    lang = "fr"
    speech = Speech(text, lang)
    sox_effects = ("speed", infos.vitesse)
    speech.play(sox_effects)


def main():
    presentation()
    while True:
        query = myspeech()
        query = query.lower()
        print(query)
        
        cmd(query)



main()