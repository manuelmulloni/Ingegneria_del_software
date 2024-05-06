import Database
import Controller_Utente
import Controller_Prenotazioni
import pickle


class Controller_Segretaria(Controller_Utente.Controller_Utente, Controller_Prenotazioni.Controller_Prenotazioni):
    def __init__(self):
        super(Controller_Segretaria,self).__init__()
        self.Lista_Segretaria = []

    