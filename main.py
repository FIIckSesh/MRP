import sys  # sys нужен для передачи argv в QApplication
import numpy as np
import pandas as pd
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import main_screen_ui  # Это наш конвертированный файл дизайна
import changed_worker_ui
import ui_clients
import shipment_ui
from shipment import Shipment, ShipmentUI
from worker import WorkerUI, Worker
from product import ProductUI, Product
from courier import CourierUI, Courier
from balance import BalanceUI, Balance
from clients import ClientUI, Client
from transaction import Transction, TransctionUI

class MainScreen(QtWidgets.QMainWindow, main_screen_ui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.fillTableWorkers()
        self.tableWidget.verticalScrollBar()
        self.addButton.clicked.connect(self.open)
        self.changedButton.clicked.connect(self.change)
        self.delButton.clicked.connect(self.delete)
        self.items = ["Сотрудники", "Курьеры", "Товары", "Клиенты"]
        self.comboBox.addItems(self.items)
        self.directoryButton.setEnabled(False)  
        self.directorySet = True
        self.directoryButton.clicked.connect(self.setMod)
        self.movementButton.clicked.connect(self.setMod)
        self.comboBox.currentIndexChanged.connect(self.ChangeTable)

    def setMod(self):
        print(123)
        if self.directorySet == False:
            print(123)
            self.directoryButton.setEnabled(False)
            self.movementButton.setEnabled(True)
            self.directorySet = True
            self.items = ["Сотрудники", "Курьеры", "Товары", "Клиенты"]
            self.comboBox.clear()
            self.comboBox.addItems(self.items)
        else:
            print(1232)
            self.directoryButton.setEnabled(True)
            self.movementButton.setEnabled(False)
            self.directorySet = False
            self.items = ["Склад", "Доставки", "Сделки"]
            self.comboBox.clear()
            self.comboBox.addItems(self.items)


    def ChangeTable(self):
        if self.comboBox.currentIndex == -1:
            return
        text = self.comboBox.currentText()
        if self.directorySet:
            if text == self.items[0]:
                self.fillTableWorkers()
                return
            elif text == self.items[1]:
                self.fillTableCouriers()
                return
            elif text == self.items[2]:
                self.fillTableProducts()
                return
            elif text == self.items[3]:
                self.fillTableClients()
                return
        else:
            if text == self.items[0]:
                self.fillTableBalance()
                return
            elif text == self.items[1]:
                self.fillTableShipment()
                return
            elif text == self.items[2]:
                self.fillTableTransaction()
                return



    def fillTableWorkers(self):
        print(1)
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
        print(2)
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
        print(3)
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
        print(4)
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
        print(5)
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
        print(6)
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
        print(7)
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
                self.openShipping()
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
                self.changedShipping()
            if text == self.items[2]:
                self.changedTransaction()

    def delete(self):
        text = self.comboBox.currentText()
        if self.directorySet == True:
            if text == self.items[0]:
                self.delWorker()
            if text == self.items[1]:
                self.delCourier()
                pass
            if text == self.items[2]:
                self.delProduct()
                pass
            if text == self.items[3]:
                self.delClient()
                pass
        else:
            if text == self.items[0]:
                self.delBalance()
                pass
            if text == self.items[1]:
                self.delShipping()
                pass
            if text == self.items[2]:
                self.delTransaction()
                pass

    def openWorker(self):
        self.work = WorkerUI()
        self.work.show()
        self.work.windowTitleChanged.connect(self.fillTableWorkers)

    def changedWorker(self):
        index = self.tableWidget.row(self.tableWidget.currentItem())
        if index == -1:
            return
        name = self.tableWidget.item(index, 0)
        surename = self.tableWidget.item(index, 1)
        patr = self.tableWidget.item(index, 2)
        self.work = ChangedWorkerUI(index, name.text(), surename.text(), patr.text())
        self.work.show()
        self.work.windowTitleChanged.connect(self.fillTableWorkers)

    def delWorker(self):
        index = self.tableWidget.row(self.tableWidget.currentItem())
        if index == -1:
            return
        Worker(index).removeWorker()
        self.fillTableWorkers()

    def openClient(self):
        self.work = ClientUI()
        self.work.show()
        self.work.windowTitleChanged.connect(self.fillTableWorkers)

    def delClient(self):
        index = self.tableWidget.row(self.tableWidget.currentItem())
        if index == -1:
            return
        Client(index).removeClient()
        self.fillTableClients()

    def changedClient(self):
        index = self.tableWidget.row(self.tableWidget.currentItem())
        if index == -1:
            return
        name = self.tableWidget.item(index, 0)
        surename = self.tableWidget.item(index, 1)
        patr = self.tableWidget.item(index, 2)
        street = self.tableWidget.item(index, 3)
        house = self.tableWidget.item(index, 4)
        phone = self.tableWidget.item(index, 5)

        self.client = ChangedClientUI(index, name.text(), surename.text(), patr.text(), street.text(), house.text(), phone.text())
        self.client.show()
        self.client.windowTitleChanged.connect(self.fillTableClients)
        pass

    def openProduct(self):
        self.work = ProductUI()
        self.work.show()
        self.work.prodAddBtn.clicked.connect(self.work.addProduct)
        self.work.prodAddBtn.clicked.connect(self.fillTableProducts)

    def changedProduct(self):
        self.index = self.tableWidget.row(self.tableWidget.currentItem())
        print(self.index )
        if self.index  == -1:
            return

        self.work = ProductUI()
        self.work.show()

        name = self.tableWidget.item(self.index ,0).text()
        price = self.tableWidget.item(self.index ,1).text()
        producer = self.tableWidget.item(self.index ,2).text()
        measurment = self.tableWidget.item(self.index ,3).text()
        self.work.changeWindow(name, price, producer, measurment)
        self.work.prodAddBtn.clicked.connect(self.prodAddBtnClicked)
        self.work.prodAddBtn.clicked.connect(self.fillTableProducts)
        self.work.prodAddBtn.clicked.connect(self.work.hide)
        #self.hide()
        pass

    def prodAddBtnClicked(self):
        name = self.work.nameLine.text()
        price = self.work.priceLine.text()
        producer = self.work.producerLine.text()
        measurment = self.work.measurmentLine.text()
        Product(name, price, producer, measurment).changeData(self.index)

    def delProduct(self):
        index = self.tableWidget.row(self.tableWidget.currentItem())
        if index == -1:
            return
        
        name = self.tableWidget.item(index,0).text()
        price = self.tableWidget.item(index,1).text()
        producer = self.tableWidget.item(index,2).text()
        measurment = self.tableWidget.item(index,3).text()
        Product(name, price, producer, measurment).removeProduct(index)
        self.fillTableProducts()

    def openCourier(self):
        self.work = CourierUI()
        self.work.show()
        self.work.addCourierButton.clicked.connect(self.work.addCourier)
        self.work.addCourierButton.clicked.connect(self.fillTableCouriers)

    def changedCourier(self):
        self.work = CourierUI()
        self.i = self.tableWidget.row(self.tableWidget.currentItem())
        if self.i == -1:
            return
        self.n = self.tableWidget.item(self.i, 0).text()
        self.s = self.tableWidget.item(self.i, 1).text()
        self.p = self.tableWidget.item(self.i, 2).text()
        self.c = self.tableWidget.item(self.i, 3).text()
        self.work.changeWindow(self.n , self.s, self.p, self.c)
        self.work.show()
        self.work.addCourierButton.clicked.connect(self.addCourierButtonClicked)
        self.work.addCourierButton.clicked.connect(self.fillTableCouriers)
        self.work.addCourierButton.clicked.connect(self.work.close)
        pass

    def addCourierButtonClicked(self):
        n = self.work.textName.toPlainText()
        s = self.work.textSurname.toPlainText()
        p = self.work.textPatr.toPlainText()
        c = self.work.carriageSize.toPlainText()
        Courier(self.i).changeCourier(n, s, p, c)

    def delCourier(self):
        index = self.tableWidget.row(self.tableWidget.currentItem())
        if index == -1:
            return
        #Courier(index).removeCourier()
        Courier(index).removeCourier()
        self.fillTableCouriers()

    def openTransaction(self):
        self.work = TransctionUI()
        self.work.show()
        self.work.accept.clicked.connect(self.work.AcceptClicked)
        self.work.accept.clicked.connect(self.fillTableTransaction)
        pass

    def changedTransaction(self):
        self.i = self.tableWidget.row(self.tableWidget.currentItem())
        if self.i == -1:
            return
        self.work = TransctionUI()
        self.work.show()

        self.work.ChangedWindow(self.tableWidget.item(self.i, 0).text(),self.tableWidget.item(self.i, 1).text(), self.tableWidget.item(self.i, 2).text(), self.tableWidget.item(self.i, 3).text(), self.tableWidget.item(self.i, 4).text(), self.tableWidget.item(self.i, 5).text())
        self.work.accept.clicked.connect(self.changeTransactionHelp)
        self.work.accept.clicked.connect(self.fillTableTransaction)
        self.work.accept.clicked.connect(self.work.close)
        pass

    def changeTransactionHelp(self):
        seller = self.work.seller.currentText()
        client = self.work.client.currentText()
        date = self.work.date.text()
        product = self.work.product.currentText()
        amount = self.work.amount.text()
        price = self.work.price.text()

        Transction(self.i).ChangeInfo(self.i, seller, client, date, product, amount, price)
        
    def delTransaction(self):
        self.i = self.tableWidget.row(self.tableWidget.currentItem())
        if self.i == -1:
            return
        Transction(self.i).DeleteTransactionInfo(self.i)
        self.fillTableTransaction()

    def openShipping(self):
        self.work = ShipmentUI()
        self.work.show()
        self.work.pushButton.clicked.connect(self.fillTableShipment)
        pass

    def changedShipping(self):
        index = self.tableWidget.row(self.tableWidget.currentItem())
        if index == -1:
            return

        courier = self.tableWidget.item(index, 0).text()
        date = self.tableWidget.item(index, 1).text()
        product = self.tableWidget.item(index, 2).text()
        count = self.tableWidget.item(index, 3).text()
        client = self.tableWidget.item(index, 4).text()
        address =  self.tableWidget.item(index, 5).text()

        self.work = ChangedShipmentUI(index, courier, date, product, count, client, address)
        self.work.show()
        self.work.pushButton.clicked.connect(self.fillTableShipment)
        pass

    def delShipping(self):
        index = self.tableWidget.row(self.tableWidget.currentItem())
        if index == -1:
            return
        
        Shipment(index).removeShipment()
        self.fillTableShipment()
        pass

    def showBalance(self):
        self.work = BalanceUI()
        self.work.show()
        self.work.acceptButton.clicked.connect(self.work.addBalanceToData)
        self.work.acceptButton.clicked.connect(self.fillTableBalance)
        pass

    def changedBalance(self):
        self.index = self.tableWidget.currentRow()
        if self.index == -1:
            return
        print(123)
        # Находить индекс по имени в pd

        self.work = BalanceUI()
        self.work.initProductComboBox()
        self.work.amount.setText(self.tableWidget.item(self.index, 2).text())
        self.work.name.setCurrentIndex(self.work.name.findText(self.tableWidget.item(self.index, 0).text()))
        self.work.show()
        self.work.acceptButton.clicked.connect(self.changeClick)
        self.work.acceptButton.clicked.connect(self.fillTableBalance)
        pass

    def changeClick(self):
        amount = self.work.amount.text()
        Balance(self.index).changeBalance(amount)
        self.work.close()


    def delBalance(self):
        index = self.tableWidget.currentRow()
        if index == -1:
            return
        Balance(index).removeBalance()
        self.fillTableBalance()
        pass

class ChangedWorkerUI(QtWidgets.QMainWindow, changed_worker_ui.Ui_MainWindow):

    def __init__(self, index, name, surename, patronymic):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.textName.setText(name)
        self.textSurname.setText(surename)
        self.textPatr.setText(patronymic)
        self.index = index

        self.addWorkerButton.clicked.connect(self.changeWorker)

    def changeWorker(self):
        self.n = self.textName.toPlainText()
        self.s = self.textSurname.toPlainText()
        self.p = self.textPatr.toPlainText()
        print(self.index, self.n, self.s, self.p)
        Worker(self.index).changeData(self.n, self.s, self.p)
        self.setWindowTitle("done")
        self.hide()

class ChangedClientUI(QtWidgets.QMainWindow, ui_clients.Ui_MainWindow):

    def __init__(self, index, name, surename, patr, street, house, phone):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.addClientButton.setText("Редактировать клиента")
        self.textName.setText(name)
        self.textSurname.setText(surename)
        self.textPatr.setText(patr)
        self.textStreet.setText(street)
        self.textHouse.setText(house)
        self.textNumber.setText(phone)
        self.index = index

        self.addClientButton.clicked.connect(self.changeClient)

    def changeClient(self):
        self.name = self.textName.toPlainText()
        self.surname = self.textSurname.toPlainText()
        self.patronymic = self.textPatr.toPlainText()
        self.street = self.textStreet.toPlainText()
        self.house = self.textHouse.toPlainText()
        self.phone = self.textNumber.toPlainText()
        Client(self.index).changeData(self.name, self.surname, self.patronymic, self.street, self.house, self.phone)
        self.setWindowTitle("done")
        self.hide()

class ChangedShipmentUI(QtWidgets.QMainWindow, shipment_ui.Ui_MainWindow):

    def __init__(self, index, courier, date, product, count, client, address):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.pushButton.setText("Редактировать клиента")
        self.Courier.setCurrentIndex(self.Courier.findText(courier))
        self.dateEdit.setDate(QtCore.QDate(int(date.split('.')[2]),  int(date.split('.')[1]), int(date.split('.')[0])))
        self.Product.setCurrentIndex(self.Product.findText(product))
        self.spinBox.setValue(int(count))
        self.Client.setCurrentIndex(self.Client.findText(client))
        self.Address.setCurrentIndex(self.Address.findText(address))
        self.index = index

        self.pushButton.clicked.connect(self.changeShipment)

    def changeShipment(self):
        courier = self.Courier.currentText()
        date = self.dateEdit.text()
        product = self.Product.currentText()
        count = self.spinBox.text()
        client = self.Client.currentText()
        address =  self.Address.currentText()
        Shipment(self.index).changeData(courier, date, product, count, client, address)
        self.hide()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainScreen()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
