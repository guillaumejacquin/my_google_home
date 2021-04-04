from googletrans import Translator
import pycountry


def translate(text, pays):
    initales_pays = pycountry.countries.search_fuzzy(pays)

    country = initales_pays[0]
    initialeLangue = country.alpha_2  # 'FR'

    tr = Translator()
    output = tr.translate(text, initialeLangue)
    print(output.text)

pays = "france"
texte = "Ciao, sono italiano, mi chiamo Guillaume"

translate(texte, pays)