import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets
import shipment_ui
import re
from accessify import protected
from courier import Courier
from clients import Client

class ShipmentUI(QtWidgets.QMainWindow, shipment_ui.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py

        super().__init__()
        self.setupUi(self)
        self.fillFields()
        self.pushButton.clicked.connect(self.addShipment)

    def fillFields(self):
        k = 0
        self.items = []
        while (True):
            try:
                courier = Courier(k)
                print(type(courier.name))
                self.items.append(str(courier.name) + " " + str(courier.surename))
                k = k + 1
            except KeyError:
                break
        self.Courier.addItems(self.items)
        dfn = pd.read_csv('data/products.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        self.items = []
        for i in range(len(dfn)):
            self.items.append(dfn.iloc[i,0])
        self.Product.addItems(self.items)
        k = 0
        self.items = []
        self.itemsAddress = []
        while (True):
            try:
                client = Client(k)
                self.items.append(str(client.name) + " " + str(client.phone_number))
                self.itemsAddress.append(str(client.street) + " " + str(client.house))
                k = k + 1
            except KeyError:
                break
        self.Client.addItems(self.items)
        self.Address.addItems(self.itemsAddress)

    def addShipment(self):
        shipment = ShipmentHandler()
        courier = self.Courier.currentText()
        date = self.dateEdit.text()
        product = self.Product.currentText()
        count = self.spinBox.text()
        client = self.Client.currentText()
        address = self.Address.currentText()

        shipment.setName(courier, date, product, count, client, address)

        print("тут")
        pass

class ShipmentHandler():

    def __init__(self):
        self.Courier = None
        self.Date = None
        self.Product = None
        self.Count = None
        self.Client = None
        self.Address = None

    def setName(self, Courier, Date, Product, Count, Client, Address):

        self.Courier = Courier
        self.Date = Date
        self.Product = Product
        self.Count = Count
        self.Client = Client
        self.Address = Address

        self.addCsv()

    @protected
    def addCsv(self):
        dfn = pd.read_csv('data/shipment.csv', encoding='utf-8')

        del dfn['Unnamed: 0']


        new_row = [self.Courier, self.Date, self.Product, self.Count, self.Client, self.Address]

        dfn = dfn.append(pd.Series(new_row, index=dfn.columns[:len(new_row)]), ignore_index=True)

        dfn.to_csv(r'data/shipment.csv')

class Shipment():

    def __init__(self, index):
        self.Courier = None
        self.Date = None
        self.Product = None
        self.Count = None
        self.Client = None
        self.Address = None
        self.index = index

        self.getShipment()

    @protected
    def getShipment(self):
        dfn = pd.read_csv('data/shipment.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        dfn.loc[self.index]

        self.Courier = dfn.loc[self.index][0]
        self.Date = dfn.loc[self.index][1]
        self.Product = dfn.loc[self.index][2]
        self.Count = dfn.loc[self.index][3]
        self.Client = dfn.loc[self.index][4]
        self.Address = dfn.loc[self.index][5]

    def changeData(self, courier, date, product, count, client, address):
        dfn = pd.read_csv('data/shipment.csv', encoding='utf-8')
        del dfn['Unnamed: 0']

        dfn.iloc[self.index,0] = courier
        dfn.iloc[self.index,1] = date
        dfn.iloc[self.index,2] = product
        dfn.iloc[self.index,3] = count
        dfn.iloc[self.index,4] = client
        dfn.iloc[self.index,5] = address

        dfn.to_csv(r'data/shipment.csv')

    def removeShipment(self):
        # Удаляем из работников
        dfn = pd.read_csv('data/shipment.csv', encoding='utf-8')

        # Проверка индекса
        try:
             dfn.iloc[self.index, 0]
        except LookupError:
            print("out of frame")
            return

        del dfn['Unnamed: 0']
        dfn = dfn.drop(index=self.index)
        dfn = dfn.reset_index(drop=True)
        dfn.to_csv(r'data/shipment.csv')    

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ShipmentUI()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
