import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets
import worker_ui
import re
from accessify import protected

class WorkerUI(QtWidgets.QMainWindow, worker_ui.Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py

        super().__init__()
        self.setupUi(self)
        self.addWorkerButton.clicked.connect(self.addWorker)

    def addWorker(self):
        self.txtErr.setText("")
        worker = WorkersHandler()

        name = self.textName.toPlainText()
        surname = self.textSurname.toPlainText()
        patronymic = self.textPatr.toPlainText()

        set_name = worker.setName(name, surname, patronymic)
        Worker(0).changeData("Kersh", "Kersh", "Kersh")
        print(Worker(0).name)
        if set_name == False:
            self.txtErr.setText("ФИО должно состоять только из латинских символов или кириллицы")
            self.txtErr.setStyleSheet("color: rgb(200, 0, 0)")
        else:
            self.setWindowTitle("done")
            self.hide()




class WorkersHandler():

    def __init__(self):
        self.name = None
        self.surename = None
        self.patronymic = None

    def setName(self, nm, sm, pt):

        pattern = re.compile(r'^[A-Za-zа-яА-Я]+$')
        nsp = [nm, sm, pt]
        for str in nsp:
            if pattern.search(str) is None:
                return False

        self.name = nm
        self.surename = sm
        self.patronymic = pt

        self.addCsv()


        return True

    @protected
    def addCsv(self):
        dfn = pd.read_csv('data/workers.csv', encoding='utf-8')

        del dfn['Unnamed: 0']


        new_row = [self.name, self.surename, self.patronymic]

        dfn = dfn.append(pd.Series(new_row, index=dfn.columns[:len(new_row)]), ignore_index=True)

        dfn.to_csv(r'data/workers.csv')

class Worker():

    def __init__(self, index):
        self.name = None
        self.surename = None
        self.patronymic = None
        self.index = index

        self.getWorker()

    @protected
    def getWorker(self):
        dfn = pd.read_csv('data/workers.csv', encoding='utf-8')
        del dfn['Unnamed: 0']
        dfn.loc[self.index]

        self.name = dfn.loc[self.index][0]
        self.surename = dfn.loc[self.index][1]
        self.patronymic = dfn.loc[self.index][2]

    def changeData(self, name, surename, patronymic):
        dfn = pd.read_csv('data/workers.csv', encoding='utf-8')
        del dfn['Unnamed: 0']

        dfn.loc[self.index][0] = name
        dfn.loc[self.index][1] = surename
        dfn.loc[self.index][2] = patronymic

        dfn.to_csv(r'data/workers.csv')

    def removeWorker():
        # Удаляем из работников
        dfn = pd.read_csv('workers.csv', encoding='utf-8')

        # Проверка индекса
        try:
             dfn.iloc[self.index, 0]
        except LookupError:
            print("out of frame")
            return

        del dfn['Unnamed: 0']
        dfn = dfn.drop(index=self.index)
        dfn = dfn.reset_index(drop=True)
        dfn.to_csv(r'workers.csv')



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = WorkerUI()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
