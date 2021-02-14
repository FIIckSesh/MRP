import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets
import ProductUi
import re
from accessify import protected

class ProductUi(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Product():

    def __init__(self, name, price, producer, measurment):
        self.name = name;
        self.price = price;
        self.producer = producer;
        self.measurment = measurment;

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ProductUi()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
