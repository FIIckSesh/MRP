import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets
import balance_ui
import re
from accessify import protected

class BalanceUI(QtWidgets.QMainWindow, balance_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        balance = Balance()


class Balance():
    def __init__(self):
        dfn = pd.read_csv('balance.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        dfn.to_dict('list')
        self.products = dfn

    def changeBalance(self, value, sign, index):
        if sign == '+':
            self.products.iloc[index, 3] += value

        if sign == '-':
            self.products.iloc[index, 3] -= value

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = BalanceUI()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
