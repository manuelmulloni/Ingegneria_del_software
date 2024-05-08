from Model import Model_Utente
import Database
import pickle


class Controller_Utente():


    def __init__(self):
        self.lista_Utente = []

    def vedere_utente(self, dict):
        if dict in self.lista_Utente:     #vede l'utente dalla lista e legge il dizionario
            return print(dict)

    def inserire_Utente(self, dict_user):
        self.lista_Utente.append(dict_user)
        with open("C:\\Users\\manue\\Documents\\GitHub\\Ingegneria_del_software\\Database\\Lista_Utenti.pickle", 'wb') as f:
              #inserisce l'utente nel file
            pickle.dump(self.lista_Utente, f)

    def eliminare_Utente(self, dict):
        with open('C:\\Users\\manue\\Documents\\GitHub\\Ingegneria_del_software\\Database\\Lista_Utenti.pickle', 'wb') as file:
            if dict in self.lista_Utente:        #elimina l'utente dal file
                self.lista_Utente.remove(dict)
                pickle.dump(self.lista_Utente, file)
    def change_utente(self, dict, new_Utente):
         with open('C:\\Users\\manue\\Documents\\GitHub\\Ingegneria_del_software\\Database\\Lista_Utenti.pickle', 'wb') as file:
            self.lista_Utente.remove(dict)   #cambia l'utente nella lista
            self.lista_Utente.append(new_Utente)
            pickle.dump(self.lista_Utente, file)

    def check_credentials(self, username, password):
        for user in self.lista_Utente:
            if user['username'] == username and user['password'] == password and user['user_type'] == 'Utente':
                return True
        return False #controlla le credenziali dell'utente


