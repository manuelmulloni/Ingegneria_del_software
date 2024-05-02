
import pickle
import Model.Model_Prenotazioni
import Database
from Model import Model_Prenotazioni

class Controller_Prenotazioni():
    def __init__(self):
        self.prenotazioni = []
    def insert(self, Utente):
        with open('Prenotazioni', 'wb') as f:
            self.prenotazioni.append(Utente)  #inserisce nel file la prenotazione
            pickle.dump(self.prenotazioni, f)
            f.close()

    def read(self):
        with open('Prenotazioni', 'rb') as f:   # leggo le prenotazioni dal file
             pickle.load(f)

    def update(self, Utente, new):
        with open('Prenotazioni', 'wb') as f:
            self.prenotazioni.remove(Utente) #cambia nel file la prenotazione
            self.prenotazioni.append(new)
            f.write(pickle.dumps(self.prenotazioni))


    def delete(self, Utente):
        with open('Prenotazioni', 'wb') as f:
            self.prenotazioni.remove(Utente)    #cancella dal file la prenotazione
            f.write(pickle.dumps(self.prenotazioni))