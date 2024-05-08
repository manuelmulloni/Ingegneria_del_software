import pickle

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from Controller.Controller_Utente import Controller_Utente
from View.view_Utente import view_Utente
from Model.Model_Utente import Model_Utente
import immagini
import Database

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.controller_utente = Controller_Utente() #inizializza il controller utente
        self.controller_utente.lista_Utente = pickle.load(open('C:\\Users\\manue\\Documents\\GitHub\\Ingegneria_del_software\\Database\\Lista_Utenti.pickle', 'rb'))
        self.setWindowTitle('Login Page')

        # Set up background image
        self.background_label = QLabel(self)

        self.layout = QVBoxLayout()

        self.username_label = QLabel('Username')
        self.username_input = QLineEdit()

        self.password_label = QLabel('Password')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.check_credentials)
        self.create_account_button = QPushButton('Crea Account')
        self.create_account_button.clicked.connect(self.crea_account)

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)
        self.layout.addWidget(self.create_account_button)
        self.setLayout(self.layout)

    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if self.controller_Admin.check_credentials(username, password):
            print('Access granted')

        elif self.controller_utente.check_credentials(username, password):
            print('Access granted')
            self.pagina_Utente = view_Utente(username)
            self.pagina_Utente.show()
        else:
            print('Access denied')

    def crea_account(self):
        username = self.username_input.text()
        password = self.password_input.text()

        nuovo = Model_Utente(username, password)
        dict_Utente = nuovo.get_info_Utente() # nonso perche non scirve sul file
        self.controller_utente.inserire_Utente(dict_Utente)

        print(f'Account creato per {username}')
        self.prenotazione = view_Utente(username)
        self.prenotazione.show()

if __name__ == '__main__':
    app = QApplication([])
    window = LoginPage()
    window.show()
    app.exec()
