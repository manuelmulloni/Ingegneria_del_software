
import Database
import pickle


class Controller_Utente:
    def __init__(self):
        self.lista_Utente = []

    def vedere_utente(self, Utente):
        with open('Lista_Utente.txt', 'r') as file:
            if Utente in self.lista_Utente:   #vede l'utente dal file
                file.read(Utente in self.lista_Utente)
    def inserire_Utente(self, Utente):
        with open('Lista_Utente.txt', 'a') as file:
            self.lista_Utente.append(Utente)  #inserisce l'utente nel file
            file.write(self.lista_Utente)

    def eliminare_Utente(self, Utente):
        with open('Lista_Utente.txt', 'w') as file:
            if Utente in self.lista_Utente: #elimina l'utente dal file
                self.lista_Utente.remove(Utente)
                file.write(self.lista_Utente)
    def change_utente(self, Utente, new_Utente):
         with open('Lista_Utente.txt', 'w') as file:
             self.lista_Utente.remove(Utente)   #cambia l'utente nella lista
             self.lista_Utente.append(new_Utente)
             file.write(self.lista_Utente)

