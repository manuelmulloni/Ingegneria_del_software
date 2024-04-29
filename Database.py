import pickle

#esempio database
class Database:
    def __init__(self):
        self.db = "database_utente"

    def aggiungi_database(self, object):
        database = pickle.dump(object,"database_utente")

    def aggiornamento_database(self, object):
        database = pickle.dump(object,"database_utente")

    def leggi_database(self, object):
        database = pickle.load("database_utente")

    def leggi_oggetto_database(self, object):
        database = pickle.dumps(object,"database_utente")
    def remove_database(self, object):
        with open("database_utente.pickle", "rb") as object:
            database = pickle.load(object)
            del database[object]
