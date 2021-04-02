from google_speech import Speech
import speech_recognition as sr
from differents_class import *
from mic import *


def say_speech(mess, infos):
    speech = Speech(mess, infos.langue)
    speech_vitesse = ("speed", infos.vitesse)
    speech.play(speech_vitesse)


def change_assistant_name(infos):
    mess = "d'accord, quel nom voulez vous me donner?"
    say_speech(mess, infos)
    while True:
            query = myspeech()
            query = query.lower()
            infos.name = query
            mess = "Le nouveau nom que vous me donnez est " + infos.name + ". Si c'est bien cela, dites oui, sinon dites non"
            say_speech(mess, infos)
            query = myspeech()
            query = query.lower()
            if (query == "oui"):
                mess = "Très bien, je m'appelle dorénavant" + infos.name
                say_speech(mess, infos)
                break
            else:
                mess = "d'accord, quel nom voulez vous me donner?"
                say_speech(mess, infos)



def change_user_name(infos):
    mess = "d'accord, quel nom voulez vous?"
    say_speech(mess, infos)
    while True:
            query = myspeech()
            query = query.lower()
            infos.user_name = query
            mess = "Le nouveau nom que vous desirez est " + infos.user_name + ". Si c'est bien cela, dites oui, sinon dites non"
            say_speech(mess, infos)
            query = myspeech()
            query = query.lower()
            if (query == "oui"):
                mess = "Très bien, vous vous appelez dorénavant" + infos.user_name
                say_speech(mess, infos)
                break
            else:
                mess = "d'accord, quel nom desirez vous?"
                say_speech(mess, infos)


def change_vitesse_bot(infos):
    mess = "D'accord, je vous prie de dire plus lent ou plus rapide afin de régler ensemble ma vitesse"
    say_speech(mess, infos)
    while True:
            query = myspeech()
            query = query.lower()
            print(query)
            
            if (query == "plus lent"):
                vit = float(infos.vitesse) - 0.1
                print(vit)
                if (vit <= 0.9):
                    mess = "Je suis désolé, il m'est encore impossible d'atteindre cette vitesse"
                    say_speech(mess)
                    continue
                infos.vitesse = str(vit)
                
                mess = "d'accord, si cela vous satisfait dites stop, sinon dites plus ou moins"
                say_speech(mess, infos)
                continue
                 
            if (query == "plus rapide"):
                vit = float(infos.vitesse) + 0.1
                infos.vitesse = str(vit)
                mess = "d'accord, si cela vous satisfait dites stop, sinon dites plus ou moins"
                say_speech(mess, infos)
                continue
           
            if (query == "stop"):
                return(1)
            else:
                mess = "je n'ai pas compris, veuillez répéter, plus ou moins, ou bien stop si cela vous suffit"
                say_speech(mess, infos)


def params(cmd, infos):
    if (cmd == "quel est ton nom"):
        mess = "je m'appelle " + infos.name
        say_speech(mess, infos)

    if (cmd == "éteins-toi"):
        mess = "D'accord, a très bientot j'espère"
        say_speech(mess, infos)
        exit (0)
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