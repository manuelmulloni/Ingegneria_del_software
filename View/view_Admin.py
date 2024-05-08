import PyQt6
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLabel


class view_Admin():

    def __init__(self):
        self.window = QMainWindow()
        self.window.setWindowTitle('Admin')
        self.window.resize(800, 600)

        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setRowCount(5)

        self.table.setHorizontalHeaderLabels(['ID'])
