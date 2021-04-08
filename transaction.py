import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets, QtCore
import transction_ui
import re
from accessify import protected

class TransctionUI(QtWidgets.QMainWindow, transction_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cancel.clicked.connect(self.close)
        self.product.currentIndexChanged.connect(lambda index: self.ProductChanged(index))

        self.InitComboSeller()
        self.InitComboClient()
        self.InitComboProduct()

    def ChangedWindow(self, seller, client, date, product, amount, price):
        self.seller.setCurrentIndex(self.seller.findText(seller))
        self.client.setCurrentIndex(self.client.findText(client))
        self.date.setDate(QtCore.QDate(int(date.split('.')[2]),int(date.split('.')[1]),int(date.split('.')[0])))
        self.product.setCurrentIndex(self.product.findText(product))
        self.amount.setText(amount)
        self.price.setText(price)

    def InitComboSeller(self):
        db = pd.read_csv('data/workers.csv', encoding='utf-8')
        del db['Unnamed: 0']
        index = 0
        while True:
            try:
                db.iloc[index, 0]
                new_item = db.iloc[index, 0] + " " + db.iloc[index, 1] + " " + db.iloc[index, 2]
                self.seller.addItem(new_item)
                index += 1
            except:
                db.to_csv(r'data/workers.csv')
                break
        db.to_csv(r'data/workers.csv')

    def InitComboClient(self):
        db = pd.read_csv('data/clients.csv', encoding='utf-8')
        del db['Unnamed: 0']
        index = 0
        while True:
            try:
                db.iloc[index, 0]
                new_item = db.iloc[index, 0] + " " + db.iloc[index, 1] + " " + db.iloc[index, 2]
                self.client.addItem(new_item)
                index += 1
            except:
                db.to_csv(r'data/clients.csv')
                break
        db.to_csv(r'data/clients.csv')

    def InitComboProduct(self):
        db = pd.read_csv('data/products.csv', encoding='utf-8')
        del db['Unnamed: 0']
        index = 0
        while True:
            try:
                db.iloc[index, 0]
                new_item = db.iloc[index, 0]
                self.product.addItem(new_item)
                index += 1
            except:
                db.to_csv(r'data/products.csv')
                break
        db.to_csv(r'data/products.csv')

    def ProductChanged(self, index):
        db = pd.read_csv('data/products.csv', encoding='utf-8')
        del db['Unnamed: 0']
        #check index
        try:
            db.iloc[index, 0]
        except:
            print("Broken")
            return
        self.price.setText(str(db.iloc[index, 1]))
        db.to_csv(r'data/products.csv')

    def AcceptClicked(self):
        seller = self.seller.currentText()
        client = self.client.currentText()
        date = self.date.text()
        product = self.product.currentText()
        amount = self.amount.text()
        price = self.price.text()
        new_row = [seller, client, date, product, amount, price]
        db = pd.read_csv('data/transaction.csv', encoding='utf-8')
        del db['Unnamed: 0']
        id = db.columns[:len(new_row)]

        Transction(id).AddToDataBase(seller, client, date, product, amount, price)

class Transction():
    seller = None
    client = None
    date = None
    product = None
    amount = None
    price = None

    def __init__(self, id):
        print("init")


    def AddToDataBase(self, seller, client, date, product, amount, price):
        patternNum = re.compile(r'^[0-9]+$')

        if patternNum.search(amount) is None:
            print("Количество это число, а не что-то другое")
            return False


        db = pd.read_csv('data/transaction.csv', encoding='utf-8')
        del db['Unnamed: 0']

        new_row = [seller, client, date, product, amount, price]
        print(new_row)
        db = db.append(pd.Series(new_row, index=db.columns[:len(new_row)]), ignore_index=True)
        print(1)
        db.to_csv(r'data/transaction.csv')

    def ChangeInfo(self, id, seller, client, date, product, amount, price):
        db = pd.read_csv('data/transaction.csv', encoding='utf-8')
        del db['Unnamed: 0']
        # check for id
        try:
            db.iloc[id, 0]
        except:
            print("Transaction.py error to check id Transaction __init__")
            return

        db.iloc[id, 0] = seller
        db.iloc[id, 1] = client
        db.iloc[id, 2] = date
        db.iloc[id, 3] = product
        db.iloc[id, 4] = amount
        db.iloc[id, 5] = price
        db.to_csv(r'data/transaction.csv')

    def DeleteTransactionInfo(self, id):
        db = pd.read_csv('data/transaction.csv', encoding='utf-8')
        del db['Unnamed: 0']
        # check for id
        try:
            db.iloc[id, 0]
        except:
            print("Transaction.py error to check id Transaction __init__")
            return
        db = db.drop(index=id)
        db = db.reset_index(drop=True)
        db.to_csv(r'data/transaction.csv')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TransctionUI()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
