from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from database import donor
from datetime import date


class NewWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        loadUi("main_window.ui", self)
        self.button_clients_add.clicked.connect(self.getDoadorForms)

    def testebotao(self):
        print("Clicou")

    def getDoadorForms(self):
        sale_date = self.entrada_data_doador.text().split("/")
        sale_date = date(int(sale_date[2]),int(sale_date[1]),int(sale_date[0]))
        donor.insert_donor((self.entrada_cpf_doador.text(), self.entrada_nome_doador.text(), self.entrada_email_doador.text(), self.box_sexo_doador.currentText(),sale_date.__str__(),self.box_tiposanguineo_doador.currentText()),(self.entrada_cpf_doador.text(),self.entrada_rua_doador.text(), self.entrada_numero_doador.text(),self.entrada_complemento_doador.text()),((self.entrada_cpf_doador.text(), self.entrada_telefone_doador.text()),(self.entrada_cpf_doador.text(),self.entrada_celular_doador.text())))
        self.emptyDoadorForms()

    def emptyDoadorForms(self):
        self.entrada_cpf_doador.clear()
        self.entrada_nome_doador.clear()
        self.entrada_email_doador.clear()
        self.entrada_data_doador.clear()
        self.box_sexo_doador.clear()
        self.box_tiposanguineo_doador.clear()
        self.entrada_rua_doador.clear()
        self.entrada_numero_doador.clear()
        self.entrada_complemento_doador.clear()
        self.entrada_telefone_doador.clear()
        self.entrada_celular_doador.clear()
        
        
def window():
    app = QApplication(sys.argv)
    win = NewWindow()
    win.setFixedWidth(900)
    win.setFixedHeight(550)

    win.show()
    sys.exit(app.exec_())

window()