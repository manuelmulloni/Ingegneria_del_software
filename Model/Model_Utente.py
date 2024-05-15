class Model_Utente:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.to_dict()

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'user_type': 'Utente'
        }