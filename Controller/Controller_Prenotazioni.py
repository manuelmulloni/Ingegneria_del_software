import pickle

import Model.Model_Prenotazioni
import Database
from Model import Model_Prenotazioni


class Controller_Prenotazioni():
    def __init__(self):
        self.prenotazioni = []



    def read_prenotazioni(self):  # apre il file prenotazioni che viene poi scritto su self.prenotazioni che viene poi printato
        with open('Prenotazioni', 'rb') as f:
            self.prenotazioni= pickle.load(f)
            return print(self.prenotazioni)


    def search_prenotazioni(self, username):  # cerca nel file prenotazioni un username e se lotrova stampa la prenotazione
        with open('Prenotazioni', 'rb') as f:
            self.prenotazioni= pickle.load(f)
            if Model_Prenotazioni.Model_Prenotazioni.username == username:
                return print(Model_Prenotazioni.Model_Prenotazioni.__str__())

    def change_prenotazioni(self, username):
        with open('Prenotazioni', 'rb') as f:
            self.prenotazioni = pickle.load(f)
            if Model_Prenotazioni.Model_Prenotazioni.username == username: #ci devo ragionare su
                return print("bella")


