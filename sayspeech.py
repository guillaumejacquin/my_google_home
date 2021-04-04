 query = myspeech()
        query = query.lower()
        print(query)
        if (query == "retour en arrière"):
            mess = "Bien, nous revoila dans le menu principal."
            say_speech(mess, infos)
            break