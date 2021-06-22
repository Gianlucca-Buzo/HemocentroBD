from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class NewWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        loadUi("HemocentroBD/untitled.ui", self)

def window():
    app = QApplication(sys.argv)
    win = NewWindow()
    win.setGeometry(100,200,300,300)

    win.show()
    sys.exit(app.exec_())

window()