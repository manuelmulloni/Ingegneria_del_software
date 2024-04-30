import Model.Model_Utente



class Controller_Utente:
    def __init__(self):
        self.Controller_Utente = []

    def vedere_utente(Module_Utente):
            return print(Module_Utente)

    def change_utente(Module_Utente):
        #importare da database metodo che cambia il file
         Module_Utente.nome = input("Nome utente: ")
         Module_Utente.email = input("Email utente: ")
         Module_Utente.password = input("<PASSWORD>: ")
         return print("Utente modificato")

    def remove_utente(Module_Utente):
         #importare da database metodo che elimina sul file
         return print("Utente eliminato")

    def create_utente(Module_Utente):
         Module_Utente.name = input("Nome utente: ")
         Module_Utente.email = input("Email utente: ")
         Module_Utente.password = input("<PASSWORD>: ")
         return print("Utente creato")