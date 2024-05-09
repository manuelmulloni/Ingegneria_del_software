
import pickle
import Database
from Model import Model_Prenotazioni
import os
from pathlib import  Path
class Controller_Prenotazioni:
    def __init__(self):
        self.prenotazioni = []
        self.pickle_file_name_prenotazioni = 'Prenotazioni.pickle'
        self.database_dir = os.getenv('Database', default='.')
        self.pickle_file_path = Path(self.database_dir) / self.pickle_file_name_prenotazioni

    def insert(self, dict):

        with open(self.pickle_file_path, 'wb') as f:
            self.prenotazioni.append(dict)  #inserisce nel file la prenotazione
            pickle.dump(self.prenotazioni, f)


    def read(self):
        with open(self.pickle_file_path, 'rb') as f:   # leggo le prenotazioni dal file
             return print(pickle.load(f))

    def update(self, dict, new):
        with open(self.pickle_file_path, 'wb') as f:
            self.prenotazioni.remove(dict) #cambia nel file la prenotazione
            self.prenotazioni.append(new)
            f.write(pickle.dumps(self.prenotazioni))


    def delete(self, dict):
        with open(self.pickle_file_path, 'wb') as f:
            self.prenotazioni.remove(dict)    #cancella dal file la prenotazione
            f.write(pickle.dumps(self.prenotazioni))