import wikipedia
from googletrans import Translator
from say_speech.say_speech import *
import time


def wiki(infos):
    say_speech("Bien quel sujet cherchez vous?", infos)
    query = myspeech()
    query = query.lower()

    try:
        wikipedia.set_lang("fr")
        result = wikipedia.summary(query, 2)
        say_speech(result, infos)
    except Exception:
        say_speech("je n'ai rien trouvé a ce sujet, reessayez avec un autre mot")



