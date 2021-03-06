# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/worker.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(399, 429)
        MainWindow.setStyleSheet("background: #5585B5;\n"
"padding: 0;\n"
"    margin: 0;\n"
"    font-family: \'Open Sans\', sans-serif;\n"
"    font-size: 14px;\n"
"    color: #1D2734;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textSurname = QtWidgets.QTextEdit(self.centralwidget)
        self.textSurname.setGeometry(QtCore.QRect(140, 100, 181, 51))
        self.textSurname.setStyleSheet("width: 100%;\n"
"    outline: none;\n"
"    border: 1px solid #DCDEE1;\n"
"    border-radius: 4px;\n"
"    color: #1D2734;\n"
"    padding-left: 16px;\n"
"    box-sizing: border-box;\n"
"    -webkit-appearance: none;")
        self.textSurname.setObjectName("textSurname")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 110, 60, 16))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 31, 16))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 71, 16))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.textName = QtWidgets.QTextEdit(self.centralwidget)
        self.textName.setGeometry(QtCore.QRect(140, 40, 181, 51))
        self.textName.setStyleSheet("width: 100%;\n"
"    outline: none;\n"
"    border: 1px solid #DCDEE1;\n"
"    border-radius: 4px;\n"
"    color: #1D2734;\n"
"    padding-left: 16px;\n"
"    box-sizing: border-box;\n"
"    -webkit-appearance: none;")
        self.textName.setObjectName("textName")
        self.textPatr = QtWidgets.QTextEdit(self.centralwidget)
        self.textPatr.setGeometry(QtCore.QRect(140, 160, 181, 51))
        self.textPatr.setStyleSheet("width: 100%;\n"
"    outline: none;\n"
"    border: 1px solid #DCDEE1;\n"
"    border-radius: 4px;\n"
"    color: #1D2734;\n"
"    padding-left: 16px;\n"
"    box-sizing: border-box;\n"
"    -webkit-appearance: none;")
        self.textPatr.setObjectName("textPatr")
        self.addWorkerButton = QtWidgets.QPushButton(self.centralwidget)
        self.addWorkerButton.setGeometry(QtCore.QRect(70, 320, 261, 32))
        self.addWorkerButton.setStyleSheet("border: 2px solid;\n"
"border-radius: 4px;\n"
"box-sizing: border-box;\n"
"cursor: pointer;\n"
"outline: none;\n"
"position: relative;\n"
"transition: 0.3s;\n"
"font-weight: 600;\n"
"vertical-align: middle;\n"
"background: #F27171;")
        self.addWorkerButton.setObjectName("addWorkerButton")
        self.txtErr = QtWidgets.QLabel(self.centralwidget)
        self.txtErr.setGeometry(QtCore.QRect(90, 280, 221, 20))
        self.txtErr.setText("")
        self.txtErr.setObjectName("txtErr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 19))
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
        self.label.setText(_translate("MainWindow", "Фамилия"))
        self.label_2.setText(_translate("MainWindow", "Имя"))
        self.label_3.setText(_translate("MainWindow", "Отчество "))
        self.addWorkerButton.setText(_translate("MainWindow", "Добавить сотрудника"))
