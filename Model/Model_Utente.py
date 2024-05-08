


class Model_Utente():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.user_type = 'Utente'   #inizializzo le variabili

    def get_info_Utente(self):
        return {
                "username": self.username,  #creo un dizionario di utente
                "password": self.password,
                "user_type": self.user_type
                }




