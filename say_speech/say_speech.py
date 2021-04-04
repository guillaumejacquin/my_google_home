from google_speech import Speech
import speech_recognition as sr
from mic import *

def say_speech(mess, infos):
    speech = Speech(mess, infos.langue)
    speech_vitesse = ("speed", infos.vitesse)
    speech.play(speech_vitesse)

