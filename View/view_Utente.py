from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from Controller.Controller_Utente import Controller_Utente

class view_Utente(QWidget):
    def __init__(self, username):  #crea la finestra utente con il nome dell'utente che vuole fare la prenotazione
        super().__init__()
        self.controller_utente = Controller_Utente()

        self.setWindowTitle('User Page')

        self.layout = QVBoxLayout()

        self.welcome_label = QLabel('Welcome, ' + username + '!') # crea la label con il nome dell'utente che ha fatto l'accesso
        self.reservation_button = QPushButton('Make a reservation')
        self.reservation_button.clicked.connect(self.make_reservation)

        self.layout.addWidget(self.welcome_label)
        self.layout.addWidget(self.reservation_button)

        self.setLayout(self.layout)

    def make_reservation(self):
        # Here you can add the logic to make a reservation
        print('Reservation made')

    def impostazioni_Profilo(self):
        print('Impostazioni Profilo') # da creare