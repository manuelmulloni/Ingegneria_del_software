import Database


class Model_Admin:
    def __init__(self, name, age, email, password):
         self.name = name
         self.age = age
         self.email = email
         self.password = password


    def get_Admin(self):
         return {"name": self.name, "age": self.age, "email": self.email, "password": self.password} #creo dizionario








