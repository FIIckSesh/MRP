#S - класс решает единственную задачу
#O - Расширять без модификации
#L - работает со всеми значениями без доп проверок
#I - Пользователь не должен зависить от неиспользуемых интерфесов
#D - общее не зависит от частного; частное зависит от общего

# Паттерн - цепочка обязанностей. Последовательная обработка.
from auth_ui import Ui_MainWindow
from PyQt5 import QtWidgets
import sys


#Класс формы с обработкой нажатия кнопок
class Auth_UI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginInput.setPlaceholderText("Логин")
        self.passwordInput.setPlaceholderText("Пароль")
        self.canceButton.clicked.connect(self.close)
        self.signInButton.clicked.connect(self.SignInClicked)

    def SignInClicked(self):
        login = str(self.loginInput.text())
        password = str(self.passwordInput.text())
        handler = AuthHandler()
        if handler.CheckData(login, password):
            print("Выполнен вход")
        
#Класс проверяющий правильность введенных данных
class AuthHandler():
    #Словарь логинов паролей. Невидимая извне этого класса
    __data = {'admin':"admin", "45":"123"}

    def CheckData(self, login="", password=""):
        if self.__ExistsLoginInData(login):
            if self.__VerificationPasswordByLogin(login, password):
                return True

    def __ExistsLoginInData(self, login):
        return login in self.__data

    def __VerificationPasswordByLogin(self, login, password):
        return self.__data[login] == password

app = QtWidgets.QApplication(sys.argv)
wind = Auth_UI()
wind.show()
app.exec()