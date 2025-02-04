import sys
from PyQt6 import QtWidgets
from mainWindow import Ui_Products
from Add import Ui_Form
from Category import Ui_categoryForm
from material import Ui_materialForm
import pymysql
from pymysql import Error
from PyQt6 import QtCore



def connect_database():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='master_pol'
        )
        return connection
    except Error as e:
        print(f"Ошибка соединения {e}")
        return None


def close_database(connection):
    if connection:
        connection.close()


class MainWindow(QtWidgets.QMainWindow, Ui_Products):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton_2.clicked.connect(self.open_add_form)
        self.deleteButton_6.clicked.connect(self.open_category_form)
        self.deleteButton_8.clicked.connect(self.open_material_form)
        self.searchButton_5.clicked.connect(self.apply_filter)
        self.deleteButton_4.clicked.connect(self.delete_selected_row)

        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 651, 281))
        self.setup_filters()
        self.show_table()

    def delete_selected_row(self):
        selected_row = self.tableWidget.currentRow()

        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления!")
            return

        item = self.tableWidget.item(selected_row, 3)  # Колонка с артикулом (article)

        if item is None:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Не удалось получить артикул продукта!")
            return

        article = item.text()

        confirm = QtWidgets.QMessageBox.question(
            self, "Удаление", f"Удалить продукт с артикулом {article}?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )

        if confirm != QtWidgets.QMessageBox.StandardButton.Yes:
            return

        connection = connect_database()

        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM products WHERE article = %s", (article,))
                connection.commit()

                self.tableWidget.removeRow(selected_row)
                QtWidgets.QMessageBox.information(self, "Успех", "Продукт удалён!")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Ошибка", f"Ошибка удаления: {e}")
            finally:
                close_database(connection)

    def setup_filters(self):
        self.priceFrom = QtWidgets.QLineEdit(self.centralwidget)
        self.priceFrom.setGeometry(QtCore.QRect(130, 80, 80, 31))
        self.priceFrom.setPlaceholderText("Цена от:")

        self.priceTo = QtWidgets.QLineEdit(self.centralwidget)
        self.priceTo.setGeometry(QtCore.QRect(215, 80, 80, 31))
        self.priceTo.setPlaceholderText("Цена до:")

        self.comboBoxType = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxType.setGeometry(QtCore.QRect(440, 120, 180, 31))
        self.comboBoxType.addItem("Выбрать тип")

        self.comboBoxMaterial = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxMaterial.setGeometry(QtCore.QRect(630, 120, 180, 31))
        self.comboBoxMaterial.addItem("Выбрать материал")

        self.comboBoxStandart = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxStandart.setGeometry(QtCore.QRect(820, 120, 180, 31))
        self.comboBoxStandart.addItem("Выбрать стандарт")

        self.load_filters()

    def load_filters(self):
        connection = connect_database()
        cursor = connection.cursor()

        cursor.execute("SELECT DISTINCT product_type_id FROM products")
        for t in cursor.fetchall():
            self.comboBoxType.addItem(str(t[0]))

        cursor.execute("SELECT DISTINCT material_id FROM products")
        for m in cursor.fetchall():
            self.comboBoxMaterial.addItem(str(m[0]))

        cursor.execute("SELECT DISTINCT standart_id FROM products")
        for s in cursor.fetchall():
            self.comboBoxStandart.addItem(str(s[0]))

        close_database(connection)

    def show_table(self, query="SELECT * FROM products", params=[]):
        connection = connect_database()
        cursor = connection.cursor()
        cursor.execute(query, params)
        data = cursor.fetchall()

        cursor.execute("SHOW COLUMNS FROM products")
        columns = cursor.fetchall()
        column_names = [column[0] for column in columns][1:]
        data = [row[1:] for row in data]

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setHorizontalHeaderLabels(column_names)
        self.tableWidget.setColumnStretch(0, 1)
        self.showMaximized()

        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(cell_data)))

        close_database(connection)

    def apply_filter(self):
        name_filter = self.SearchlineEdit.text().strip()
        price_from = self.priceFrom.text().strip()
        price_to = self.priceTo.text().strip()
        type_filter = self.comboBoxType.currentText()
        material_filter = self.comboBoxMaterial.currentText()
        standart_filter = self.comboBoxStandart.currentText()

        query = "SELECT * FROM products WHERE 1=1"
        params = []

        if name_filter:
            query += " AND name LIKE %s"
            params.append(f"%{name_filter}%")

        if price_from.isdigit():
            query += " AND min_partner_price >= %s"
            params.append(int(price_from))

        if price_to.isdigit():
            query += " AND min_partner_price <= %s"
            params.append(int(price_to))

        if type_filter != "Все типы":
            query += " AND product_type_id = %s"
            params.append(int(type_filter))

        if material_filter != "Все материалы":
            query += " AND material_id = %s"
            params.append(int(material_filter))

        if standart_filter != "Все стандарты":
            query += " AND standart_id = %s"
            params.append(int(standart_filter))

        self.show_table(query, params)

    def open_add_form(self):
        self.add_form = AddForm()
        self.add_form.show()
        self.hide()  # Скрываем текущее окно

    def open_category_form(self):
        self.category_form = CategoryForm()
        self.category_form.show()
        self.hide()

    def open_material_form(self):
        self.materil_from = MaterialForm()
        self.materil_from.show()
        self.hide()


