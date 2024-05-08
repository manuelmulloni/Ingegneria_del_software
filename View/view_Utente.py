from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QDialog, QDateEdit
from Controller.Controller_Utente import Controller_Utente
from Controller.Controller_Prenotazioni import Controller_Prenotazioni
from Model.Model_Prenotazioni import Model_Prenotazioni
class ReservationDialog(QDialog):
    def __init__(self,username):
        super().__init__()
        self.prenotazioni = Controller_Prenotazioni()
        self.nome = username #dato che ho ilcostruttore con username che ho preso dalla pagina di login do il nome della persona che prenota direttamente
        self.layout = QVBoxLayout()
        self.setGeometry(100, 100, 400, 200)


        self.date_label = QLabel('Data')
        self.date_input = QDateEdit()

        self.parrucchiere_label = QLabel('Parrucchiere')
        self.parrucchiere_input = QComboBox()
        # Aggiungi qui le opzioni per il parrucchiere

        self.taglio_label = QLabel('Servizio')
        self.taglio_input = QComboBox()
        self.taglio_input.addItem('Taglio')
        self.taglio_input.addItem('Colore')
        self.taglio_input.addItem('Piega')

        self.prenota = QPushButton('Prenota')
        self.prenota.clicked.connect(self.inserisci_prenotazione())




        self.layout.addWidget(self.date_label)
        self.layout.addWidget(self.date_input)
        self.layout.addWidget(self.parrucchiere_label)
        self.layout.addWidget(self.parrucchiere_input)
        self.layout.addWidget(self.taglio_label)
        self.layout.addWidget(self.taglio_input)
        self.layout.addWidget(self.prenota)
        self.setLayout(self.layout)

    def inserisci_prenotazione(self):
        data = self.date_input.date().toString('dd/MM/yyyy')
        parrucchiere = self.parrucchiere_input.currentText()
        tipo_taglio = self.taglio_input.currentText()   #scegli nella combo box i ltipo di prenotazione e la inserisce nel file prenotazioni
        prenotazione = Model_Prenotazioni(self.nome, data, parrucchiere, tipo_taglio)
        dict_prenotazione = prenotazione.get_Prenotazioni()
        self.prenotazioni.insert(dict_prenotazione)

class view_Utente(QWidget):
    def __init__(self, username):
        super().__init__()
        self.controller_utente = Controller_Utente()
        self.username = username

        self.setWindowTitle('User Page')
        self.layout = QVBoxLayout()

        self.menu = QComboBox()
        self.menu.addItem('Profilo')
        self.menu.addItem('Prenotazione')
        self.menu.currentIndexChanged.connect(self.selectionchange)

        self.layout.addWidget(self.menu)

        self.setLayout(self.layout)

    def selectionchange(self, i):
        if self.menu.currentText() == 'Profilo':
            self.show_profilo()
        elif self.menu.currentText() == 'Prenotazione':
            self.make_reservation()

    def show_profilo(self):
        # Here you can add the logic to show the user profile
        print('Showing user profile')

    def make_reservation(self,username):
        # Here you can add the logic to make a reservation
        print('Making a reservation')
        self.reservation_dialog = ReservationDialog(username) #inserisco un parametro username quando faccio la prenotazione
        self.reservation_dialog.exec()
