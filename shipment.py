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
                self.items.append(courier.name + " " + courier.surename)
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
                self.items.append(client.name + " " + client.phone_number)
                self.itemsAddress.append(client.street + " " + client.house)
                k = k + 1
            except KeyError:
                break
        self.Client.addItems(self.items)
        self.Address.addItems(self.itemsAddress)

    def addShipment(self):
        print("тут")
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ShipmentUI()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
