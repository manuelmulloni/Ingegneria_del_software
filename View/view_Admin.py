from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGroupBox, QListWidget, QDialog, QLineEdit, \
    QLabel
from Controller import Controller_Utente, Controller_Prenotazioni
class view_Admin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Admin View')

        self.layout = QVBoxLayout()

        self.group_box = QGroupBox("Admin Actions")
        self.group_layout = QVBoxLayout()

        self.view_profile_button = QPushButton('View Profile')
        self.view_profile_button.clicked.connect(self.view_profile)

        self.view_bookings_button = QPushButton('View Bookings')
        self.view_bookings_button.clicked.connect(self.view_bookings)

        self.delete_bookings_button = QPushButton('Delete Bookings')
        self.delete_bookings_button.clicked.connect(self.delete_bookings)

        self.view_users_button = QPushButton('View Users')
        self.view_users_button.clicked.connect(self.view_users)

        self.delete_users_button = QPushButton('Delete Users')
        self.delete_users_button.clicked.connect(self.delete_users)

        self.group_layout.addWidget(self.view_profile_button)
        self.group_layout.addWidget(self.view_bookings_button)
        self.group_layout.addWidget(self.delete_bookings_button)
        self.group_layout.addWidget(self.view_users_button)
        self.group_layout.addWidget(self.delete_users_button)

        self.group_box.setLayout(self.group_layout)

        self.layout.addWidget(self.group_box)

        self.setLayout(self.layout)

    def view_profile(self):
        self.profile_dialog = QDialog()
        self.profile_dialog.setWindowTitle('Profile Options')

        self.profile_layout = QVBoxLayout()

        self.view_profile_button = QPushButton("View Profile")
        self.view_profile_button.clicked.connect(self.leggi_Profilo)

        self.edit_profile_button = QPushButton("Edit Profile")
        self.edit_profile_button.clicked.connect(self.edit_profile)

        self.delete_profile_button = QPushButton("Delete Profile")
        self.delete_profile_button.clicked.connect(self.delete_user_by_name)

        self.profile_layout.addWidget(self.view_profile_button)
        self.profile_layout.addWidget(self.edit_profile_button)
        self.profile_layout.addWidget(self.delete_profile_button)

        self.profile_dialog.setLayout(self.profile_layout)

        self.profile_dialog.exec()
    def leggi_Profilo(self):
        # Qui puoi aggiungere la logica per leggere il profilo
        print('Read Profile')

    def edit_profile(self):
        # Qui puoi aggiungere la logica per modificare il profilo
        print('Edit Profile')

    def delete_user_by_name(self):
        # Qui puoi aggiungere la logica per eliminare il profilo
        print('Delete Profile')
    def view_bookings(self):
        self.bookings_controller = Controller_Prenotazioni.Controller_Prenotazioni("C:\\Users\\manue\\Documents\\GitHub\\Ingegneria_del_software\\Database\\Prenotazioni.pickle")
        bookings = self.bookings_controller.get_all_bookings()

        self.bookings_dialog = QDialog()
        self.bookings_dialog.setWindowTitle('View Bookings')

        self.bookings_layout = QVBoxLayout()
        self.bookings_list = QListWidget()

        for booking in bookings:
            self.bookings_list.addItem(booking.username + ' ' + booking.date + ' ' + booking.time + ' ' + booking.court + ' ' + booking.duration + ' ' + booking.price + ' ' + booking.payment_status)

        self.bookings_layout.addWidget(self.bookings_list)
        self.bookings_dialog.setLayout(self.bookings_layout)

        self.bookings_dialog.exec()

    def delete_bookings(self):
        self.delete_booking_dialog = QDialog()
        self.delete_booking_dialog.setWindowTitle('Delete Booking')

        self.delete_booking_layout = QVBoxLayout()

        self.username_label = QLabel("Username")
        self.username_input = QLineEdit()

        self.date_label = QLabel("Date")
        self.date_input = QLineEdit()

        self.service_label = QLabel("Service")
        self.service_input = QLineEdit()

        self.delete_booking_button = QPushButton("Delete Booking")
        self.delete_booking_button.clicked.connect(self.delete_booking_by_details)

        self.delete_booking_layout.addWidget(self.username_label)
        self.delete_booking_layout.addWidget(self.username_input)
        self.delete_booking_layout.addWidget(self.date_label)
        self.delete_booking_layout.addWidget(self.date_input)
        self.delete_booking_layout.addWidget(self.service_label)
        self.delete_booking_layout.addWidget(self.service_input)
        self.delete_booking_layout.addWidget(self.delete_booking_button)

        self.delete_booking_dialog.setLayout(self.delete_booking_layout)

        self.delete_booking_dialog.exec()

    def delete_booking_by_details(self):
        username = self.username_input.text()
        date = self.date_input.text()
        service = self.service_input.text()
        self.bookings_controller = Controller_Prenotazioni.Controller_Prenotazioni(
            "C:\\Users\\manue\\Documents\\GitHub\\Ingegneria_del_software\\Database\\Prenotazioni.pickle")
        self.bookings_controller.delete_booking(username, date, service)
        print(f'Booking for user {username} on date {date} for service {service} deleted')



    def view_users(self):
        self.users_controller = Controller_Utente.Controller_Utente("C:\\Users\\manue\\Documents\\GitHub\\Ingegneria_del_software\\Database\\Lista_Utenti.pickle")
        users = self.users_controller.get_all_users()

        self.users_dialog = QDialog()
        self.users_dialog.setWindowTitle('View Users')

        self.users_layout = QVBoxLayout()
        self.users_list = QListWidget()

        for user in users:
            self.users_list.addItem(user.username + ' ' + user.password)

        self.users_layout.addWidget(self.users_list)
        self.users_dialog.setLayout(self.users_layout)

        self.users_dialog.exec()

    def delete_users(self):
        self.delete_user_dialog = QDialog()
        self.delete_user_dialog.setWindowTitle('Delete User')

        self.delete_user_layout = QVBoxLayout()

        self.username_label = QLabel("Username")
        self.username_input = QLineEdit()

        self.delete_user_button = QPushButton("Delete User")
        self.delete_user_button.clicked.connect(self.delete_user_by_name)

        self.delete_user_layout.addWidget(self.username_label)
        self.delete_user_layout.addWidget(self.username_input)
        self.delete_user_layout.addWidget(self.delete_user_button)

        self.delete_user_dialog.setLayout(self.delete_user_layout)

        self.delete_user_dialog.exec()

    def delete_user_by_name(self):
        username = self.username_input.text()
        self.users_controller = Controller_Utente.Controller_Utente(
            "C:\\Users\\manue\\Documents\\GitHub\\Ingegneria_del_software\\Database\\Lista_Utenti.pickle")
        self.users_controller.delete_user(username)
        print(f'User {username} deleted')

if __name__ == '__main__':
    app = QApplication([])
    window = view_Admin()
    window.show()
    app.exec()
