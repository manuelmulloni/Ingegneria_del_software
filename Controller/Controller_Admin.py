import Database
import Controller_Utente
import Controller_Prenotazioni
import pickle
#esempio di controller
class Controller_Admin(Controller_Utente.Controller_Utente, Controller_Prenotazioni.Controller_Prenotazioni):
    def __init__(self):
        super(Controller_Admin,self).__init__()
        self.lista_Admin = []


