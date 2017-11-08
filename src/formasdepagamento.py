# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\formasdepagamento.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from conexao import Conexao

class Ui_FormasDePagamento(object):
    def setupUi(self, FormasDePagamento):
        FormasDePagamento.setObjectName("FormasDePagamento")
        FormasDePagamento.setWindowModality(QtCore.Qt.WindowModal)
        FormasDePagamento.resize(640, 480)
        self.pBIncluir = QtWidgets.QPushButton(FormasDePagamento)
        self.pBIncluir.setGeometry(QtCore.QRect(10, 450, 75, 23))
        self.pBIncluir.setObjectName("pBIncluir")
        self.pBEditar = QtWidgets.QPushButton(FormasDePagamento)
        self.pBEditar.setGeometry(QtCore.QRect(90, 450, 75, 23))
        self.pBEditar.setObjectName("pBEditar")
        self.pBEditar.setEnabled(False)
        self.pBExcluir = QtWidgets.QPushButton(FormasDePagamento)
        self.pBExcluir.setGeometry(QtCore.QRect(170, 450, 75, 23))
        self.pBExcluir.setObjectName("pBExcluir")
        self.pBExcluir.setEnabled(False)
        self.pBSair = QtWidgets.QPushButton(FormasDePagamento)
        self.pBSair.setGeometry(QtCore.QRect(250, 450, 75, 23))
        self.pBSair.setObjectName("pBSair")
        self.tableFormaDePagamento = QtWidgets.QTableWidget(FormasDePagamento)
        self.tableFormaDePagamento.setGeometry(QtCore.QRect(10, 11, 621, 431))
        self.tableFormaDePagamento.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableFormaDePagamento.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableFormaDePagamento.setAlternatingRowColors(True)
        self.tableFormaDePagamento.setColumnCount(2)
        self.tableFormaDePagamento.setObjectName("tableFormaDePagamento")
        self.tableFormaDePagamento.setRowCount(0)
        self.tableFormaDePagamento.verticalHeader().setVisible(False)
        self.tableFormaDePagamento.verticalHeader().setHighlightSections(False)

        self.retranslateUi(FormasDePagamento)
        QtCore.QMetaObject.connectSlotsByName(FormasDePagamento)

        self.pBSair.clicked.connect(FormasDePagamento.close)

        self.MontaGrid()
        self.PopulaGrid()

    def retranslateUi(self, FormasDePagamento):
        _translate = QtCore.QCoreApplication.translate
        FormasDePagamento.setWindowTitle(_translate("FormasDePagamento", "Formas de Pagamento"))
        self.pBIncluir.setText(_translate("FormasDePagamento", "Incluir"))
        self.pBEditar.setText(_translate("FormasDePagamento", "Editar"))
        self.pBExcluir.setText(_translate("FormasDePagamento", "Excluir"))
        self.pBSair.setText(_translate("FormasDePagamento", "Sair"))

    def MontaGrid(self):

        fontHeader = QtGui.QFont()
        fontHeader.setBold(True)
        fontHeader.setFamily("Arial")

        fontGrid = QtGui.QFont()
        fontGrid.setFamily("Arial")

        self.tableFormaDePagamento.horizontalHeader().setFont(fontHeader)
        self.tableFormaDePagamento.setHorizontalHeaderLabels(["Código", "Forma de Pagamento"])
        self.tableFormaDePagamento.setAlternatingRowColors(1)  # Alternar Cores do Grid
        self.tableFormaDePagamento.setSelectionBehavior(QtWidgets.QTableView.SelectRows)  # Selecionar uma linha inteira
        self.tableFormaDePagamento.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)  # Definir o tamanho máximo do grid
        self.tableFormaDePagamento.setFont(fontGrid)

    def PopulaGrid(self):
        conn = Conexao()
        a = conn.ExecutaConsultaTodos("SELECT * FROM forma_de_pagamento")

        self.tableFormaDePagamento.setRowCount(len(a))

        for x, y in enumerate(a):
            self.tableFormaDePagamento.setItem(x, 0, QTableWidgetItem(str(y[0])))
            self.tableFormaDePagamento.setItem(x, 1, QTableWidgetItem(y[1]))

        conn.FechaConexao()

        self.tableFormaDePagamento.doubleClicked.connect(self.CapturaCodigo)

    def CapturaCodigo(self):
        a = []
        for currentQTableWidgetItem in self.tableFormaDePagamento.selectedItems():
            a.append(currentQTableWidgetItem.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormasDePagamento = QtWidgets.QDialog()
    ui = Ui_FormasDePagamento()
    ui.setupUi(FormasDePagamento)
    FormasDePagamento.show()
    sys.exit(app.exec_())


