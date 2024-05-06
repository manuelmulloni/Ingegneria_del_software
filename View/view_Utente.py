from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class view_Utente(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('User Page')

        self.layout = QVBoxLayout()

        self.welcome_label = QLabel('Welcome, user!')
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