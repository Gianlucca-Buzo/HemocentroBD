from typing import Tuple
from PyQt5 import QtWidgets,QtGui
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTableView
import sys
from database import donor,order,donation,employee,stock,transaction,hospital
from datetime import date


class NewWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        loadUi("HemocentroBD/main_window.ui", self)
        self.botao_adicionar_doador.clicked.connect(self.getDoadorForms)
        self.botao_adicionar_doacao.clicked.connect(self.getDoacaoForms)
        self.botao_adicionar_funcionario.clicked.connect(self.getFuncionarioForms)
        self.botao_adicionar_enfermeiro.clicked.connect(self.getEnfermeiroForms)
        self.botao_adicionar_admin.clicked.connect(self.getAdminForms)
        self.botao_adicionar_hospital.clicked.connect(self.getHospitalForms)
        self.botao_adicionar_pedido.clicked.connect(self.getPedidoForms)
        self.botao_pesquisar_doador.clicked.connect(self.getDoadorPesquisaForms)
        self.botao_pesquisar_doacao.clicked.connect(self.getDoacaoPesquisaForms)
        self.botao_pesquisar_funcionario.clicked.connect(self.getFuncionarioPesquisaForms)
        self.botao_pesquisar_hospital.clicked.connect(self.getHospitalPesquisaForms)
        self.botao_pesquisar_pedido.clicked.connect(self.getPedidoPesquisaForms)

    def getDoadorPesquisaForms(self):
        checkboxList = []
        # checkboxList.append(True) if self.checkbox_todos_doador.checkState() else checkboxList.append(False)
        if not self.checkbox_todos_doador.checkState():
            checkboxList.append(True) if self.checkbox_cpf_doador.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_nome_doador.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_email_doador.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_sexo_doador.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_data_doador.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_tiposanguineo_doador.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_telefone_doador.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_rua_doador.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_numero_doador.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_complemento_doador.checkState() else checkboxList.append(False)
            checkboxTuple = tuple(checkboxList)
        else:
            checkboxTuple = (True,True,True,True,True,True,True,True,True,True)
        pesquisa_data_doador = self.dateToString(self.pesquisa_data_doador.text())
        fields = donor.create_dictionary_fields (checkboxTuple)
        values = donor.create_dictionary((self.pesquisa_cpf_doador.text(), self.pesquisa_nome_doador.text(), self.pesquisa_email_doador.text(), self.pesquisa_box_sexo_doador.currentText(),pesquisa_data_doador,self.pesquisa_box_tiposanguineo_doador.currentText()))
        result = donor.select_donor(fields,values)
        self.displayTable(result)

    def getDoacaoPesquisaForms(self):
        checkboxList = []

        if not self.checkbox_todos_doacao.checkState():
            checkboxList.append(True) if self.checkbox_cpf_doador_doacao.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_cpf_enfermeiro_doacao.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_data_doacao.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_quantidade_doacao.checkState() else checkboxList.append(False)
            checkboxTuple = tuple(checkboxList)
        else:
            checkboxTuple = (True,True,True,True)
        fields = donation.create_dictionary_fields (checkboxTuple)
        values = donation.create_dictionary((self.pesquisa_cpf_doador_doacao.text(), self.pesquisa_cpf_enfermeiro_doacao.text(), self.pesquisa_data_doacao.text(), self.pesquisa_quantidade_doacao.text()))
        result = donation.select_donation(fields,values)
        self.displayTable(result)

    def getFuncionarioPesquisaForms(self):
        checkboxList = []
        if not self.checkbox_todos_funcionario.checkState():
            checkboxList.append(True) if self.checkbox_cpf_funcionario.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_nome_funcionario.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_email_funcionario.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_sexo_funcionario.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_data_funcionario.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_salario_funcionario.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_cargo_funcionario.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_coren_funcionario.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_cofen_funcionario.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_telefone_funcionario.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_rua_funcionario.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_numero_funcionario.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_complemento_funcionario.checkState() else checkboxList.append(False)
            checkboxTuple = tuple(checkboxList)
        else:
            checkboxTuple = (True,True,True,True,True,True,True,True,True,True,True,True,True)
        pesquisa_data_funcionario = self.dateToString(self.pesquisa_data_funcionario.text())
        fields = employee.create_dictionary_fields (checkboxTuple)
        values = employee.create_dictionary((self.pesquisa_cpf_funcionario.text(), self.pesquisa_nome_funcionario.text(), self.pesquisa_email_funcionario.text(), self.pesquisa_box_sexo_funcionario.currentText(),pesquisa_data_funcionario,self.pesquisa_salario_funcionario.text(),self.pesquisa_cargo_funcionario.text()))
        result = employee.select_employee(fields,values)
        self.displayTable(result)


    def getHospitalPesquisaForms(self):
        checkboxList = []
        if not self.checkbox_todos_hospital.checkState():
            checkboxList.append(True) if self.checkbox_nome_hospital.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_email_hospital.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_telefone_hospital.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_rua_hospital.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_numero_hospital.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_complemento_hospital.checkState() else checkboxList.append(False)
            checkboxTuple = tuple(checkboxList)
        else:
            checkboxTuple = (True,True,True,True,True,True)
        print(checkboxTuple)
        fields = hospital.create_dictionary_fields (checkboxTuple)
        print(f"fields = {fields}")
        values = hospital.create_dictionary((self.pesquisa_nome_hospital.text(), self.pesquisa_email_hospital.text()))
        result = hospital.select_hospital(fields,values)
        self.displayTable(result)

    def getPedidoPesquisaForms(self):
        checkboxList = []
        # checkboxList.append(True) if self.checkbox_todos_doador.checkState() else checkboxList.append(False)
        if not self.checkbox_todos_pedido.checkState():
            checkboxList.append(True) if self.checkbox_nome_pedido.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_quantidade_pedido.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_tiposanguineo_pedido.checkState() else checkboxList.append(False)
            checkboxList.append(True) if self.checkbox_data_pedido.checkState() else checkboxList.append(False)
            checkboxTuple = tuple(checkboxList)
        else:
            checkboxTuple = (True,True,True,True,True,True,True,True,True,True)
        pesquisa_data_pedido = self.dateToString(self.pesquisa_data_pedido.text())
        fields = order.create_dictionary_fields (checkboxTuple)
        values = order.create_dictionary((self.pesquisa_nome_pedido.text(),self.pesquisa_quantidade_pedido.text(),self.pesquisa_box_tiposanguineo_pedido.currentText(),pesquisa_data_pedido))
        result = order.select_order(fields,values)
        self.displayTable(result)
            


    def displayTable(self,results):
        self.dialog = TableWindow(self)
        self.dialog.loadData(results)
        self.dialog.show()

