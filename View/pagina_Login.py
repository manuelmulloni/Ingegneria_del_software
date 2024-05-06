from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from Controller.Controller_Utente import Controller_Utente
from View.view_Utente import view_Utente
class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.controller_utente = Controller_Utente() #inizializza il controller utente


        self.setWindowTitle('Login Page')

        self.layout = QVBoxLayout()

        self.username_label = QLabel('Username')
        self.username_input = QLineEdit()

        self.password_label = QLabel('Password')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.check_credentials)

        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)


    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if self.controller_utente.check_credentials(username, password):  #controlla le credenziali usando il controller utente
            print('Access granted')
            self.view_utente = view_Utente()# se lecredenziali sono giuste apre la pagina utente
            self.view_utente.show()
        else:
            print('Access denied')
