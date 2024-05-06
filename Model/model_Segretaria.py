


class model_Segretaria():
    def __init__(self, id, password):
        self.id = id
        self.password = password


    def get_info_Segretaria(self):
        return {"id": self.id,
                "password": self.password}  #creo dict


