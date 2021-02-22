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

        pattern = re.compile(r'^[A-Za-zа-яА-Я]+$')
        nsp = [nm, sm, pt, st, hs, nb]
        for str in nsp:
            if pattern.search(str) is None:
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
        dfn = pd.read_csv('clients.csv', encoding='utf-8')

        del dfn['Unnamed: 0']


        new_row = [self.__name, self.__surename, self.__patronymic, self.__street, self.__house, self.__phone_number]

        dfn = dfn.append(pd.Series(new_row, index=dfn.columns[:len(new_row)]), ignore_index=True)

        dfn.to_csv(r'clients.csv')

class Client():

    def __init__(self, index):
        self.address = Address()
        self.name = None
        self.surename = None
        self.patronymic = None

        self.getClient(index)

    def getClient(self, index):
        dfn = pd.read_csv('workers.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        dfn.loc[index]

        self.name = dfn.loc[index][0]
        self.surename = dfn.loc[index][1]
        self.patronymic = dfn.loc[index][2]

    def removeClient(index):
        print(index)

        # Удаляем из товаров
        dfn = pd.read_csv('clients.csv', encoding='utf-8')

        # Проверка индекса
        try:
             dfn.iloc[index, 0]
        except LookupError:
            print("out of frame")
            return

        del dfn['Unnamed: 0']
        dfn = dfn.drop(index=index)
        dfn = dfn.reset_index(drop=True)
        dfn.to_csv(r'clients.csv')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ClientUI()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
