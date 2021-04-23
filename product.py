#Абстрактная фабрика
import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets,QtCore
import product_ui
import re
from accessify import protected
from AbstractFactory import Directory

# логика интерфейса
class ProductUI(QtWidgets.QMainWindow, product_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # кнопка "Добавить"
    def addProduct(self):
        if self.nameLine.text() == '':
            return
        name = self.nameLine.text()
        price = self.priceLine.text()
        producer = self.producerLine.text()
        measurment = self.measurmentLine.text()
        Product(name, price, producer, measurment).addCsv()


        self.close()

    def changeWindow(self, name, price, producer, measurment):
        self.priceLine.setText(price)
        self.measurmentLine.setText(measurment)
        self.nameLine.setText(name)
        self.producerLine.setText(producer)
        _translate = QtCore.QCoreApplication.translate
        self.prodAddBtn.setText(_translate("MainWindow", "Изменить товар"))


class Product(Directory):
    def __init__(self, name=None, price=None, producer=None, measurment=None):
        self.name = name
        self.price = price
        self.producer = producer
        self.measurment = measurment

    def addCsv(self):
        # Создаем объект и добавляем в csv файл
        dfn = pd.read_csv('data/products.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        new_row = [self.name, self.price, self.producer, self.measurment]
        index = dfn.columns[:len(new_row)]
        dfn = dfn.append(pd.Series(new_row, index=index), ignore_index=True)
        dfn.to_csv(r'data/products.csv')

    def changeData(self, index):
        dfn = pd.read_csv('data/products.csv', encoding='utf-8')
        del dfn['Unnamed: 0']

        dfn.iloc[index,0] = self.name
        dfn.iloc[index,1] = self.price
        dfn.iloc[index,2] = self.producer
        dfn.iloc[index,3] = self.measurment
        dfn.to_csv(r'data/products.csv')

    def removeProduct(self, index):
        # Удаляем из товаров
        dfn = pd.read_csv('data/products.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        # Проверка индекса
        try:
             dfn.iloc[index, 0]
        except:
            print("out of frame")
            return
        dfn = dfn.drop(index=index)
        dfn = dfn.reset_index(drop=True)
        dfn.to_csv(r'data/products.csv')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ProductUI()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
