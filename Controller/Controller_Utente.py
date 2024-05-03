import Model.Model_Utente
import Database
import pickle


class Controller_Utente:


    def __init__(self):
        self.lista_Utente = []

    def vedere_utente(self, dict):
        if dict in self.lista_Utente:     #vede l'utente dalla lista e legge il dizionario
            return print(dict)

    def inserire_Utente(self, dict):
        with open('Database\Lista_Utente.pickle', 'ab') as file:
            self.lista_Utente.append(dict)  #inserisce l'utente nel file
            pickle.dump(list(self.lista_Utente), file)

    def eliminare_Utente(self, dict):
        with open('Database\Lista_Utente.pickle', 'wb') as file:
            if dict in self.lista_Utente:        #elimina l'utente dal file
                self.lista_Utente.remove(dict)
                pickle.dump(list(self.lista_Utente), file)
    def change_utente(self, dict, new_Utente):
         with open('Database\Lista_Utente.pickle', 'wb') as file:
             self.lista_Utente.remove(dict)   #cambia l'utente nella lista
             self.lista_Utente.append(new_Utente)
             pickle.dump(self.lista_Utente, file)

