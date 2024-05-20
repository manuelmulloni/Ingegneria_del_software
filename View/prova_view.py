from PyQt6.QtCore import QFile
from PyQt6.QtWidgets import QMessageBox

import file_ui
import sys
from PyQt6 import QtWidgets, uic

class prova_view(QtWidgets.QWidget):
    def __init__(self):
        super(prova_view, self).__init__()
        uic.loadUi("C:\\Users\\manue\\Documents\\GitHub\\Ingegneria_del_software\\file_ui\\viewAdmin.ui", self)
        # Carica il file .ui creato con qt designer


        # Connetti i pulsanti ai metodi appropriati
        self.VediUtenti.clicked.connect(self.view_users) # button di visualizzazione utenti
        self.pushButton_2.clicked.connect(self.view_bookings) # button di visualizzazione prenotazioni
        self.pushButton_3.clicked.connect(self.delete_user) # button di cancellazione utente
        self.pushButton_4.clicked.connect(self.delete_booking) # button di cancellazione prenotazione
        self.comboBox.addItem("Vedi Parruchieri") #elementi della combobox
        self.comboBox.addItem("Aggiungi Parrucchiere")
        self.comboBox.addItem("Elimina Parrucchiere")
        self.comboBox_2.addItem("Vedi Profilo") #elementi della combobox 2
        self.comboBox_2.addItem("Modifica Profilo")

        self.comboBox.currentIndexChanged.connect(self.indirizzo_selezionato) #connetti la combobox al metodo
        self.comboBox_2.currentIndexChanged.connect(self.indirizzo_selezionato_2)

    def indirizzo_selezionato(self,index): #metodo per la selezione della combobox in base all'indirizzo ricevuto
        if index == 0:
            self.vedi_parrucchiere()
        elif index == 1:
            self.aggiungi_parrucchiere()
        elif index == 2:
            self.elimina_parrucchiere()


    def indirizzo_selezionato_2(self,index): #metodo per la selezione della combobox 2 in base all'indirizzo ricevuto
          if index == 0:
                self.vedi_profilo()
          elif index == 1:
             self.modifica_profilo()

    def view_users(self):
        # Implementa la logica per visualizzare gli utenti
        QMessageBox.information(self, "Info", "Visualizza Utenti")

    def view_bookings(self):
        # Implementa la logica per visualizzare le prenotazioni
        QMessageBox.information(self, "Info", "Visualizza Prenotazioni")

    def delete_user(self):
        # Implementa la logica per cancellare un utente
        QMessageBox.information(self, "Info", "Cancella Utente")

    def delete_booking(self):
        # Implementa la logica per cancellare una prenotazione
        QMessageBox.information(self, "Info", "Cancella Prenotazioni")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = prova_view()
    window.show()
    sys.exit(app.exec())