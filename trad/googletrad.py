from googletrans import Translator
import pycountry
from say_speech.say_speech import *
import time

def translate(text, infos):
    tmp = text.split()
    text = str(tmp[1:])
    initiales_pays = pycountry.countries.search_fuzzy(infos.langage_traduction)
    print(infos.langage_traduction)
    texte = "la langue actuelle est :" + str(infos.langage_traduction) + "si vous voulez la changer, vous pouvez la changer avec change la langue de traduction"
    
    country = initiales_pays[0]
    initialeLangue = country.alpha_2  # 'FR'

    tr = Translator()
    output = tr.translate(text, initialeLangue)

    say_speech(output.text, infos)
    time.sleep(0.5)
    say_speech(texte, infos)


print(pycountry.countries)