class MaterialForm(QtWidgets.QWidget, Ui_materialForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton_4.clicked.connect(self.back_to_main)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 651, 281))
        self.show_table()


    def show_table(self):
        connection = connect_database()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM materials")
        data = cursor.fetchall()

        if data:
            # Получаем имена столбцов
            cursor.execute("SHOW COLUMNS FROM materials")
            columns = cursor.fetchall()
            column_names = [column[0] for column in columns]

            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(column_names))
            self.tableWidget.setHorizontalHeaderLabels(column_names)

            for row_index, row_data in enumerate(data):
                for col_index, cell_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(cell_data)))
        close_database(connection)

    def back_to_main(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.hide()


class CategoryForm(QtWidgets.QWidget, Ui_categoryForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton_4.clicked.connect(self.back_to_main)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 651, 281))
        self.show_table()



    def back_to_main(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def show_table(self):
        connection = connect_database()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM product_types")
        data = cursor.fetchall()


        if data:
            # Получаем имена столбцов
            cursor.execute("SHOW COLUMNS FROM product_types")
            columns = cursor.fetchall()
            column_names = [column[0] for column in columns]

            self.tableWidget.setRowCount(len(data))
            self.tableWidget.setColumnCount(len(column_names))
            self.tableWidget.setHorizontalHeaderLabels(column_names)

            for row_index, row_data in enumerate(data):
                for col_index, cell_data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(cell_data)))
        close_database(connection)


class AddForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exitButton_2.clicked.connect(self.back_to_main)

        self.db_connection = connect_database()  # Подключение к БД
        self.load_data()

    def load_data(self):
        self.load_standarts()
        self.load_type_products()
        self.load_materials()

    def load_standarts(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT number FROM standarts")
            standarts = cursor.fetchall()
            self.comboBox.clear()
            for standart_number in standarts:
                self.comboBox.addItem(f"{standart_number[0]}")
        except Error as e:
            print(f"Ошибка при загрузке данных клиентов: {e}")

    def load_type_products(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT name FROM product_types")
            type_products = cursor.fetchall()

            self.comboBox_2.clear()
            for type_product_name in type_products:
                self.comboBox_2.addItem(f"{type_product_name[0]}")
        except Error as e:
            print(f"Ошибка при загрузке данных клиентов: {e}")

    def load_materials(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT name FROM materials")
            materials = cursor.fetchall()
            self.comboBox_3.clear()
            for material_name in materials:
                self.comboBox_3.addItem(f"{material_name[0]}")
        except Error as e:
            print(f"Ошибка при загрузке данных клиентов: {e}")

    def back_to_main(self):
        self.db_connection.close()
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
