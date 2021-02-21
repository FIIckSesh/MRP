import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets
import product_ui
import re
from accessify import protected

# логика интерфейса
class ProductUI(QtWidgets.QMainWindow, product_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.prodAddBtn.clicked.connect(self.addProduct)

    # кнопка "Добавить"
    def addProduct(self):
        if self.nameLine.text() == '':
            return
        name = self.nameLine.text()
        price = self.priceLine.text()
        producer = self.producerLine.text()
        measurment = self.measurmentLine.text()

        # Создаем объект и добавляем в csv файл
        newProduct = Product(name, price, producer, measurment)
        dfn = pd.read_csv('products.csv', encoding='utf-8')

        # Проверка на уникальность товара
        for index, row in dfn.iterrows():
            if row['Name'] == name:
                return;

        del dfn['Unnamed: 0']
        new_row = [name, price, producer, measurment]
        index = dfn.columns[:len(new_row)]
        dfn = dfn.append(pd.Series(new_row, index=index), ignore_index=True)
        dfn.to_csv(r'products.csv')

        # Инициализируем кол-во товара
        newProduct.initAmount();

        self.close()


class Product():
    def __init__(self, name, price, producer, measurment):
        self.name = name
        self.price = price
        self.producer = producer
        self.measurment = measurment

    def initAmount(self):
        dfn = pd.read_csv('balance.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        new_row = [self.name, self.producer, 0, self.measurment]
        index = dfn.columns[:len(new_row)]
        dfn = dfn.append(pd.Series(new_row, index=index), ignore_index=True)
        dfn.to_csv(r'balance.csv')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ProductUI()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
