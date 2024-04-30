import Model_Parrucchiere
import Database



class Model_Prenotazioni():
    def __init__(self, username, data, Module_Parruchiere, taglio):
        self.username = username
        self.data = data
        self.parruchiere = Module_Parruchiere
        self.taglio = taglio
        Database.dump(self) #metododa vedere

