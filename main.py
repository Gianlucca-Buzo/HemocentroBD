from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from database import donor


class NewWindow(QMainWindow):
    def _init_(self):
        super(QMainWindow, self)._init_()
        loadUi("HemocentroBD/main_window.ui", self)
        self.button_clients_add.clicked.connect(self.getDoadorForms)

    def testebotao(self):
        print("Clicou")

    def getDoadorForms(self):
        donor.insert_donor((self.entrada_cpf_doador.text(), self.entrada_nome_doador.text(), self.entrada_email_doador.text(), self.box_sexo_doador.currentText(),self.entrada_data_doador.text(),self.box_tiposanguineo_doador.currentText()),(self.entrada_cpf_doador.text(),self.entrada_rua_doador.text(), self.entrada_numero_doador.text(),self.entrada_complemento_doador.text()),((self.entrada_cpf_doador.text(), self.entrada_telefone_doador.text()),(self.entrada_cpf_doador.text(),self.entrada_celular_doador.text())))
        # print(, , )
        
def window():
    app = QApplication(sys.argv)
    win = NewWindow()
    win.setFixedWidth(900)
    win.setFixedHeight(550)

    win.show()
    sys.exit(app.exec_())

window()