from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from login import Ui_Login
from main import Ui_MainWindow
from cadastros import Ui_Cadastros
import sqlite3

class Login(QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.btn_login.clicked.connect(self.login)
        self.app = App()
        self.signin = Cadastros()
        self.app.pushButton.clicked.connect(self.logout)
        self.label_retorune.setText("")
        self.btn_signin.clicked.connect(self.signin_)
        self.signin.pushButton_apply.clicked.connect(self.signin_apply)

    def login(self):
        user = self.lineEdit_user.text()
        password = self.lineEdit_password.text()

        banco = sqlite3.connect('banco_cadastros.db')
        cursor = banco.cursor()
        try:
            cursor.execute(f"SELECT password FROM cadastro WHERE user='{user}'")
            password_bd = cursor.fetchall()

            if password_bd[0][0] == password:
                login.close()
                self.app.show()
            else:
                self.label_retorune.setText("Invalid User.")
        except:
            self.label_retorune.setText("ERROR.")

        banco.close()

    def logout(self):
        self.app.close()
        login.show()
        self.label_retorune.setText("")

    def signin_(self):
        self.signin.show()
        self.signin.label_2.setText("")

    def signin_apply(self):
        name = self.signin.lineEdit_name.text()
        user = self.signin.lineEdit_new_user.text()
        password = self.signin.lineEdit_new_password.text()
        repeat = self.signin.lineEdit_repeat_password.text()

        if password == repeat:
            try:
                banco = sqlite3.connect('banco_cadastros.db')
                cursor = banco.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS cadastro (name text, user text, password text)')
                cursor.execute('INSERT INTO cadastro VALUES ("'+name+'","'+user+'", "'+password+'")')
                banco.commit()
                banco.close()
                self.signin.label_2.setText("Success.")
                self.signin.close()
            except:
                self.signin.label_2.setText("ERROR")
        else:
            self.signin.label_2.setText("Different passwords")




class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

class Cadastros(QMainWindow, Ui_Cadastros):
    def __init__(self):
        super().__init__()
        super().setupUi(self)


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    login = Login()
    app = App()
    cadastros = Cadastros()
    login.show()
    qt.exec_()