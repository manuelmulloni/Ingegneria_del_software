

class Model_Prenotazioni():
    def __init__(self, username, data, parruchiere, servizio):
        self.username = username
        self.data = data
        self.parruchiere = parruchiere
        self.servizio = servizio
        self.get_Prenotazioni()




    def get_Prenotazioni(self):
        return {"username": self.username, "data": self.data, "parruchiere": self.parruchiere,
                "servizio": self.servizio}