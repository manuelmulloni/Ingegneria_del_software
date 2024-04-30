import Model.Model_Prenotazioni
import Database
from Model import Model_Prenotazioni


class Controller_Prenotazioni():
    def __init__(self):
        self.prenotazioni = []



    def read_prenotazioni(self):
        Model.Model_Prenotazioni.Model_Prenotazioni.data = Database.load(Database, 'data')
        Model.Model_Prenotazioni.Model_Prenotazioni.parruchiere = Database.load(Database, 'parruchiere')
        Model.Model_Prenotazioni.Model_Prenotazioni.taglio = Database.load(Database, 'taglio')

    def search_prenotazioni(self, prenotazioni):
        Database.Database.load(prenotazioni) # sbagliato
    def change_prenotazioni(self, prenotazioni):
        Controller_Prenotazioni.search_prenotazioni(prenotazioni)
        Model.Model_Prenotazioni.Model_Prenotazioni.data = input("Inserisci un prenotazione: ")
        Database.Database.dump(Model.Model_Prenotazioni.Model_Prenotazioni.data, 'data')
