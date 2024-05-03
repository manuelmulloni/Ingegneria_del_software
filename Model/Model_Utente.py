


class Model_Utente:
    def __init__(self,name, surname, username, email, password):
        self.name = name
        self.surname = surname
        self.username = username
        self.email = email
        self.password = password

    def get_info_Utente(self):
        return {"name": self.name,
                "surname": self.surname,
                "username": self.username,  #creo un dizionario di utente
                "email": self.email,
                "password": self.password
                }




