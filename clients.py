import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets
import ui_clients
import re
from accessify import protected

class ClientUI(QtWidgets.QMainWindow, ui_clients.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py

        super().__init__()
        self.setupUi(self)
        self.addClientButton.clicked.connect(self.addClient)

    def addClient(self):
        client = ClientsHandler()

        name = self.textName.toPlainText()
        surname = self.textSurname.toPlainText()
        patronymic = self.textPatr.toPlainText()
        street = self.textStreet.toPlainText()
        house = self.textHouse.toPlainText()
        number = self.textNumber.toPlainText()

        set_name = client.setName(name, surname, patronymic, street, house, number)
<<<<<<< HEAD
        self.setWindowTitle("done")
        self.hide()
=======
>>>>>>> parent of 31beef7 (123)


        print(set_name)


class ClientsHandler():

    def __init__(self):
        self.__name = None
        self.__surename = None
        self.__patronymic = None
        self.__street = None
        self.__house = None
        self.__phone_number = None

    def setName(self, nm, sm, pt, st, hs, nb):

        patternEng = re.compile(r'^[A-Za-z]+$')
        patternRus = re.compile(r'^[а-яА-Я]+$')
        nsp = [nm, sm, pt, st, hs, nb]
        for str in nsp:
            if patternEng.search(str) is None or patternRus.search(str) is None:
                return False

        self.__name = nm
        self.__surename = sm
        self.__patronymic = pt
        self.__street = st
        self.__house = hs
        self.__phone_number = nb

        self.addCsv()


        return True

    @protected
    def addCsv(self):
<<<<<<< HEAD
        dfn = pd.read_csv('data/clients.csv', encoding='utf-8')
=======
        dfn = pd.read_csv('clients.csv', encoding='utf-8')
>>>>>>> parent of 31beef7 (123)

        del dfn['Unnamed: 0']


        new_row = [self.__name, self.__surename, self.__patronymic, self.__street, self.__house, self.__phone_number]

        dfn = dfn.append(pd.Series(new_row, index=dfn.columns[:len(new_row)]), ignore_index=True)

<<<<<<< HEAD
        dfn.to_csv(r'data/clients.csv')
=======
        dfn.to_csv(r'clients.csv')
>>>>>>> parent of 31beef7 (123)

class Client():

    def __init__(self, index):
        self.name = None
        self.surename = None
        self.patronymic = None
        self.street = None
        self.house = None
        self.phone_number = None
        self.index = index

        self.getClient(index)

    def getClient(self, index):
        dfn = pd.read_csv('data/clients.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        dfn.loc[self.index]

        self.name = dfn.loc[self.index][0]
        self.surename = dfn.loc[self.index][1]
        self.patronymic = dfn.loc[self.index][2]
        self.street = dfn.loc[self.index][3]
        self.house = dfn.loc[self.index][4]
        self.phone_number = dfn.loc[self.index][5]

<<<<<<< HEAD
<<<<<<< HEAD
    def removeClient(self, index):
        print(index)
=======
    def removeClient(self):
        print(self.index)
>>>>>>> 41fd03c46743a4e67b4bd2a698114aaa2c51f059
=======
    def removeClient(self, index):
        print(index)
>>>>>>> parent of 31beef7 (123)

        # Удаляем из товаров
        dfn = pd.read_csv('data/clients.csv', encoding='utf-8')

        # Проверка индекса
        try:
<<<<<<< HEAD
             dfn.iloc[self.index, 0]
=======
             dfn.iloc[index, 0]
>>>>>>> parent of 31beef7 (123)
        except LookupError:
            print("out of frame")
            return

        del dfn['Unnamed: 0']
<<<<<<< HEAD
        dfn = dfn.drop(index=self.index)
=======
        dfn = dfn.drop(index=index)
>>>>>>> parent of 31beef7 (123)
        dfn = dfn.reset_index(drop=True)
        dfn.to_csv(r'data/clients.csv')

    def changeData(self, name, surename, patr, street, house, phone):
        dfn = pd.read_csv('data/clients.csv', encoding='utf-8')
        del dfn['Unnamed: 0']

        #print(self.index, name, surename, patr, street, house, phone)
        print(name)
        print(dfn.loc[self.index][0])
        dfn.iloc[self.index, 0] = name
        print(dfn.iloc[self.index][0])
        dfn.iloc[self.index, 1] = surename
        dfn.iloc[self.index, 2] = patr
        dfn.iloc[self.index, 3] = street
        dfn.iloc[self.index, 4] = house
        dfn.iloc[self.index, 5] = phone

        dfn.to_csv(r'data/clients.csv')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ClientUI()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
