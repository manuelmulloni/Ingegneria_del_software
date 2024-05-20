import os
import pickle
from Model import Model_Utente

class Controller_Utente:
    def __init__(self, db_path):
        self.db_path = db_path
        self.users = []
        self.initialize_user()#inizializza il controller

    def initialize_user(self):
        if os.path.getsize(self.db_path) == 0: #se il file è vuoto scrive nel file l'utente di default
            with open(self.db_path, 'wb') as db_file:
                pickle.dump(Model_Utente.Model_Utente('Utente', 'prenota'), db_file)
        else:
            self.users = self.load_from_file() #altrimneti carica il file


    def create_user(self, username, password):
        user = Model_Utente.Model_Utente(username, password)
        self.users.append(user)
        self.save_to_file()
    def user_exists(self, username):
        for Model_Utente in self.users:
            if Model_Utente.username == username:
                return True
        return False
    def get_user(self, username):
        for Model_Utente in self.users:
            if Model_Utente.username == username:
                return Model_Utente
        return None

    def update_user(self, username, new_password):
        for Model_Utente in self.users:
            if Model_Utente.username == username:
                Model_Utente.password = new_password
                self.save_to_file()
                return
        raise ValueError(f"User {username} not found")

    def delete_user(self, username):
        self.users = [user for user in self.users if user.username != username]
        self.save_to_file()

    def save_to_file(self):
        with open(self.db_path, 'wb') as db_file:
            pickle.dump(self.users, db_file)

    def load_from_file(self):
        try:
            with open(self.db_path, 'rb') as db_file:
                return pickle.load(db_file)
        except FileNotFoundError:
            return []

    def get_all_users(self):
        self.users = self.load_from_file()
        return self.users
