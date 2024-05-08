import Database


class Model_Admin:
    def __init__(self, name, age, email, password):
         self.name = name
         self.age = age
         self.email = email
         self.password = password
         self.user_type = "admin"


    def get_Admin(self):
         return {"name": self.name, "age": self.age, "email": self.email, "password": self.password,
                 "user_type": self.user_type} #creo dizionario