############################################################# INSERCOES ###################################################################################

    def getDoadorForms(self):
        data_doador = self.dateToString(self.entrada_data_doador.text())
        donor.insert_donor((self.entrada_cpf_doador.text(), self.entrada_nome_doador.text(), self.entrada_email_doador.text(), self.box_sexo_doador.currentText(),data_doador,self.box_tiposanguineo_doador.currentText()),(self.entrada_cpf_doador.text(),self.entrada_rua_doador.text(), self.entrada_numero_doador.text(),self.entrada_complemento_doador.text()),((self.entrada_cpf_doador.text(), self.entrada_telefone_doador.text()),(self.entrada_cpf_doador.text(),self.entrada_celular_doador.text())))
        self.emptyDoadorForms()
        self.successMessage("Doador inserido com sucesso")    
        
    def getDoacaoForms(self):
        data_doacao = self.dateToString(self.entrada_data_doacao.text())
        donation.insert_donation((self.entrada_cpf_doacao.text(),self.entrada_cpf_enfermeiro_doacao.text(),data_doacao,self.entrada_quantidade_doacao.text()))
        self.emptyDoacaoForms()
        self.successMessage("Doação inserida com sucesso")

    def getFuncionarioForms(self):
        data_funcionario = self.dateToString(self.entrada_data_funcionario.text())
        employee.insert_employee((self.entrada_cpf_funcionario.text(),self.entrada_nome_funcionario.text(), self.entrada_email_funcionario.text(),self.box_sexo_funcionario.currentText(),data_funcionario,float(self.entrada_salario_funcionario.text()),self.entrada_cargo_funcionario.text()), (self.entrada_cpf_funcionario.text(),self.entrada_rua_funcionario.text(),self.entrada_numero_funcionario.text(),self.entrada_complemento_funcionario.text()),((self.entrada_cpf_funcionario.text(),self.entrada_celular_funcionario.text()),(self.entrada_cpf_funcionario.text(),self.entrada_telefone_funcionario.text())))
        self.emptyFuncionarioForms()
        self.successMessage("Funcionário inserido com sucesso")

    def getEnfermeiroForms(self):
        data_enfermeiro = self.dateToString(self.entrada_data_enfermeiro.text())
        employee.insert_nurse((self.entrada_cpf_enfermeiro.text(),self.entrada_nome_enfermeiro.text(), self.entrada_email_enfermeiro.text(),self.box_sexo_enfermeiro.currentText(),data_enfermeiro,float(self.entrada_salario_enfermeiro.text())),(self.entrada_cpf_enfermeiro.text(),self.entrada_coren_enfermeiro.text(),self.entrada_cofen_enfermeiro.text()), (self.entrada_cpf_enfermeiro.text(),self.entrada_rua_enfermeiro.text(),self.entrada_numero_enfermeiro.text(),self.entrada_complemento_enfermeiro.text()),((self.entrada_cpf_enfermeiro.text(),self.entrada_celular_enfermeiro.text()),(self.entrada_cpf_enfermeiro.text(),self.entrada_telefone_enfermeiro.text())))
        self.emptyEnfermeiroForms()
        self.successMessage("Enfermeiro inserido com sucesso")

    def getAdminForms(self):
        data_admin = self.dateToString(self.entrada_data_admin.text())
        employee.insert_manager((self.entrada_cpf_admin.text(),self.entrada_nome_admin.text(), self.entrada_email_admin.text(),self.box_sexo_admin.currentText(),data_admin,float(self.entrada_salario_admin.text())),(self.entrada_cpf_admin.text(),self.entrada_usuario_admin.text(),self.entrada_senha_admin.text()), (self.entrada_cpf_admin.text(),self.entrada_rua_admin.text(),self.entrada_numero_admin.text(),self.entrada_complemento_admin.text()),((self.entrada_cpf_admin.text(),self.entrada_celular_admin.text()),(self.entrada_cpf_admin.text(),self.entrada_telefone_admin.text())))
        self.emptyAdminForms()
        self.successMessage("Administrador inserido com sucesso")

    def getHospitalForms(self):
        hospital.insert_hospital((self.entrada_nome_hospital.text(),self.entrada_email_hospital.text()), [self.entrada_rua_hospital.text(),self.entrada_numero_hospital.text(),self.entrada_complemento_hospital.text()],([self.entrada_celular_hospital.text()],[self.entrada_telefone_hospital.text()]))
        self.emptyHospitalForms()
        self.successMessage("Hospital inserido com sucesso")
    
    def getPedidoForms(self):
        orderTuple = order.create_tuple(self.entrada_hospital_pedido.text(),[self.entrada_quantidade_pedido.text(),self.box_tiposanguineo_pedido.currentText()])
        order.insert_order(orderTuple)
        self.emptyPedidoForms()
        self.successMessage("Pedido inserido com sucesso")


