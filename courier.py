import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets, QtCore
import courier_ui
import re
from worker import WorkersHandler, Worker
from accessify import protected

class CourierUI(QtWidgets.QMainWindow, courier_ui.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py

        super().__init__()
        self.setupUi(self)
        self.addCourierButton.clicked.connect(self.addCourier)

    def changeWindow(self, name, surname, patronymic, carriageSize):
        self.textName.setText(name)
        self.textPatr.setText(patronymic)
        self.textSurname.setText(surname)
        self.carriageSize.setText(carriageSize)
        _translate = QtCore.QCoreApplication.translate
        self.addCourierButton.setText(_translate("MainWindow", "Изменить курьера"))

    def addCourier(self):
        self.txtErr.setText("")
        courier = CouriersHandler()

        name = self.textName.toPlainText()
        surname = self.textSurname.toPlainText()
        patronymic = self.textPatr.toPlainText()
        carriageSize = self.carriageSize.toPlainText()

        set_name = courier.setName(name, surname, patronymic, carriageSize)

        if set_name == False:
            self.txtErr.setText("ФИО должно состоять только из латинских символов или кириллицы")
            self.txtErr.setStyleSheet("color: rgb(200, 0, 0)")
        else:
            self.hide()

class CouriersHandler(WorkersHandler):

    def setName(self, nm, sm, pt, cs):

        pattern = re.compile(r'^[A-Za-zа-яА-Я]+$')
        pattern2 = re.compile(r'^[1-9]+$')
        nsp = [nm, sm, pt]
        for str in nsp:
            if pattern.search(str) is None:
                return False

        if pattern2.search(cs) is None:
            return False

        self.name = nm
        self.surename = sm
        self.patronymic = pt
        self.carriageSize = cs

        self.addCsv()


        return True

    @protected
    def addCsv(self):
        dfn = pd.read_csv('data/couriers.csv', encoding='utf-8')

        del dfn['Unnamed: 0']


        new_row = [self.name, self.surename, self.patronymic, self.carriageSize]

        dfn = dfn.append(pd.Series(new_row, index=dfn.columns[:len(new_row)]), ignore_index=True)

        dfn.to_csv(r'data/couriers.csv')

class Courier(Worker):

    def __init__(self, index):
        self.name = None
        self.surename = None
        self.patronymic = None
        self.index = index
        self.getCourier(index)

    @protected
    def getCourier(self, index):
        dfn = pd.read_csv('data/couriers.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        self.name = dfn.loc[index][0]
        self.surename = dfn.loc[index][1]
        self.patronymic = dfn.loc[index][2]
        self.carriageSize = dfn.loc[index][3]

    def changeCourier(self, name, surename, patronymic, carriageSize):
        dfn = pd.read_csv('data/couriers.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        print(dfn.loc[self.index])
        dfn.__getitem__(self.index).__setitem__(0, name)
        dfn.__getitem__(self.index).__setitem__(1, surename)
        dfn.__getitem__(self.index).__setitem__(2, patronymic)
        dfn.__getitem__(self.index).__setitem__(3, carriageSize)
        #dfn.loc[self.index][0] = name
        #dfn.loc[self.index][1] = surename
        #dfn.loc[self.index][2] = patronymic
        #dfn.loc[self.index][3] = carriageSize

        dfn.to_csv(r'data/couriers.csv')

    def removeCourier(self, index):
        # Удаляем из курьеров
        dfn = pd.read_csv('data/couriers.csv', encoding='utf-8')

        # Проверка индекса
        try:
             dfn.iloc[index, 0]
        except LookupError:
            print("out of frame")
            return

        del dfn['Unnamed: 0']
        dfn = dfn.drop(index=index)
        dfn = dfn.reset_index(drop=True)
        dfn.to_csv(r'data/couriers.csv')



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = CourierUI()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
