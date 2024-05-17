
import pickle
import Database
from Model import Model_Prenotazioni
import os
class Controller_Prenotazioni:
    def __init__(self, db_path):
        self.db_path = db_path
        self.prenotazioni = []
        self.initialize_prenotazioni()  # inizializza il controller

    def initialize_prenotazioni(self):
        if os.path.getsize(self.db_path) == 0:  # se il file è vuoto scrive nel file l'utente di default
            with open(self.db_path, 'wb') as db_file:
                pickle.dump(Model_Prenotazioni.Model_Prenotazioni('U', 'd','p', 's'), db_file)
        else:
            self.prenotazioni = self.load_from_file()  # altrimneti carica il file

    def create_booking(self, username, data, parruchiere, servizio):
        prenotazione = Model_Prenotazioni.Model_Prenotazioni(username, data, parruchiere, servizio)
        self.prenotazioni.append(prenotazione)
        self.save_to_file()

    def user_exists(self, username):
        for Model_Prenotazioni in self.prenotazioni:
            if Model_Prenotazioni.username == username:
                return True
        return False

    def get_user(self, username):
        for Model_Prenotazioni in self.prenotazioni:
            if Model_Prenotazioni.username == username:
                return Model_Prenotazioni
        return None

    def update_user(self, username, new_password):
        for Model_Prenotazioni in self.prenotazioni:
            if Model_Prenotazioni.username == username:
                Model_Prenotazioni.password = new_password
                self.save_to_file()
                return
        raise ValueError(f"User {username} not found")

    def delete_user(self, username):
        self.prenotazioni = [user for user in self.prenotazioni if user.username != username]
        self.save_to_file()

    def save_to_file(self):
        with open(self.db_path, 'wb') as db_file:
            pickle.dump(self.prenotazioni, db_file)

    def load_from_file(self):
        try:
            with open(self.db_path, 'rb') as db_file:
                return pickle.load(db_file)
        except FileNotFoundError:
            return []
    def get_all_bookings(self):
        return self.prenotazioni


