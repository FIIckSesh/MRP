# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clients.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textSurname = QtWidgets.QTextEdit(self.centralwidget)
        self.textSurname.setGeometry(QtCore.QRect(130, 60, 161, 41))
        self.textSurname.setObjectName("textSurname")
        self.textPatr = QtWidgets.QTextEdit(self.centralwidget)
        self.textPatr.setGeometry(QtCore.QRect(130, 110, 161, 41))
        self.textPatr.setObjectName("textPatr")
        self.addClientButton = QtWidgets.QPushButton(self.centralwidget)
        self.addClientButton.setGeometry(QtCore.QRect(80, 320, 251, 32))
        self.addClientButton.setObjectName("addClientButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 70, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 20, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 120, 60, 16))
        self.label_3.setObjectName("label_3")
        self.textName = QtWidgets.QTextEdit(self.centralwidget)
        self.textName.setGeometry(QtCore.QRect(130, 10, 161, 41))
        self.textName.setObjectName("textName")
        self.textStreet = QtWidgets.QTextEdit(self.centralwidget)
        self.textStreet.setGeometry(QtCore.QRect(130, 160, 161, 41))
        self.textStreet.setObjectName("textStreet")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 60, 16))
        self.label_4.setObjectName("label_4")
        self.textHouse = QtWidgets.QTextEdit(self.centralwidget)
        self.textHouse.setGeometry(QtCore.QRect(130, 210, 161, 41))
        self.textHouse.setObjectName("textHouse")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 220, 60, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 270, 60, 16))
        self.label_6.setObjectName("label_6")
        self.textNumber = QtWidgets.QTextEdit(self.centralwidget)
        self.textNumber.setGeometry(QtCore.QRect(130, 260, 161, 41))
        self.textNumber.setObjectName("textNumber")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addClientButton.setText(_translate("MainWindow", "Добавить клиента"))
        self.label.setText(_translate("MainWindow", "Фамилия"))
        self.label_2.setText(_translate("MainWindow", "Имя"))
        self.label_3.setText(_translate("MainWindow", "Отчество "))
        self.label_4.setText(_translate("MainWindow", "Улица"))
        self.label_5.setText(_translate("MainWindow", "Дом"))
        self.label_6.setText(_translate("MainWindow", "Телефон"))
