# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'courier.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(627, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textSurname = QtWidgets.QTextEdit(self.centralwidget)
        self.textSurname.setGeometry(QtCore.QRect(140, 140, 104, 51))
        self.textSurname.setObjectName("textSurname")
        self.textPatr = QtWidgets.QTextEdit(self.centralwidget)
        self.textPatr.setGeometry(QtCore.QRect(370, 140, 104, 51))
        self.textPatr.setObjectName("textPatr")
        self.addCourierButton = QtWidgets.QPushButton(self.centralwidget)
        self.addCourierButton.setGeometry(QtCore.QRect(200, 200, 251, 32))
        self.addCourierButton.setObjectName("addCourierButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 110, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 110, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 110, 60, 16))
        self.label_3.setObjectName("label_3")
        self.textName = QtWidgets.QTextEdit(self.centralwidget)
        self.textName.setGeometry(QtCore.QRect(250, 140, 104, 51))
        self.textName.setObjectName("textName")
        self.txtErr = QtWidgets.QLabel(self.centralwidget)
        self.txtErr.setGeometry(QtCore.QRect(90, 240, 471, 31))
        self.txtErr.setText("")
        self.txtErr.setObjectName("txtErr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 24))
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
        self.addCourierButton.setText(_translate("MainWindow", "Добавить курьера"))
        self.label.setText(_translate("MainWindow", "Фамилия"))
        self.label_2.setText(_translate("MainWindow", "Имя"))
        self.label_3.setText(_translate("MainWindow", "Отчество "))