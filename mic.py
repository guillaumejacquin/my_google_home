import speech_recognition as sr
from google_speech import Speech



def myspeech():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
     try:
        query = r.recognize_google(audio, language='fr-in')
        global vocale
        vocale = query.split()
     except sr.UnknownValueError:
        speech = Speech("je ne vous ai pas compris", "fr")
        speech.play()

        query = str(speech)

     return query
