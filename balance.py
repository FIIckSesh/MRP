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
        self.cancelButton.clicked.connect(self.close)

    def addBalanceToData(self):
        name = self.name.currentText()
        producer = self.producer.text()
        amount = self.amount.text()
        measurment = self.measurment.text()

        index = 0
        dfn = pd.read_csv('data/balance.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        while True:
            try:
                dfn.iloc[index]
            except:
                break
            index+=1
        Balance(index).addBalance(name, producer, amount, measurment)
        self.close()
        pass
        



class Balance():
    def __init__(self, index):
        self.name = None
        self.producer = None
        self.amount = None
        self.measurment = None
        self.index = index
        pass
    
    #Добавление нового баланса
    def addBalance(self, name, producer, amount, measurment):
        patternNum = re.compile(r'^[0-9]+$')
        patternEng = re.compile(r'^[A-Za-z]+$')
        patternRus = re.compile(r'^[А-Яа-я]+$')
        patternCheck = False

        listToCheck = [name, producer, measurment]
        for check in listToCheck:
            if patternEng.search(check) is not None:
                patternCheck = True
                
        for check in listToCheck:
            if patternRus.search(check) is not None:
                patternCheck = True

        if patternNum.search(amount) is None:
            patternCheck = False

        if not patternCheck:
            pass

        
        dfn = pd.read_csv('data/balance.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        new_row = [name, producer, amount, measurment]
        dfn = dfn.append(pd.Series(new_row, index=dfn.columns[:len(new_row)]), ignore_index=True)
        dfn.to_csv(r'data/balance.csv')

        pass
    #Изменение баланса по индексу
    def changeBalance(self, amount):
        dfn = pd.read_csv('data/balance.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        print(amount)

        dfn.iloc[self.index, 2] = amount

        dfn.to_csv(r'data/balance.csv')
        pass

    #Удаление банса по индексу
    def removeBalance(self):
        dfn = pd.read_csv('data/balance.csv', encoding='utf-8')

        # Проверка индекса
        try:
             dfn.iloc[self.index, 0]
        except LookupError:
            print("out of frame")
            return

        del dfn['Unnamed: 0']
        dfn = dfn.drop(index=self.index)
        dfn = dfn.reset_index(drop=True)
        dfn.to_csv(r'data/balance.csv')
        pass

    @protected
    #Получение данных по индексу
    def __getInfoBalanceForId__(self):
        dfn = pd.read_csv('data/balance.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        try:
            dfn.iloc[self.index, 0]
        except LookupError:
            print("out of frame")
            return

        self.name = dfn.iloc[self.index, 0]
        self.producer = dfn.iloc[self.index, 1]
        self.amount = dfn.iloc[self.index, 2]
        self.measurment = dfn.iloc[self.index, 3]

        dfn.to_csv(r'data/balance.csv')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = BalanceUI()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
