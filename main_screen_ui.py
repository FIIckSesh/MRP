# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_screen_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1027, 479)
        MainWindow.setStyleSheet("background: #FFFFFF;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(25, 51, 979, 381))
        self.widget.setStyleSheet("position: absolute;\n"
"width: 979px;\n"
"height: 381px;\n"
"left: 25px;\n"
"top: 74px;\n"
"\n"
"background: #CF9292;")
        self.widget.setObjectName("widget")
        self.changedButton = QtWidgets.QPushButton(self.widget)
        self.changedButton.setEnabled(True)
        self.changedButton.setGeometry(QtCore.QRect(650, 70, 321, 46))
        self.changedButton.setStyleSheet("position: absolute;\n"
"width: 299px;\n"
"height: 46px;\n"
"left: 695px;\n"
"top: 93px;\n"
"\n"
"background: #C4C4C4;")
        self.changedButton.setObjectName("changedButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 130, 321, 46))
        self.pushButton_4.setStyleSheet("position: absolute;\n"
"width: 299px;\n"
"height: 45px;\n"
"left: 695px;\n"
"top: 165px;\n"
"\n"
"background: #C4C4C4;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.addButton = QtWidgets.QPushButton(self.widget)
        self.addButton.setGeometry(QtCore.QRect(650, 10, 321, 46))
        self.addButton.setStyleSheet("position: absolute;\n"
"width: 299px;\n"
"height: 46px;\n"
"left: 695px;\n"
"top: 236px;\n"
"\n"
"background: #C4C4C4;")
        self.addButton.setObjectName("addButton")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 632, 361))
        self.tableWidget.setStyleSheet("position: absolute;\n"
"width: 632px;\n"
"height: 344px;\n"
"left: 45px;\n"
"top: 93px;\n"
"\n"
"background: #C4C4C4;")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(25, 20, 304, 23))
        self.comboBox.setStyleSheet("background: #C4C4C4;")
        self.comboBox.setObjectName("comboBox")
        self.directoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.directoryButton.setGeometry(QtCore.QRect(675, 20, 156, 23))
        self.directoryButton.setStyleSheet("position: absolute;\n"
"width: 88px;\n"
"height: 39px;\n"
"left: 801px;\n"
"top: 20px;\n"
"\n"
"background: #C4C4C4;")
        self.directoryButton.setObjectName("directoryButton")
        self.movementButton = QtWidgets.QPushButton(self.centralwidget)
        self.movementButton.setGeometry(QtCore.QRect(840, 20, 156, 23))
        self.movementButton.setStyleSheet("position: absolute;\n"
"width: 88px;\n"
"height: 39px;\n"
"left: 914px;\n"
"top: 20px;\n"
"\n"
"background: #C4C4C4;")
        self.movementButton.setObjectName("movementButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1027, 24))
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
        self.changedButton.setText(_translate("MainWindow", "Редактировать"))
        self.pushButton_4.setText(_translate("MainWindow", "Удалить"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.directoryButton.setText(_translate("MainWindow", "Справочники"))
        self.movementButton.setText(_translate("MainWindow", "Движения"))