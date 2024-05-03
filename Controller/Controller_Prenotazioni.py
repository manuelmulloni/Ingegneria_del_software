
import pickle
import Model.Model_Prenotazioni
import Database
from Model import Model_Prenotazioni

class Controller_Prenotazioni():
    def __init__(self):
        self.prenotazioni = []

    def insert(self, dict):
        with open('Database\Prenotazioni.pickle', 'wb') as f:
            self.prenotazioni.append(dict)  #inserisce nel file la prenotazione
            pickle.dump(self.prenotazioni, f)


    def read(self):
        with open('Database\Prenotazioni.pickle', 'rb') as f:   # leggo le prenotazioni dal file
             return print(pickle.load(f))

    def update(self, dict, new):
        with open('Database\Prenotazioni.pickle', 'wb') as f:
            self.prenotazioni.remove(dict) #cambia nel file la prenotazione
            self.prenotazioni.append(new)
            f.write(pickle.dumps(self.prenotazioni))


    def delete(self, dict):
        with open('Database\Prenotazioni.pickle', 'wb') as f:
            self.prenotazioni.remove(dict)    #cancella dal file la prenotazione
            f.write(pickle.dumps(self.prenotazioni))