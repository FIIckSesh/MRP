# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\balance.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 108)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #Наимевание продукции
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lName = QtWidgets.QLabel(self.centralwidget)
        self.lName.setAlignment(QtCore.Qt.AlignCenter)
        self.lName.setObjectName("lName")

        self.verticalLayout.addWidget(self.lName)
        self.name = QtWidgets.QComboBox(self.centralwidget)
        self.initProductComboBox()
        self.name.setCurrentIndex(-1)

        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        #Производитель
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lProducer = QtWidgets.QLabel(self.centralwidget)
        self.lProducer.setAlignment(QtCore.Qt.AlignCenter)
        self.lProducer.setObjectName("lProducer")
        self.verticalLayout_2.addWidget(self.lProducer)
        self.producer = QtWidgets.QLineEdit(self.centralwidget)
        self.producer.setObjectName("producer")
        self.producer.setReadOnly(True)
        self.verticalLayout_2.addWidget(self.producer)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        #Количество
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lAmount = QtWidgets.QLabel(self.centralwidget)
        self.lAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.lAmount.setObjectName("lAmount")
        self.verticalLayout_3.addWidget(self.lAmount)
        self.amount = QtWidgets.QLineEdit(self.centralwidget)
        self.amount.setObjectName("amount")
        self.verticalLayout_3.addWidget(self.amount)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        #Единицы измерения
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lMeasurment = QtWidgets.QLabel(self.centralwidget)
        self.lMeasurment.setAlignment(QtCore.Qt.AlignCenter)
        self.lMeasurment.setObjectName("lMeasurment")
        self.verticalLayout_4.addWidget(self.lMeasurment)
        self.measurment = QtWidgets.QLineEdit(self.centralwidget)
        self.measurment.setObjectName("measurment")
        self.measurment.setReadOnly(True)
        self.verticalLayout_4.addWidget(self.measurment)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        #Кнопки принять/отменить
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acceptButton = QtWidgets.QPushButton(self.centralwidget)
        self.acceptButton.setObjectName("acceptButton")
        self.horizontalLayout.addWidget(self.acceptButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.name.currentIndexChanged.connect(lambda x: self.nameCurrentUndexChanged(x))

    def nameCurrentUndexChanged(self, index):
        dfn = pd.read_csv('data/products.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        self.producer.setText(str(dfn.iloc[index, 2]))
        self.measurment.setText(str(dfn.iloc[index, 3]))
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Остаток"))
        self.lName.setText(_translate("MainWindow", "Наимевание продукции"))
        self.lProducer.setText(_translate("MainWindow", "Производитель продукции"))
        self.lAmount.setText(_translate("MainWindow", "Остаток продукции"))
        self.lMeasurment.setText(_translate("MainWindow", "Ед измерения"))
        self.acceptButton.setText(_translate("MainWindow", "Принять"))
        self.cancelButton.setText(_translate("MainWindow", "Отменить"))

    def initProductComboBox(self):
        self.name.clear()
        dfn = pd.read_csv('data/products.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        k = 0
        while True:
            try:
                dfn.iloc[k, 0]
            except:
                break
            self.name.addItem(dfn.iloc[k, 0])
            k += 1
