
from Model import Model_Admin
import pickle
import os
class Controller_Admin:
    def __init__(self, db_path):
        self.db_path = db_path
        self.admins = []
        self.initialize_user()  # inizializza il controller

    def initialize_user(self):
        if os.path.getsize(self.db_path) == 0:  # se il file è vuoto scrive nel file l'utente di default
            with open(self.db_path, 'wb') as db_file:
                pickle.dump(Model_Admin.Model_Admin('admin', 'admin'), db_file)
        else:
            self.admins = self.load_from_file()  # altrimneti carica il file

    def create_user(self, username, password):
        admin = Model_Admin.Model_Admin(username, password)
        self.admins.append(admin)
        self.save_to_file()

    def user_exists(self, username):
        for Model_Admin in self.admins:
            if Model_Admin.username == username:
                return True
        return False

    def get_user(self, username):
        for Model_Admin in self.admins:
            if Model_Admin.username == username:
                return Model_Admin
        return None

    def update_user(self, username, new_password):
        for Model_Admin in self.admins:
            if Model_Admin.username == username:
                Model_Admin.password = new_password
                self.save_to_file()
                return
        raise ValueError(f"User {username} not found")

    def delete_user(self, username):
        self.admins = [user for user in self.admins if user.username != username]
        self.save_to_file()

    def save_to_file(self):
        with open(self.db_path, 'wb') as db_file:
            pickle.dump(self.admins, db_file)

    def load_from_file(self):
        try:
            with open(self.db_path, 'rb') as db_file:
                return pickle.load(db_file)
        except FileNotFoundError:
            return []