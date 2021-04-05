from googletrans import Translator
from say_speech.say_speech import *
import time

def translate(text, infos):
    tmp = text.split()
    text = str(tmp[1:])

    tr = Translator()
    output = tr.translate(text, dest= infos.langage_traduction)

    say_speech(output.text, infos)
    time.sleep(0.5)
    print(output)
    texte = "la langue actuelle est :" + str(infos.langage_traduction) + "si vous voulez la changer, vous pouvez la changer avec 'change la langue de traduction'"

    say_speech(texte, infos)

