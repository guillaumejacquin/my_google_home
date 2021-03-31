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

    if (cmd == "quel est ton nom"):
        mess = "je m'appelle " + infos.name
        say_speech(mess, infos)


    if (cmd == "change de nom"):
        change_assistant_name(infos)

    if (cmd == "quel est mon nom"):
        mess = "votre nom  est " + infos.user_name
        say_speech(mess, infos)

    if (cmd == "change mon nom"):
        change_user_name(infos)

    if (cmd == "change ta vitesse"):
        mess = "votre vitesse  est " + infos.user_name
        change_vitesse_bot(infos)



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