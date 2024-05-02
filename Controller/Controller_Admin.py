import Database


#esempio di controller
class Controller_Admin:
    def __init__(self):
        self.lista_Admin = []

    def vedere_utente(utente):
        return print(utente)

    def change_utente(utente):
        #importare da database metodo che cambia il file
         utente.nome = input("Nome utente: ")
         utente.email = input("Email utente: ")
         utente.password = input("<PASSWORD>: ")
         return print("Utente modificato")

    def remove_utente(utente):
         #importare da database metodo che elimina sul file
         return print("Utente eliminato")

    def create_utente(utente):
         utente.name = input("Nome utente: ")
         utente.email = input("Email utente: ")
         utente.password = input("<PASSWORD>: ")
         return print("Utente creato")