############################################################# LIMPA OS CAMPOS ###################################################################################

    def emptyDoadorForms(self):
        self.entrada_cpf_doador .clear()
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

    def emptyDoacaoForms(self):
        self.entrada_cpf_doacao.clear()
        self.entrada_cpf_enfermeiro_doacao.clear()
        self.entrada_data_doacao.clear()
        self.entrada_quantidade_doacao.clear()

    def emptyFuncionarioForms(self):
        self.entrada_cpf_funcionario.clear()
        self.entrada_nome_funcionario.clear()
        self.entrada_email_funcionario.clear()
        self.box_sexo_funcionario.clear()
        self.entrada_data_funcionario.clear()
        self.entrada_salario_funcionario.clear()
        self.entrada_cargo_funcionario.clear()
        self.entrada_celular_funcionario.clear()
        self.entrada_telefone_funcionario.clear()
        self.entrada_rua_funcionario.clear()
        self.entrada_numero_funcionario.clear()
        self.entrada_complemento_funcionario.clear()

    def emptyEnfermeiroForms(self):
        self.entrada_cpf_enfermeiro.clear()
        self.entrada_nome_enfermeiro.clear()
        self.entrada_email_enfermeiro.clear()
        self.box_sexo_enfermeiro.clear()
        self.entrada_data_enfermeiro.clear()
        self.entrada_salario_enfermeiro.clear()
        self.entrada_coren_enfermeiro.clear()
        self.entrada_cofen_enfermeiro.clear()
        self.entrada_celular_enfermeiro.clear()
        self.entrada_telefone_enfermeiro.clear()
        self.entrada_rua_enfermeiro.clear()
        self.entrada_numero_enfermeiro.clear()
        self.entrada_complemento_enfermeiro.clear()

    def emptyAdminForms(self):
        self.entrada_cpf_admin.clear()
        self.entrada_nome_admin.clear()
        self.entrada_email_admin.clear()
        self.box_sexo_admin.clear()
        self.entrada_data_admin.clear()
        self.entrada_salario_admin.clear()
        self.entrada_usuario_admin.clear()
        self.entrada_senha_admin.clear()
        self.entrada_celular_admin.clear()
        self.entrada_telefone_admin.clear()
        self.entrada_rua_admin.clear()
        self.entrada_numero_admin.clear()
        self.entrada_complemento_admin.clear()

    def emptyHospitalForms(self):
        self.entrada_nome_hospital.clear()
        self.entrada_email_hospital.clear()
        self.entrada_celular_hospital.clear()
        self.entrada_telefone_hospital.clear()
        self.entrada_rua_hospital.clear()
        self.entrada_numero_hospital.clear()
        self.entrada_complemento_hospital.clear()

    def emptyPedidoForms(self):
        self.entrada_hospital_pedido.clear()
        self.entrada_quantidade_pedido.clear()
        self.box_tiposanguineo_pedido.clear()


