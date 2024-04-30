import Database


class Module_Admin:
    def __init__(self, name, age, email, password):
         self.name = name
         self.age = age
         self.email = email
         self.password = password
         Database.dump(self, 'proprietario')










