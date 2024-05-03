import Model_Parrucchiere
import Database



class Model_Prenotazioni():
    def __init__(self, username, data, parruchiere, taglio):
        self.username = username
        self.data = data
        self.parruchiere = parruchiere
        self.taglio = taglio




    def get_Prenotazioni(self):
        return {"username": self.username, "data": self.data, "parruchiere": self.parruchiere,
                "taglio": self.taglio}