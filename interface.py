from PyQt5 import QtCore, QtGui, QtWidgets
from CamFaceIdentify import identify
from CamFaceData import getdata
import numpy as np
from CamFaceTrainer import train
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 313)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.set_data = QtWidgets.QPushButton(self.centralwidget)
        self.set_data.setStyleSheet("font: 75 13pt \"Times New Roman\";\n"
                                    "color: rgb(194, 255, 233);\n"
                                    "background-color: rgb(54, 88, 90);")
        self.set_data.setAutoDefault(False)
        self.set_data.setObjectName("set_data")
        self.verticalLayout.addWidget(self.set_data)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label.setStyleSheet("background-color: rgb(255, 170, 127);\n"
                                 "font: 75 11pt \"Times New Roman\";")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.name_edit.setObjectName("name_edit")
        self.verticalLayout.addWidget(self.name_edit)
        self.add_new = QtWidgets.QPushButton(self.centralwidget)
        self.add_new.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
                                   "color: rgb(194, 255, 233);\n"
                                   "background-color: rgb(54, 88, 90);")
        self.add_new.setObjectName("add_new")
        self.verticalLayout.addWidget(self.add_new)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.trainer = QtWidgets.QPushButton(self.centralwidget)
        self.trainer.setStyleSheet("font: 75 12pt \"Times New Roman\";\n"
                                   "color: rgb(194, 255, 233);\n"
                                   "background-color: rgb(54, 88, 90);")
        self.trainer.setObjectName("trainer")
        self.verticalLayout_2.addWidget(self.trainer)
        self.identify_mod = QtWidgets.QPushButton(self.centralwidget)
        self.identify_mod.setStyleSheet("font: 75 17pt \"Times New Roman\";\n"
                                        "color: rgb(194, 255, 233);\n"
                                        "background-color: rgb(54, 88, 90);")
        self.identify_mod.setObjectName("identify_mod")
        self.verticalLayout_2.addWidget(self.identify_mod)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.set_data.setText(_translate(
            "MainWindow", "Сбор данных нов.пользов."))
        self.label.setText(_translate(
            "MainWindow", "Info: Смотрите в камеру пока горит индикатор"))
        self.name_edit.setText(_translate(
            "MainWindow", "Введите имя пользователя"))
        self.add_new.setText(_translate("MainWindow", "Добавить пользователя"))
        self.trainer.setText(_translate(
            "MainWindow", "Обучить модель новым лицам"))
        self.identify_mod.setText(_translate(
            "MainWindow", "Запуск режима идентификации"))

    def functions(self):
        self.identify_mod.clicked.connect(self.identify)
        self.set_data.clicked.connect(self.newdata)
        self.add_new.clicked.connect(self.face)
        self.trainer.clicked.connect(self.train)

        
        

    def identify(self):   
        identify()

    def newdata(self):
        getdata()
    
    def face(self):
        people=np.loadtxt('names.txt', dtype=str)
        a=self.name_edit.text()
        people=np.append(people,a)
        np.savetxt('names.txt',people, fmt='%s')

    def train(self):
        train()

        


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
