from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGroupBox, QGridLayout, QDialog, QDateEdit, QComboBox, QLineEdit

from Controller import Controller_Utente
import pagina_Login

class BookingDialog(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.date_label = QLabel("Data")
        self.date_input = QDateEdit()

        self.service_label = QLabel("Servizio")
        self.service_input = QLineEdit()

        self.hairdresser_label = QLabel("Parrucchiere")
        self.hairdresser_input = QLineEdit()

        self.confirm_button = QPushButton("Conferma")
        self.confirm_button.clicked.connect(self.confirm_booking)

        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.service_label)
        layout.addWidget(self.service_input)
        layout.addWidget(self.hairdresser_label)
        layout.addWidget(self.hairdresser_input)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def confirm_booking(self):
        # Qui dovresti implementare la logica per confermare la prenotazione
        # Per ora, stampiamo solo un messaggio di conferma
        print("Prenotazione confermata!")


class ProfileDialog(QDialog):
    def __init__(self, username):
        super().__init__()

        self.username = username
        self.user_controller = Controller_Utente.Controller_Utente("C:\\Users\\manue\\PycharmProjects\\pythonProject1\\database.pickle")

        layout = QVBoxLayout()

        self.username_label = QLabel("Username")
        self.username_input = QLineEdit()
        self.username_input.setText(self.username)

        self.password_label = QLabel("Password")
        self.password_input = QLineEdit()

        self.change_button = QPushButton("Cambia")
        self.change_button.clicked.connect(self.change_profile)

        self.delete_button = QPushButton("Cancella")
        self.delete_button.clicked.connect(self.delete_profile)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.change_button)
        layout.addWidget(self.delete_button)

        self.setLayout(layout)

    def change_profile(self):
        new_password = self.password_input.text()
        self.user_controller.update_user(self.username, new_password)
        print("Profilo cambiato con successo!")

    def delete_profile(self):
        self.user_controller.delete_user(self.username)
        print("Profilo cancellato con successo!")
        self.close()

class view_Utente(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.setWindowTitle("User View")

        layout = QVBoxLayout()

        self.greeting_label = QLabel(f"Welcome, {username}!")

        self.group_box = QGroupBox("Opzioni")
        group_layout = QGridLayout()

        self.booking_button = QPushButton("Prenota")
        self.booking_button.clicked.connect(self.book_appointment)

        self.profile_button = QPushButton("Profilo")
        self.profile_button.clicked.connect(self.view_profile)

        group_layout.addWidget(self.booking_button, 0, 0)
        group_layout.addWidget(self.profile_button, 0, 1)

        self.group_box.setLayout(group_layout)

        layout.addWidget(self.greeting_label)
        layout.addWidget(self.group_box)

        self.setLayout(layout)

    def book_appointment(self):
        self.booking_dialog = BookingDialog()
        self.booking_dialog.show()

    def view_profile(self):
        self.profile_dialog = ProfileDialog(self.username)
        self.profile_dialog.show()

