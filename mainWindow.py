from PyQt6 import QtCore, QtGui, QtWidgets
from Add import Ui_Form
class Ui_Products(object):
    def setupUi(self, Products):
        Products.setObjectName("Products")
        Products.resize(1000, 700)
        Products.setStyleSheet("background-color: rgb(244, 232, 211);")
        self.centralwidget = QtWidgets.QWidget(parent=Products)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(5, 160, 990, 350))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.verticalScrollBar = QtWidgets.QScrollBar(parent=self.widget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(970, 20, 20, 300))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 121, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\Пользователь\\Desktop\\бабаева/Ресурсы/Мастер пол.ico"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.addButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addButton_2.setGeometry(QtCore.QRect(5, 580, 120, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addButton_2.setFont(font)
        self.addButton_2.setStyleSheet("background-color: rgb(103, 186, 128);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border: 2px #F4E8D3;")
        self.addButton_2.setObjectName("addButton_2")
        self.deleteButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deleteButton_4.setGeometry(QtCore.QRect(135, 580, 120, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deleteButton_4.setFont(font)
        self.deleteButton_4.setStyleSheet("background-color: rgb(103, 186, 128);\n"
"border-radius: 20px;\n"
"border: 2px #F4E8D3;\n"
"color: rgb(255, 255, 255);")
        self.deleteButton_4.setObjectName("deleteButton_4")
        self.SearchlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchlineEdit.setGeometry(QtCore.QRect(0, 120, 301, 31))
        self.SearchlineEdit.setPlaceholderText("Введите название продукции...")
        self.SearchlineEdit.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 10px; padding: 5px;")
        self.SearchlineEdit.setObjectName("SearchlineEdit")
        self.searchButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.searchButton_5.setGeometry(QtCore.QRect(300, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.searchButton_5.setFont(font)
        self.searchButton_5.setStyleSheet("""
                    background-color: rgb(103, 186, 128);
                    border-radius: 10px;
                    color: white;
                    font-size: 12pt;
                """)
        self.searchButton_5.setObjectName("searchButton_5")
        self.deleteButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deleteButton_5.setGeometry(QtCore.QRect(390, 580, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deleteButton_5.setFont(font)
        self.deleteButton_5.setStyleSheet("background-color: rgb(103, 186, 128);\n"
"border-radius: 20px;\n"
"border: 2px #F4E8D3;\n"
"color: rgb(255, 255, 255);")
        self.deleteButton_5.setObjectName("deleteButton_5")
        self.deleteButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deleteButton_6.setGeometry(QtCore.QRect(745, 580, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deleteButton_6.setFont(font)
        self.deleteButton_6.setStyleSheet("background-color: rgb(103, 186, 128);\n"
"border-radius: 20px;\n"
"border: 2px #F4E8D3;\n"
"color: rgb(255, 255, 255);")
        self.deleteButton_6.setObjectName("deleteButton_6")
        self.deleteButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deleteButton_8.setGeometry(QtCore.QRect(875, 580, 120, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deleteButton_8.setFont(font)
        self.deleteButton_8.setStyleSheet("background-color: rgb(103, 186, 128);\n"
"border-radius: 20px;\n"
"border: 2px #F4E8D3;\n"
"color: rgb(255, 255, 255);")
        self.deleteButton_8.setObjectName("deleteButton_8")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 30, 390, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        Products.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Products)
        self.statusbar.setObjectName("statusbar")
        Products.setStatusBar(self.statusbar)

        self.retranslateUi(Products)
        QtCore.QMetaObject.connectSlotsByName(Products)

    def retranslateUi(self, Products):
        _translate = QtCore.QCoreApplication.translate
        Products.setWindowTitle(_translate("Products", "Продукция"))
        self.addButton_2.setText(_translate("Products", "Добавить"))

        self.deleteButton_4.setText(_translate("Products", "Удалить"))
        self.SearchlineEdit.setText(_translate("Products", ""))
        self.searchButton_5.setText(_translate("Products", "Поиск"))
        self.deleteButton_5.setText(_translate("Products", "Создать заявку на производство"))
        self.deleteButton_6.setText(_translate("Products", "Категории"))
        self.deleteButton_8.setText(_translate("Products", "Материалы"))
        self.label_2.setText(_translate("Products", "МАСТЕР ПОЛ"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Products = QtWidgets.QMainWindow()
    ui = Ui_Products()
    ui.setupUi(Products)
    Products.show()
    sys.exit(app.exec())
