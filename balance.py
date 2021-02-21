import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets
import balance_ui
import re
from accessify import protected

class BalanceUi(QtWidgets.QMainWindow, Balance_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def addBalance(self):
        #name = self.nameLine.text()


        # Создаем объект и добавляем в csv файл
        #newBalance = Balance(name, price, producer, measurment)
        #newBalance.addCsv()
        dfn = pd.read_csv('balance.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        new_row = [self.name, self.price, self.producer, self.measurment]
        dfn = dfn.append(pd.Series(new_row, index=dfn.columns[:len(new_row)]), ignore_index=True)
        dfn.to_csv(r'balance.csv')


class Balance():
    def __init__(self, product, amount):
        self.product = product
        self.amount = amount

    def getBalance^


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = BalanceUi()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