##############################################################################################################################################################

    def dateToString(self,dateTime):
        if dateTime != None:
            if dateTime != '':
                sale_date = dateTime.split("/")
                sale_date = date(int(sale_date[2]),int(sale_date[1]),int(sale_date[0]))
                return sale_date.__str__()
        return ''

    def successMessage(self,message):
        success_message = QtWidgets.QMessageBox()
        success_message.setIcon(QtWidgets.QMessageBox.Information)
        success_message.setText(message)
        success_message.setWindowTitle("Sucesso")
        success_message.addButton(QtWidgets.QMessageBox.Ok)
        success_message.exec_()

    def errorMessage(self,message):
        error_message = QtWidgets.QMessageBox()
        error_message.setIcon(QtWidgets.QMessageBox.Critical)
        error_message.setText(message)
        error_message.setWindowTitle("Erro")
        error_message.addButton(QtWidgets.QMessageBox.Ok)
        error_message.exec_()
        

class TableWindow(QDialog):
    def __init__(self, parent= None):
        super(QDialog, self).__init__(parent)
        loadUi("HemocentroBD/table2.ui",self)


    def loadData(self,results):
        data = results[0]
        headers = results[1]
        lenHeaders = len(headers)
        self.tableWidget.setColumnCount(lenHeaders)
        self.tableWidget.setHorizontalHeaderLabels(headers)
        index = 0
        self.tableWidget.setRowCount(len(data))
        for row in data:
            for column in range(0,lenHeaders):
                self.tableWidget.setItem(index,column,QtWidgets.QTableWidgetItem(row[column].__str__()))
            index += 1


app = QApplication(sys.argv)
win = NewWindow()
# widget = QtWidgets.QStackedWidget()
# widget.addWidget(win)

win.setFixedWidth(900)
win.setFixedHeight(550)

win.show()
sys.exit(app.exec_())
