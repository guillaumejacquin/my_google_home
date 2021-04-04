class Voice_assistant:
  def __init__(self):
    self.name = "cécilia le gros bébé"
    self.user_name = "Guillaume"
    self.vitesse = "1.2"
    self.langue = "fr"


    #google_trad
    self.langage_traduction = "france" 

    #pileouface
    self.ratio_pileouface = [0, 0]
  def change_name(self, name):
        self.name = name
