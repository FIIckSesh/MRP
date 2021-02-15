import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets
import product_ui
import re
from accessify import protected

class ProductUi(QtWidgets.QMainWindow, product_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.prodAddBtn.clicked.connect(self.addProduct)

    def addProduct(self):
        name = self.nameLine.text()
        price = self.priceLine.text()
        producer = self.producerLine.text()
        measurment = self.measurmentLine.text()

        # Создаем объект и добавляем в csv файл
        newProduct = Product(name, price, producer, measurment)
        newProduct.__addCsv__()


class Product():
    def __init__(self, name, price, producer, measurment):
        self.name = name
        self.price = price
        self.producer = producer
        self.measurment = measurment

    def getProduct(self, index):
        dfn = pd.read_csv('products.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        dfn.loc[index]

        self.name = dfn.loc[index][0]
        self.price = dfn.loc[index][1]
        self.producer = dfn.loc[index][2]
        self.measurment = dfn.loc[index][3]

    def __addCsv__(self):
        dfn = pd.read_csv('products.csv', encoding='utf-8')

        del dfn['Unnamed: 0']
        new_row = [self.name, self.price, self.producer, self.measurment]
        dfn = dfn.append(pd.Series(new_row, index=dfn.columns[:len(new_row)]), ignore_index=True)
        dfn.to_csv(r'products.csv')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ProductUi()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
