import sys  # sys нужен для передачи argv в QApplication
import numpy as np
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import main_screen_ui  # Это наш конвертированный файл дизайна
import changed_worker_ui
from worker import WorkerUI

class MainScreen(QtWidgets.QMainWindow, main_screen_ui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.fillTableWorkers()
        self.addButton.clicked.connect(self.open)
        self.changedButton.clicked.connect(self.change)
        self.items = ["Сотрудники", "Курьеры", "Товары", "Клиенты"]
        self.comboBox.addItems(self.items)
        self.directoryButton.setEnabled(False)
        self.directorySet = True
        self.directoryButton.clicked.connect(self.setMod)
        self.movementButton.clicked.connect(self.setMod)
        self.comboBox.currentIndexChanged.connect(self.ChangeTable)
        self.tableWidget.itemSelectionChanged.connect(self.test)

    def test(self):
        print(self.tableWidget.itemSelectionChanged)
        print(self.tableWidget.row(self.tableWidget.currentItem()))

    def setMod(self):
        if self.directorySet == False:
            self.directoryButton.setEnabled(False)
            self.movementButton.setEnabled(True)
            self.directorySet = True
            self.items = ["Сотрудники", "Курьеры", "Товары", "Клиенты"]
            self.comboBox.clear()
            self.comboBox.addItems(self.items)
            self.fillTableWorkers()
        else:
            self.directoryButton.setEnabled(True)
            self.movementButton.setEnabled(False)
            self.directorySet = False
            self.items = ["Склад", "Доставки", "Сделки"]
            self.comboBox.clear()
            self.comboBox.addItems(self.items)


    def ChangeTable(self):
        text = self.comboBox.currentText()
        if self.directorySet == True:
            if text == self.items[0]:
                self.fillTableWorkers()
            if text == self.items[1]:
                self.fillTableCouriers()
            if text == self.items[2]:
                self.fillTableProducts()
            if text == self.items[3]:
                self.fillTableClients()
        else:
            if text == self.items[0]:
                self.fillTableBalance()
            if text == self.items[1]:
                self.fillTableShipment()
            if text == self.items[2]:
                self.fillTableTransaction()



    def fillTableWorkers(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(3)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Имя", "Фамилия", "Отчество"])
        dfn = pd.read_csv('data/workers.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        k = 0
        print(len(dfn))
        while True:
            try:
                dfn.loc[k][0]
            except:
                break
            k = k + 1
        self.tableWidget.setRowCount(k)
        for i in range(k):
            for j in range(3):
                self.tableWidget.setItem(i, j, QTableWidgetItem(dfn.loc[i][j]))

    def fillTableCouriers(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(4)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Имя", "Фамилия", "Отчество", "Емкость машины"])
        dfn = pd.read_csv('data/couriers.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        k = 0
        while True:
            try:
                dfn.loc[k][0]
            except:
                break
            k = k + 1
        self.tableWidget.setRowCount(k)
        for i in range(k):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(dfn.loc[i][j])))

    def fillTableProducts(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(4)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Наименование", "Цена", "Поставщик", "Ед. изм."])
        dfn = pd.read_csv('data/products.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        k = 0
        while True:
            try:
                dfn.loc[k][0]
            except:
                break
            k = k + 1
        self.tableWidget.setRowCount(k)
        for i in range(k):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(dfn.loc[i][j])))

    def fillTableClients(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(6)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Имя", "Фамилия", "Отчество", "Улица", "Дом", "Телефон"])
        dfn = pd.read_csv('data/clients.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        k = 0
        while True:
            try:
                dfn.loc[k][0]
            except:
                break
            k = k + 1
        self.tableWidget.setRowCount(k)
        for i in range(k):
            for j in range(6):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(dfn.loc[i][j])))

    def fillTableBalance(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(4)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Название", "Производитель", "Количество", "Ед. изм."])
        dfn = pd.read_csv('data/balance.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        k = 0
        while True:
            try:
                dfn.loc[k][0]
            except:
                break
            k = k + 1
        self.tableWidget.setRowCount(k)
        for i in range(k):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(dfn.loc[i][j])))

    def fillTableShipment(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(6)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Курьер", "Дата", "Товар", "Количество", "Клиент", "Адрес"])
        dfn = pd.read_csv('data/shipment.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        k = 0
        while True:
            try:
                dfn.loc[k][0]
            except:
                break
            k = k + 1
        self.tableWidget.setRowCount(k)
        for i in range(k):
            for j in range(6):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(dfn.loc[i][j])))

    def fillTableTransaction(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(6)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Продавец", "Клиент", "Дата", "Товар", "Количество", "Цена"])
        dfn = pd.read_csv('data/transaction.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        k = 0
        while True:
            try:
                dfn.loc[k][0]
            except:
                break
            k = k + 1
        self.tableWidget.setRowCount(k)
        for i in range(k):
            for j in range(6):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(dfn.loc[i][j])))

    def open(self):
        text = self.comboBox.currentText()
        if self.directorySet == True:
            if text == self.items[0]:
                self.openWorker()
            if text == self.items[1]:
                self.openCourier()
            if text == self.items[2]:
                self.openProduct()
            if text == self.items[3]:
                self.openClient()
        else:
            if text == self.items[0]:
                self.showBalance()
            if text == self.items[1]:
                self.openShipment()
            if text == self.items[2]:
                self.openTransaction()

    def change(self):
        text = self.comboBox.currentText()
        if self.directorySet == True:
            if text == self.items[0]:
                self.changedWorker()
            if text == self.items[1]:
                self.changedCourier()
            if text == self.items[2]:
                self.changedProduct()
            if text == self.items[3]:
                self.changedClient()
        else:
            if text == self.items[0]:
                self.changedBalance()
            if text == self.items[1]:
                self.changedShipment()
            if text == self.items[2]:
                self.changedTransaction()

    def openWorker(self):
        self.work = WorkerUI()
        self.work.show()

    def changedWorker(self):
        self.work = ChangedWorkerUI(5)
        self.work.show()

    def openClient(self):
        ##self.work = ClientUI()
        #self.work.show()
        #self.hide()
        pass

    def changedClient(self):
        ##self.work = ClientUI()
        #self.work.show()
        #self.hide()
        pass

    def openProduct(self):
        #self.work = ProductUI()
        #self.work.show()
        #self.hide()
        pass

    def changedProduct(self):
        #self.work = ProductUI()
        #self.work.show()
        #self.hide()
        pass

    def openCourier(self):
        #self.work = CourierUI()
        #self.work.show()
        #self.hide()
        pass

    def changedCourier(self):
        #self.work = CourierUI()
        #self.work.show()
        #self.hide()
        pass

    def openTransaction(self):
        pass

    def changedTransaction(self):
        pass

    def openShipping(self):
        pass

    def changedShipping(self):
        pass

    def showBalance(self):
        #self.work = BalanceUI()
        #self.work.show()
        #self.hide()
        pass

    def changedBalance(self):
        #self.work = BalanceUI()
        #self.work.show()
        #self.hide()
        pass

class ChangedWorkerUI(QtWidgets.QMainWindow, changed_worker_ui.Ui_MainWindow):

    def __init__(self, index):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        print(index)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainScreen()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
