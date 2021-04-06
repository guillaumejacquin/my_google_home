import akinator
from say_speech.say_speech import *
from mic import *
import speech_recognition as sr



def akinatorus(infos):
    aki = akinator.Akinator()

    q = aki.start_game(language='fr', child_mode=False)
    while aki.progression <= 80:
        say_speech(q, infos)

        query = myspeech()
        a = query.lower()
        print(a)
        if(a == "oui"):
            a = "y"
        if (a == "non"):
            a = "n"
        if (a == "je ne sais pas"):
            a = "i"
        if ( a == "probablement"):
            a = "p"
        if (a == "probablement pas"):
            a = "pn"


        if (a == "stop"):
            say_speech("très bien, au revoir", infos)

            return(1)
        if a == "b":
            try:
                q = aki.back()
            except akinator.CantGoBackAnyFurther:
                pass
        else:
            q = aki.answer(a)
    aki.win()

    correct =(f"la réponse est  {aki.first_guess['name']} ({aki.first_guess['description']})! ai-je raison?\n\t")
    say_speech(correct, infos)

    query = myspeech()
    a = query.lower() + "\n\t"

    if correct.lower() == "oui" or correct.lower() == "y":
        say_speech("Yay\n", infos)
    else:
        say_speech("Oof\n", infos)


