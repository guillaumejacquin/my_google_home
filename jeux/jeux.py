from google_speech import Speech
import speech_recognition as sr
from differents_class import *
from mic import *
import time
import random


def say_speech(mess, infos):
    speech = Speech(mess, infos.langue)
    speech_vitesse = ("speed", infos.vitesse)
    speech.play(speech_vitesse)



def pileouface(infos):
    mess = "Choisissez, pile ou face?"
    say_speech(mess, infos)
    autorisation = False

    while True:
        query = myspeech()
        query = query.lower()
        print(query)
        predict = 0
        if (query == "pile"):
            autorisation = True
            predict = 1
            break

        if (query == "face"):
            autorisation = True
            predict = 2
            break
        
        else:
            mess = "je ne vous ai aps compris, Choisissez, pile ou face?"
            continue

    if (autorisation == True):
            mess = "Très bien! "

            say_speech(mess, infos)
            time.sleep(0.5)

            mess = "et le resultat est.."
            say_speech(mess, infos)

            time.sleep(2)
            result = random.choice(['pile', 'face'])
            if (result == "pile"):
                predict_ia = 1
            else:
                predict_ia = 2

            
            say_speech(str(result), infos)
            if (predict == predict_ia):
                mess = "Bravo, vous avez encore gagné!"
                infos.ratio_pileouface[0] += 1

            else:
                mess = "Zut pas de chance, vous gagnerez la prochaine fois"
                infos.ratio_pileouface[1] += 1
            say_speech(mess, infos)
            time.sleep(1)

            mess = "Vous êtes actuellement à " + str(infos.ratio_pileouface[0]) + " victoires et à " + str(infos.ratio_pileouface[1]) + " défaites .Votre pourcentage de victoire est de " + str(int((infos.ratio_pileouface[0] / (infos.ratio_pileouface[0] + infos.ratio_pileouface[1]))) *100) + "%. Si vous voulez rejouer dites la commande Rejouer"
            say_speech(mess, infos)
            query = myspeech()
            query = query.lower()
            if (query == "rejouer"):
                pileouface(infos)

            else:
                return(1)


