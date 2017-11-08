# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sistemafinanceiro.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from formasdepagamento import  Ui_FormasDePagamento

class Ui_MainWindow_Financeiro(object):
    def setupUi(self, MainWindow_Financeiro):
        MainWindow_Financeiro.setObjectName("MainWindow_Financeiro")
        MainWindow_Financeiro.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow_Financeiro)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow_Financeiro.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_Financeiro)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuExibir = QtWidgets.QMenu(self.menubar)
        self.menuExibir.setObjectName("menuExibir")
        self.menuGerenciar = QtWidgets.QMenu(self.menubar)
        self.menuGerenciar.setObjectName("menuGerenciar")
        MainWindow_Financeiro.setMenuBar(self.menubar)
        self.actionContas = QtWidgets.QAction(MainWindow_Financeiro)
        self.actionContas.setObjectName("actionContas")
        self.actionFormas_de_Pagamento = QtWidgets.QAction(MainWindow_Financeiro)
        self.actionFormas_de_Pagamento.setObjectName("actionFormas_de_Pagamento")
        self.menuGerenciar.addAction(self.actionContas)
        self.menuGerenciar.addAction(self.actionFormas_de_Pagamento)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuExibir.menuAction())
        self.menubar.addAction(self.menuGerenciar.menuAction())

        self.retranslateUi(MainWindow_Financeiro)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Financeiro)

        self.actionFormas_de_Pagamento.triggered.connect(self.FormasDePagamento)

    def FormasDePagamento(self):
        self.actionFormas_de_Pagamento.setEnabled(False)
        FP_Window = QtWidgets.QDialog()
        u = Ui_FormasDePagamento()
        u.setupUi(FP_Window)
        FP_Window.exec_()
        self.actionFormas_de_Pagamento.setEnabled(True)

    def retranslateUi(self, MainWindow_Financeiro):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Financeiro.setWindowTitle(_translate("MainWindow_Financeiro", "MainWindow"))
        self.menuArquivo.setTitle(_translate("MainWindow_Financeiro", "Arquivo"))
        self.menuEditar.setTitle(_translate("MainWindow_Financeiro", "Editar"))
        self.menuExibir.setTitle(_translate("MainWindow_Financeiro", "Exibir"))
        self.menuGerenciar.setTitle(_translate("MainWindow_Financeiro", "Gerenciar"))
        self.actionContas.setText(_translate("MainWindow_Financeiro", "Contas"))
        self.actionFormas_de_Pagamento.setText(_translate("MainWindow_Financeiro", "Formas de Pagamento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Financeiro = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Financeiro()
    ui.setupUi(MainWindow_Financeiro)
    MainWindow_Financeiro.show()
    sys.exit(app.exec_())

