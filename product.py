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
        newClient = Client();


class Product():
    def __init__(self):
        self.name = None;
        self.price = None;
        self.producer = None;
        self.measurment = None;

    def getProduct(self, index):
        dfn = pd.read_csv('products.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        dfn.loc[index]

        self.name = dfn.loc[index][0]
        self.price = dfn.loc[index][1]
        self.producer = dfn.loc[index][2]
        self.measurment = dfn.loc[index][3]

    #def setProduct(self, nm, sm, pt):

        #pattern = re.compile(r'^[A-Za-zа-яА-Я]+$')
        #nsp = [name, sm, pt]
        #for str in nsp:
        #    if pattern.search(str) is None:
        #        return False

        #self.name = nm
        #self.surename = sm
        #self.patronymic = pt

        #self.addCsv()


        #return True

    #def __addCsv__(self):
        #dfn = pd.read_csv('clients.csv', encoding='utf-8')

        #del dfn['Unnamed: 0']
        #new_row = [self.name, self.surename, self.patronymic]
        #dfn = dfn.append(pd.Series(new_row, index=dfn.columns[:len(new_row)]), ignore_index=True)

        #dfn.to_csv(r'clients.csv')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ProductUi()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
