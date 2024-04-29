import Database


#esempio di controller
class Controller:
    def __init__(self):
     def vedere_utente(utente):
            return print(utente)

     def change_utente(utente):
         utente.nome = input("Nome utente: ")
         utente.email = input("Email utente: ")
         utente.password = input("<PASSWORD>: ")
         return print("Utente modificato")

     def remove_utente(utente):
         Database.remove(utente)
         return print("Utente eliminato")

     def create_utente(utente):
         utente.name = input("Nome utente: ")
         utente.email = input("Email utente: ")
         utente.password = input("<PASSWORD>: ")
         return print("Utente creato")