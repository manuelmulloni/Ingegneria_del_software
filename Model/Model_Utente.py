import Database


class Model_Utente:
    def __init__(self,name, surname, username, email, password):
        self.name = name
        self.surname = surname
        self.username = username
        self.email = email
        self.password = password
        Database.dump(self, 'Utente') #metodo da vedere


