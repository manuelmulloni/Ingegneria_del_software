from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
import sys
import view_Utente

import prova_view
from Controller import Controller_Utente, Controller_Admin


class pagina_Login(QWidget):
    def __init__(self):
        super().__init__()
        self.user_controller = Controller_Utente.Controller_Utente("C:\\Users\\manue\\Documents\\GitHub\\Ingegneria_del_software\\Database\\Lista_Utenti.pickle")
        self.admin_controller = Controller_Admin.Controller_Admin("C:\\Users\\manue\\Documents\\GitHub\\Ingegneria_del_software\\Database\\Lista_Admin.pickle")
        self.setWindowTitle("Login")

        layout = QVBoxLayout()

        self.username_label = QLabel("Username")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_credentials)

        self.create_account_button = QPushButton("Crea Account")
        self.create_account_button.clicked.connect(self.create_account)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.create_account_button)

        self.setLayout(layout)




    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()
        print("Checking credentials...")
        if self.admin_controller.user_exists(username):
            print("Admin exists!")
            admin = self.admin_controller.get_user(username)
            if admin.Password == password and admin.User_type == "Admin":
                print("Admin logged in!")
                self.admin_view = prova_view.prova_view()
                self.admin_view.show()
        elif self.user_controller.user_exists(username):
            user = self.user_controller.get_user(username)
            if user.password == password:
                self.user_view = view_Utente.view_Utente(username)
                self.user_view.show()
            else:
                print("Incorrect password!")
        else:
            print("User does not exist!")

    def create_account(self):
        username = self.username_input.text()
        password = self.password_input.text()  #crea un nuovo account ma se l'username esiste già non lo crea

        if not self.user_controller.user_exists(username):
            self.user_controller.create_user(username, password)
            print("Account creato con successo!")
            self.view = view_Utente.view_Utente(username)
            self.view.show()
        else:
            print("Username già esistente!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = pagina_Login()
    login_window.show()

    sys.exit(app.exec())