import Database


class Model_Admin:
    def __init__(self, username, password):
          self.username = username
          self.password = password
          self.get_Admin()


    def get_Admin(self):
         return {
             'Username': self.username,
             'Password': self.password,
             'User_type': "Admin"
        } #creo dizionario








