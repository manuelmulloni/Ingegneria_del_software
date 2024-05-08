import Database
import Controller_Utente
import Controller_Prenotazioni
import pickle


class Controller_Admin:
    def __init__(self):
        self.lista_Admin = []


    def inserisci_Admin(self, dict):
        with open('Database\Lista_Admin.pickle', 'wb') as f:
            self.lista_Admin.append(dict)
            pickle.dump(self.lista_Admin, f)

    def leggi_Admin(self):
        with open('Database\Lista_Admin.pickle', 'rb') as f:
            return print(pickle.load(f))

    def elimina_Admin(self, dict):
        with open('Database\Lista_Admin.pickle', 'wb') as f:
            self.lista_Admin.remove(dict)
            pickle.dump(self.lista_Admin,f)

    def cambia_Admin(self, dict, new):
        with open('Database\Lista_Admin.pickle', 'wb') as f:
            self.lista_Admin.remove(dict)
            self.lista_Admin.append(new)
            pickle.dump(self.lista_Admin,f)

    def elimina_utente(self, dict):
        with open('Database\Lista_Utente.pickle', 'wb') as f:
            self.lista_Utente.remove(dict)
            pickle.dump(self.lista_Utente,f)

    def read_Utenti(self):
        with open('Database\Lista_Utente.pickle', 'rb') as f:
            return print(pickle.load(f))

    def read_Prenotazioni(self):
        with open('Database\Prenotazioni.pickle', 'rb') as f:
            return print(pickle.load(f))

    def cambia_prenotazioni(self, dict, new):
        with open('Database\Prenotazioni.pickle', 'wb') as f:
            self.prenotazioni.remove(dict)
            self.prenotazioni.append(new)
            pickle.dump(self.prenotazioni,f)

    def check_credentials(self, username, password):
        for Admin in self.lista_Admin:
            if Admin['username'] == username and Admin['password'] == password and Admin['user_type'] == 'Admin':
                return True
        return True #controlla le credenziali dell'admin