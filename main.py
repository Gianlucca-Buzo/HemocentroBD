from typing import Tuple
from PyQt5 import QtWidgets,QtGui
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTableView
import sys
from database import donor,order
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

    
    def getDoadorForms(self):
        data_doador = self.dateToString(self.entrada_data_doador.text())
        values = donor.create_dictionary((self.entrada_cpf_doador.text(), self.entrada_nome_doador.text(), self.entrada_email_doador.text(), self.box_sexo_doador.currentText(),data_doador,self.box_tiposanguineo_doador.currentText()))
        donor.select_donor(values)
        # donor.insert_donor((self.entrada_cpf_doador.text(), self.entrada_nome_doador.text(), self.entrada_email_doador.text(), self.box_sexo_doador.currentText(),data_doador,self.box_tiposanguineo_doador.currentText()),(self.entrada_cpf_doador.text(),self.entrada_rua_doador.text(), self.entrada_numero_doador.text(),self.entrada_complemento_doador.text()),((self.entrada_cpf_doador.text(), self.entrada_telefone_doador.text()),(self.entrada_cpf_doador.text(),self.entrada_celular_doador.text())))
        # values = donor.create_dictionary((self.entrada_cpf_doador.text(), self.entrada_nome_doador.text(), self.entrada_email_doador.text(), self.box_sexo_doador.currentText(),sale_date.__str__(),self.box_tiposanguineo_doador.currentText()))
        # donor.select_donor(values)
        self.emptyDoadorForms()

    def getDoadorPesquisaForms(self):
        checkboxList = []
        # checkboxList.append(True) if self.checkbox_todos_doador.checkState() else checkboxList.append(False)
        if not self.checkbox_todos_doador.checkState():
            checkboxList.append(False)
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
            checkboxTuple = (True,True,True,True,True,True,True,True,True,True,True)
        pesquisa_data_doador = self.dateToString(self.pesquisa_data_doador.text())
        fields = donor.create_dictionary_fields (checkboxTuple)
        values = donor.create_dictionary((self.pesquisa_cpf_doador.text(), self.pesquisa_nome_doador.text(), self.pesquisa_email_doador.text(), self.pesquisa_box_sexo_doador.currentText(),pesquisa_data_doador,self.pesquisa_box_tiposanguineo_doador.currentText()))
        result = donor.select_donor(fields,values)
        self.displayTable(result)


    def displayTable(self,results):
        self.dialog = TableWindow(self)
        self.dialog.loadData(results)
        self.dialog.show()

            
        
    def getDoacaoForms(self):
        data_doacao = self.dateToString(self.entrada_data_doacao.text())
        print((self.entrada_cpf_doacao.text(),self.entrada_cpf_enfermeiro_doacao.text(),data_doacao,self.entrada_quantidade_doacao.text()))
        self.emptyDoacaoForms()
        self.successMessage("Doação inserida com sucesso")

    def getFuncionarioForms(self):
        data_funcionario = self.dateToString(self.entrada_data_funcionario.text())
        print((self.entrada_cpf_funcionario.text(),self.entrada_nome_funcionario.text(), self.entrada_email_funcionario.text(),self.box_sexo_funcionario.currentText(),data_funcionario,float(self.entrada_salario_funcionario.text()),self.entrada_cargo_funcionario.text()), (self.entrada_cpf_funcionario.text(),self.entrada_rua_funcionario.text(),self.entrada_numero_funcionario.text(),self.entrada_complemento_funcionario.text()),((self.entrada_cpf_funcionario.text(),self.entrada_celular_funcionario.text()),(self.entrada_cpf_funcionario.text(),self.entrada_telefone_funcionario.text())))
        self.emptyFuncionarioForms()

    def getEnfermeiroForms(self):
        data_enfermeiro = self.dateToString(self.entrada_data_enfermeiro.text())
        print((self.entrada_cpf_enfermeiro.text(),self.entrada_nome_enfermeiro.text(), self.entrada_email_enfermeiro.text(),self.box_sexo_enfermeiro.currentText(),data_enfermeiro,float(self.entrada_salario_enfermeiro.text()),self.entrada_coren_enfermeiro.text(),self.entrada_cofen_enfermeiro.text()), (self.entrada_cpf_enfermeiro.text(),self.entrada_rua_enfermeiro.text(),self.entrada_numero_enfermeiro.text(),self.entrada_complemento_enfermeiro.text()),((self.entrada_cpf_enfermeiro.text(),self.entrada_celular_enfermeiro.text()),(self.entrada_cpf_enfermeiro.text(),self.entrada_telefone_enfermeiro.text())))
        self.emptyEnfermeiroForms()

    def getAdminForms(self):
        data_admin = self.dateToString(self.entrada_data_admin.text())
        print((self.entrada_cpf_admin.text(),self.entrada_nome_admin.text(), self.entrada_email_admin.text(),self.box_sexo_admin.currentText(),data_admin,float(self.entrada_salario_admin.text()),self.entrada_usuario_admin.text(),self.entrada_senha_admin.text()), (self.entrada_cpf_admin.text(),self.entrada_rua_admin.text(),self.entrada_numero_admin.text(),self.entrada_complemento_admin.text()),((self.entrada_cpf_admin.text(),self.entrada_celular_admin.text()),(self.entrada_cpf_admin.text(),self.entrada_telefone_admin.text())))
        self.emptyAdminForms()

    def getHospitalForms(self):
        #getHospitalIdByName(self.entrada_nome_admin.text())
        hospitalId = 1
        print((hospitalId, self.entrada_email_hospital.text()), (hospitalId,self.entrada_rua_hospital.text(),self.entrada_numero_hospital.text(),self.entrada_complemento_hospital.text()),((hospitalId,self.entrada_celular_hospital.text()),(hospitalId,self.entrada_telefone_hospital.text())))
        self.emptyHospitalForms()
    
    def getPedidoForms(self):
        orderTuple = order.create_tuple(self.entrada_hospital_pedido.text(),[self.entrada_quantidade_pedido.text(),self.box_tiposanguineo_pedido.currentText()])
        order.insert_order(orderTuple)
        self.emptyPedidoForms()


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
        # self.tableWidget.setColumnWidth(0, 250)
        # self.tableWidget.setColumnWidth(1, 100)
        # self.tableWidget.setColumnWidth(2, 350)
        # self.tableWidget.setHorizontalHeaderLabels(["City","Country","Subcountry"])
        # self.loaddata()

    # def loadData(self,cursor):
    #     num_fields = len(cursor.description)
    #     field_names = [i[0] for i in cursor.description]
    #     model = QtGui.QStandardItemModel()
    #     model.setHorizontalHeaderLabels(field_names)
    #     self.tableView.setModel(model)

    def loadData(self,results):
        data = results[0]
        headers = results[1]
        lenHeaders = len(headers)
        self.tableWidget.setColumnCount(lenHeaders)
        self.tableWidget.setHorizontalHeaderLabels(headers)
        # self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("teste"))
        index = 0
        self.tableWidget.setRowCount(len(data))
        for row in data:
            for column in range(0,lenHeaders):
                value = row[column]
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
