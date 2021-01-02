import sqlite3
from sys import argv, exit
from datetime import datetime
from re import sub, split, match
from time import mktime, time
from typing import List, Text, Tuple

from PySide2.QtGui import QCloseEvent
from PySide2.QtCore import Qt, QDate
from PySide2.QtPrintSupport import QPrinter
from PySide2.QtWidgets import QApplication, \
    QMessageBox, QDialog, QTableWidgetItem, QWidget, QFileDialog, QMainWindow
from pytz import timezone

from forms.about import Ui_Dialog
from forms.additional import Ui_Form as additional_Ui_Form
from forms.create_orders import Ui_Form as create_orders_Ui_Form
from db import DataBase
from forms.employees import Ui_Form
from forms.main_welcome import Ui_MainWindow
from forms.spravka import Ui_Form as spravka_Ui_Form
from forms.update_orders import Ui_Form as update_orders_Ui_Form
from image_resource import *
from string import punctuation


class AboutForm(QDialog):
    def __init__(self) -> None:
        super(AboutForm, self).__init__(None, Qt.WindowSystemMenuHint)
        self.about = Ui_Dialog()
        self.about.setupUi(self)

        self.setEnabled(True)
        self.setToolTip("Почта для связи - pavlyuchenko_196@mail.ru")
        self.about.pushButton_about_2.clicked.connect(lambda: self.close())


class Employees(QWidget):
    def __init__(self) -> None:
        super(Employees, self).__init__()
        self.employees = Ui_Form()
        self.employees.setupUi(self)
        self.db = DataBase()
        self.employees.tabWidget.setCurrentIndex(0)
        self.employees.pushButton.clicked.connect(self.adding_employee)
        self.employees.comboBox.setPlaceholderText("Ничего не выбрано")
        self.employee_list = self.db.getting(["*"], "employees", "simple")
        for i in range(0, len(self.employee_list), 1):
            self.employees.comboBox.addItem(f"{self.employee_list[i][1]} {self.employee_list[i][2]} {self.employee_list[i][3]}")
        self.employees.comboBox.activated[str].connect(self.get_info_ab_employee)

    def adding_employee(self):
        title: Text = "ПУСТОЕ ПОЛЕ"
        msg: Text = "Вы ничего не написали в поле - "
        first_name: Text = ""
        surname: Text = ""
        patronymic: Text = ""
        employement_date: Text = ""
        trigger: bool = False
        if self.employees.lineEdit.text() == "":
            QMessageBox.information(self, title, msg + "Фамилия")
            trigger += True
        elif self.employees.lineEdit_2.text() == "":
            QMessageBox.information(self, title, msg + "Имя")
            trigger += True
        elif self.employees.lineEdit_3.text() == "":
            patronymic += "-"

        if trigger is False:
            try:
                surname += self.employees.lineEdit.text().lstrip(" ").rstrip(" ").capitalize()
                first_name += self.employees.lineEdit_2.text().lstrip(" ").rstrip(" ").capitalize()
                employement_date += self.employees.dateEdit.text().lstrip(" ").rstrip(" ")
                insert_query: Text = "INSERT INTO employees ('SURNAME', 'FIRST_NAME','PATRONYMIC','EMPLOYMENT_DATE') VALUES ("
                if patronymic == "-":
                    insert_query += f"'{surname}', '{first_name}', '-', '{employement_date}')"
                    self.db.insert(insert_query)
                else:
                    patronymic += self.employees.lineEdit_3.text().lstrip(" ").rstrip(" ").capitalize()
                    insert_query += f"'{surname}', '{first_name}', '{patronymic}', '{employement_date}')"
                    self.db.insert(insert_query)
                self.employees.comboBox.addItem(f"{surname} {first_name} {patronymic}")
            except sqlite3.IntegrityError as err:
                if "UNIQUE constraint failed" in err.args[0]:
                    QMessageBox.information(self, "Нарушение целостности данных в БД", "Вы пытаетесь добавить сотрудника, который уже есть!!!")
                else:
                    pass
            finally:
                self.employees.lineEdit.clear()
                self.employees.lineEdit_2.clear()
                self.employees.lineEdit_3.clear()

    def get_info_ab_employee(self, string):
        loc_str: List = split(" ", string)
        select_query: Text = f"WHERE SURNAME='{loc_str[0]}' and FIRST_NAME='{loc_str[1]}' and PATRONYMIC='{loc_str[2]}'"
        loc_employee_data_db: List[Tuple] = self.db.getting(["*"], "employees", method="custom", custom_body=select_query)
        self.employees.lineEdit_4.setText(loc_employee_data_db[0][1])
        self.employees.lineEdit_5.setText(loc_employee_data_db[0][2])
        self.employees.lineEdit_6.setText(loc_employee_data_db[0][3])
        self.employees.lineEdit_7.setText(str(loc_employee_data_db[0][0]))
        loc_date: List = split("/", loc_employee_data_db[0][4])
        self.employees.dateEdit_2.setDate(QDate(int(loc_date[2]), int(loc_date[1]), int(loc_date[0])))

    def closeEvent(self, event: QCloseEvent):
        self.db.__del__()
        event.accept()


class create_orders(QWidget):
    def __init__(self) -> None:
        super(create_orders, self).__init__()
        self.c_orders = create_orders_Ui_Form()
        self.c_orders.setupUi(self)
        self.db = DataBase()
        self.c_orders.comboBox.setPlaceholderText("Ничего не выбрано")
        self.employee_list = self.db.getting(["*"], "employees", "simple")
        for i in range(0, len(self.employee_list), 1):
            self.c_orders.comboBox.addItem(f"{self.employee_list[i][1]} {self.employee_list[i][2]} {self.employee_list[i][3]}")
        self.c_orders.comboBox.activated[str].connect(self.employee_id)
        self.loc_employee_id: Text = ""

        self.c_orders.pushButton.clicked.connect(self.confirm_button_clk)

        self.vehicle_model: Text = ""
        self.vehicle_brand: Text = ""
        self.reg_number: Text = ""
        self.repair_date_start: float = 0
        self.repair_date_end: float = 0

    def employee_id(self, fullname):

        loc_list: List = split(" ", fullname)
        loc_query: Text = f"WHERE SURNAME='{loc_list[0]}' and FIRST_NAME='{loc_list[1]}' and PATRONYMIC='{loc_list[2]}'"
        self.loc_employee_id: Text = self.db.getting(["*"], "employees", "custom", custom_body=loc_query)[0][0]

    def confirm_button_clk(self):
        title: Text = "ПУСТОЕ ПОЛЕ"
        msg: Text = "Вы ничего не написали в поле - "
        title2: Text = "НЕКОРРЕКТНЫЙ ВВОД"
        msg2: Text = "Данное поле не может содержать более "
        msg3: Text = "Данное поле может содержать только два слова, разделенные дефисом либо пробелом\n" \
                     "Например, Alfa Romeo или Mercedes-Benz "
        msg4: Text = "Введен недопустимый символ _"

        if self.c_orders.vehicle_brand.text() == "":
            QMessageBox.information(self, title, msg + "Марка ТС")
        elif match("(\w{3,}\s{2,}\w{1,})", self.c_orders.vehicle_brand.text().lstrip(" ").rstrip(" ")):
            QMessageBox.information(self, title2, "Вы ввели более одного пробельного символа между словами")
        elif len(self.c_orders.vehicle_brand.text().rstrip(" ").lstrip(" ").split(" ")) > 2:
            QMessageBox.information(self, title2, msg2 + "2 слов")
        elif "_" in self.c_orders.vehicle_brand.text().rstrip(" ").lstrip(" "):
            QMessageBox.information(self, title2, msg4)
        elif match(r'(^\w{1,}-\w{1,}$|^\w{1,}$|^\w{1,}\s[^\d\W]{1,}$)', self.c_orders.vehicle_brand.text().lstrip(" ").rstrip(" ")) is None:
            QMessageBox.information(self, title2, msg3)

        elif self.c_orders.vehicle_model.text() == "":
            QMessageBox.information(self, title, msg + "Модель ТС")
        elif len(self.c_orders.vehicle_model.text().rstrip(" ").split(" ")) > 1:
            QMessageBox.information(self, title2, msg2 + "1 слова")

        elif self.c_orders.repair_cost.text() == "":
            QMessageBox.information(self, title, msg + "Стоимость ремонта")
        elif len(self.c_orders.repair_cost.text().rstrip(" ").split(" ")) > 1:
            QMessageBox.information(self, title2, msg2 + "одного числа без пробелов!")
        elif match(r'(^\d{1,}\.\d{1,}$|^\d{1,}$)', self.c_orders.repair_cost.text()) is None:
            QMessageBox.information(self, title2, "Поле - 'Стоимость ремонта' должно состоять из числа, а не из буквенных символов")

        elif self.c_orders.reg_number.text() == "":
            QMessageBox.information(self, title, msg + "Гос. номер ТС")
        elif len(self.c_orders.reg_number.text().rstrip(" ").split(" ")) > 1:
            QMessageBox.information(self, title2, msg2 + "одного слова без пробелов, например - У735ВР33")

        elif self.c_orders.breakdown_description.toPlainText() == "":
            QMessageBox.information(self, title, msg + "Описание поломки")
        elif self.c_orders.comboBox.currentIndex() == -1:
            QMessageBox.information(self, title, "Выберите мастера!")
        else:
            self.vehicle_model = self.c_orders.vehicle_model.text().rstrip(" ").lstrip(" ").capitalize()

            vehicle_brand_split = split("(\s|-)", self.c_orders.vehicle_brand.text().rstrip(" ").lstrip(" "))
            vehicle_brand: Text = ""
            for i in vehicle_brand_split:
                if len(i) > 3 and match("(^\s{1,}$|^-$)", i) is None:
                    vehicle_brand += " " + sub("_{1,}", "", i).capitalize()
                elif len(i) == 3 and match("(^\s{1,}$|^-$)", i) is None:
                    vehicle_brand += sub("_{1,}", "", i).upper()
            if "BMW" in vehicle_brand or "БМВ" in vehicle_brand:
                self.vehicle_brand = "BMW"
            elif "Mercedes" in vehicle_brand or "Benz" in vehicle_brand or "benz" in vehicle_brand or "Мерс" in vehicle_brand or "мерс" in vehicle_brand:
                self.vehicle_brand = "Mercedes-Benz"
            elif "GMC" in vehicle_brand:
                self.vehicle_brand = "GMC"
            elif "Alfa" in vehicle_brand or "romeo" in vehicle_brand or "Romeo" in vehicle_brand or "Альфа" in vehicle_brand or "альфа" in vehicle_brand:
                self.vehicle_brand = "Alfa-Romeo"
            else:
                self.vehicle_brand = vehicle_brand.lstrip(" ").rstrip(" ")

            self.reg_number = self.c_orders.reg_number.text().rstrip(" ").lstrip(" ").upper()
            self.repair_date_start = mktime(datetime.strptime(self.c_orders.dateEdit.text().rstrip(" ").lstrip(" "), "%d/%m/%Y").timetuple())
            self.repair_date_end = mktime(datetime.strptime(self.c_orders.dateEdit_2.text().rstrip(" ").lstrip(" "), "%d/%m/%Y").timetuple())

            if self.repair_date_start > self.repair_date_end:
                QMessageBox.information(self, "НЕВЕРНЫЕ ДАТЫ", "Дата начала не может быть позже даты окончания работ!!!")
            else:

                loc_repair_date_start: Text = datetime.fromtimestamp(self.repair_date_start).strftime("%d/%m/%Y")
                loc_repair_date_end: Text = datetime.fromtimestamp(self.repair_date_end).strftime("%d/%m/%Y")

                if type(self.db.insert("INSERT INTO orders ('EMPLOYEE_ID', 'VEHICLE_ID', 'REPAIR_COST', 'BREAKDOWN_DESCRIPTION',"
                                       f"'REPAIR_DATE_START', 'REPAIR_DATE_END') VALUES ("
                                       f"{int(self.loc_employee_id)}, '{self.vehicle()}', '{self.c_orders.repair_cost.text()}',"
                                       f"'{self.c_orders.breakdown_description.toPlainText()}', '{loc_repair_date_start}',"
                                       f"'{loc_repair_date_end}')")) is int:
                    self.c_orders.vehicle_model.clear()
                    self.c_orders.vehicle_brand.clear()
                    self.c_orders.reg_number.clear()
                    self.c_orders.repair_cost.clear()
                    self.c_orders.breakdown_description.clear()

    def vehicle(self) -> int:
        select_vehicle_query: Text = f"WHERE VEHICLE_BRAND='{self.vehicle_brand}' and VEHICLE_MODEL='{self.vehicle_model}' " \
                                     f"and REG_NUMBER='{self.reg_number}'"
        loc_vehicle_id = self.db.getting(["*"], "vehicle", "custom", custom_body=select_vehicle_query)
        if len(loc_vehicle_id) != 0:
            return loc_vehicle_id[0][0]
        else:
            insert_vehicle_query: Text = "INSERT INTO vehicle ('VEHICLE_BRAND', 'VEHICLE_MODEL', 'REG_NUMBER') VALUES " \
                                         f"('{self.vehicle_brand}', '{self.vehicle_model}', '{self.reg_number}')"
            return self.db.insert(insert_vehicle_query)

    def closeEvent(self, event: QCloseEvent):
        self.db.__del__()
        event.accept()


class update_orders(QWidget):
    def __init__(self) -> None:
        super(update_orders, self).__init__()
        self.u_orders = update_orders_Ui_Form()
        self.u_orders.setupUi(self)

        self.db = DataBase()
        self.u_orders.comboBox.setPlaceholderText("Ничего не выбрано")
        self.employee_list = self.db.getting(["*"], "employees", "simple")
        for i in range(0, len(self.employee_list), 1):
            self.u_orders.comboBox.addItem(f"{self.employee_list[i][1]} {self.employee_list[i][2]} {self.employee_list[i][3]}")
        self.u_orders.comboBox_2.setPlaceholderText("Не выбран сотрудник")

        self.loc_employee_id: Text = ""
        self.u_orders.comboBox.activated[str].connect(self.employee_id)

        self.employee_orders_by_index: dict = dict()
        self.u_orders.comboBox_2.activated[int].connect(self.fill_data_to_field)

        self.index: int = 0
        self.repair_date_start: float = 0
        self.repair_date_end: float = 0
        self.breakdown_description: Text = ""
        self.repair_cost: Text = ""
        self.u_orders.pushButton.clicked.connect(self.apply_changes)

    def employee_id(self, fullname):
        loc_list: List = split(" ", fullname)
        loc_query: Text = f"WHERE SURNAME='{loc_list[0]}' and FIRST_NAME='{loc_list[1]}' and PATRONYMIC='{loc_list[2]}'"
        self.loc_employee_id: Text = self.db.getting(["*"], "employees", "custom", custom_body=loc_query)[0][0]
        self.employee_orders()

    def employee_orders(self):
        self.u_orders.comboBox_2.clear()

        select_employee_orders: Text = f"WHERE EMPLOYEE_ID={self.loc_employee_id}"
        tmp_employee_orders: List[Tuple] = self.db.getting(["*"], "orders", "custom", custom_body=select_employee_orders)

        if len(tmp_employee_orders) != 0:
            counter: int = 0
            for order in tmp_employee_orders:
                order_string: Text = ""
                tmp_vehicle_data: Tuple = self.db.getting(["*"], "vehicle", "custom", custom_body=f"WHERE ID={order[2]}")[0]
                order_string += f"Заказ от {order[5]}, {tmp_vehicle_data[1]} {tmp_vehicle_data[2]}, {tmp_vehicle_data[3]}"

                self.u_orders.comboBox_2.addItem(order_string)
                self.u_orders.comboBox_2.setItemData(counter, order_string, Qt.ToolTipRole)
                self.u_orders.comboBox_2.setToolTipDuration(2000)
                self.employee_orders_by_index[counter] = [order, tmp_vehicle_data[1], tmp_vehicle_data[2], tmp_vehicle_data[3]]
                counter += 1

    def fill_data_to_field(self, idx):
        self.index = idx
        for i in range(3, 7, 1):
            if i == 3:
                self.u_orders.repair_cost.setText(self.employee_orders_by_index[idx][0][i])
            elif i == 4:
                self.u_orders.breakdown_description.setText(self.employee_orders_by_index[idx][0][i])
            elif i == 5:
                loc_repair_start_date: List = self.employee_orders_by_index[idx][0][i].split("/")
                self.u_orders.dateEdit.setDate(QDate(int(loc_repair_start_date[2]), int(loc_repair_start_date[1]), int(loc_repair_start_date[0])))
            elif i == 6:
                loc_repair_end_date: List = self.employee_orders_by_index[idx][0][i].split("/")
                self.u_orders.dateEdit_2.setDate(QDate(int(loc_repair_end_date[2]), int(loc_repair_end_date[1]), int(loc_repair_end_date[0])))

        self.u_orders.vehicle_brand.setText(self.employee_orders_by_index[idx][1])
        self.u_orders.vehicle_brand.setReadOnly(True)

        self.u_orders.vehicle_model.setText(self.employee_orders_by_index[idx][2])
        self.u_orders.vehicle_model.setReadOnly(True)

        self.u_orders.reg_number.setText(self.employee_orders_by_index[idx][3])
        self.u_orders.reg_number.setReadOnly(True)

    def apply_changes(self):

        title: Text = "ПУСТОЕ ПОЛЕ"
        msg: Text = "Вы ничего не написали в поле - "
        title2: Text = "НЕКОРРЕКТНЫЙ ВВОД"
        msg2: Text = "Данное поле не может содержать более "

        if self.u_orders.repair_cost.text() == "":
            QMessageBox.information(self, title, msg + "Стоимость ремонта")
        elif len(self.u_orders.repair_cost.text().rstrip(" ").split(" ")) > 1:
            QMessageBox.information(self, title2, msg2 + "одного числа без пробелов!")
        elif match(r'(^\d{1,}\.\d{1,}$|^\d{1,}$)', self.u_orders.repair_cost.text()) is None:
            QMessageBox.information(self, title2, "Поле - 'Стоимость ремонта' должно состоять из числа, а не из буквенных символов")
        else:
            self.repair_cost = self.u_orders.repair_cost.text().lstrip(" ").rstrip(" ")

            # print(mktime(datetime.strptime("20/10/2020", "%d/%m/%Y").timetuple()))
            # print(datetime.fromtimestamp(1603134000.0, tz=timezone("Asia/Yekaterinburg")))

            self.repair_date_start = mktime(datetime.strptime(self.u_orders.dateEdit.text().rstrip(" ").lstrip(" "), "%d/%m/%Y").timetuple())
            self.repair_date_end = mktime(datetime.strptime(self.u_orders.dateEdit_2.text().rstrip(" ").lstrip(" "), "%d/%m/%Y").timetuple())
            self.breakdown_description = self.u_orders.breakdown_description.toPlainText().rstrip(" ").lstrip(" ")

            if self.repair_date_start > self.repair_date_end:
                QMessageBox.information(self, "НЕВЕРНЫЕ ДАТЫ", "Дата начала не может быть позже даты окончания работ!!!")
            else:
                loc_repair_date_start: Text = datetime.fromtimestamp(self.repair_date_start).strftime("%d/%m/%Y")
                loc_repair_date_end: Text = datetime.fromtimestamp(self.repair_date_end).strftime("%d/%m/%Y")
                # UPDATE "main"."orders" SET "BREAKDOWN_DESCRIPTION"=? WHERE "_rowid_"='1004'
                query: Text = f"UPDATE orders SET BREAKDOWN_DESCRIPTION='{self.breakdown_description}', REPAIR_COST='{self.repair_cost}', " \
                              f"REPAIR_DATE_START='{loc_repair_date_start}', REPAIR_DATE_END='{loc_repair_date_end}' " \
                              f"WHERE ID={self.employee_orders_by_index[self.index][0][0]}"
                self.u_orders.comboBox_2.setItemText(self.index, sub("\d{1,2}/\d{1,2}/\d{,4}", f"{loc_repair_date_start}", self.u_orders.comboBox_2.currentText()))
                self.db.update(query)

    def closeEvent(self, event: QCloseEvent):
        self.db.__del__()
        event.accept()


class certificates(QWidget):
    def __init__(self) -> None:
        super(certificates, self).__init__()
        self.spravka = spravka_Ui_Form()
        self.spravka.setupUi(self)

        self.db = DataBase()

        self.spravka.pushButton.clicked.connect(self.SavetoPDF)
        self.spravka.pushButton_2.clicked.connect(self.SavetoPDF)

        # print(mktime(datetime.strptime("20/10/2020", "%d/%m/%Y").timetuple()))
        # print(datetime.fromtimestamp(1603134000.0, tz=timezone("Asia/Yekaterinburg")))

        self.today_timestamp: float = time()
        self.one_year_ago_timestamp: float = 0.0
        self.total_revenue_year: float = 0.0
        self.total_revenue_helfyear: float = 0.0
        self.one_year_ago()
        self.half_year_ago()

    def db_to_timestamp(self, date) -> float:
        return mktime(datetime.strptime(str(date), "%d/%m/%Y").timetuple())

    def one_year_ago(self):
        self.one_year_ago_timestamp = self.today_timestamp - (86400.0 * 365.2425)
        loc_year_ago_date: Text = datetime.strftime(datetime.fromtimestamp(self.one_year_ago_timestamp - 86400, tz=timezone("UTC")), "%d/%m/%Y")
        loc_current_date: Text = datetime.strftime(datetime.fromtimestamp(self.today_timestamp, tz=timezone("UTC")), "%d/%m/%Y")
        self.spravka.textEdit.setText(sub("00/00/0000", loc_year_ago_date, self.spravka.textEdit.toHtml()))
        self.spravka.textEdit.setText(sub("11/11/1111", loc_current_date, self.spravka.textEdit.toHtml()))

        loc_orders: List[Tuple] = self.db.getting(["*"], "orders", "simple")
        for order in loc_orders:
            if (self.db_to_timestamp(loc_year_ago_date) < self.db_to_timestamp(order[5])) and (self.db_to_timestamp(order[6]) < time()):
                self.total_revenue_year += float(order[3])
            else:
                pass
        self.spravka.textEdit.setText(sub("\{сумма\}", str(self.total_revenue_year), self.spravka.textEdit.toHtml()))

    def half_year_ago(self):
        self.one_year_ago_timestamp = self.today_timestamp - (86400.0 * (365.2425 / 2))
        loc_halfyear_ago_date: Text = datetime.strftime(datetime.fromtimestamp(self.one_year_ago_timestamp, tz=timezone("UTC")), "%d/%m/%Y")
        loc_current_date: Text = datetime.strftime(datetime.fromtimestamp(self.today_timestamp, tz=timezone("UTC")), "%d/%m/%Y")
        self.spravka.textEdit_2.setText(sub("00/00/0000", loc_halfyear_ago_date, self.spravka.textEdit_2.toHtml()))
        self.spravka.textEdit_2.setText(sub("11/11/1111", loc_current_date, self.spravka.textEdit_2.toHtml()))

        loc_orders: List[Tuple] = self.db.getting(["*"], "orders", "simple")
        for order in loc_orders:
            if (self.db_to_timestamp(loc_halfyear_ago_date) < self.db_to_timestamp(order[5])) and (self.db_to_timestamp(order[6]) < time()):
                self.total_revenue_helfyear += float(order[3])

            else:
                pass
        self.spravka.textEdit_2.setText(sub("\{сумма\}", str(self.total_revenue_helfyear), self.spravka.textEdit_2.toHtml()))

    def SavetoPDF(self):
        filename = QFileDialog.getSaveFileName(self, ("Save to PDF"), filter=("PDF Document (*.pdf)"))
        if filename[0] != '':
            printer = QPrinter(QPrinter.HighResolution)
            printer.setPageSize(QPrinter.A4)
            printer.setColorMode(QPrinter.Color)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(filename[0])
            self.spravka.textEdit.document().print_(printer)

    def closeEvent(self, event: QCloseEvent):
        self.db.__del__()
        event.accept()


class additional(QWidget):
    def __init__(self):
        super(additional, self).__init__()
        self.additional = additional_Ui_Form()
        self.additional.setupUi(self)

        self.db = DataBase()
        self.vehicle_list = self.db.getting(["*"], "vehicle", "simple")
        for i in range(0, len(self.vehicle_list), 1):
            self.additional.comboBox.addItem(f"{self.vehicle_list[i][1]} {self.vehicle_list[i][2]}, Гос. номер: {self.vehicle_list[i][3]}")
        self.additional.comboBox.activated[str].connect(self.getting_orders)

    def getting_orders(self, vehicle):
        # clear all item in Table
        self.additional.tableWidget.clearContents()
        self.additional.tableWidget.setRowCount(1)
        # Добавить в запрет вводить спецсимволы нижнее подчеркивание
        raw_vehicle_params: List = sub(", Гос. номер: ", "_", vehicle).split("_")
        split_vehicle_params: List = raw_vehicle_params[0].split(" ")

        # print(raw_vehicle_params, split_vehicle_params)

        if len(split_vehicle_params) == 3:
            loc_vehicle_params: List = [split_vehicle_params[0] + " " + split_vehicle_params[1], split_vehicle_params[2], raw_vehicle_params[1]]

        elif len(split_vehicle_params) == 2:
            loc_vehicle_params: List = [split_vehicle_params[0], split_vehicle_params[1], raw_vehicle_params[1]]

        loc_vehicle_id: str = self.db.getting(["*"], "vehicle", "custom", custom_body=f"WHERE VEHICLE_BRAND='{loc_vehicle_params[0]}' and "
                                                                                      f"VEHICLE_MODEL='{loc_vehicle_params[1]}' and REG_NUMBER='{loc_vehicle_params[2]}'")[0][0]
        orders_list: List[Tuple] = self.db.getting(["*"], "orders", "custom", custom_body=f"WHERE VEHICLE_ID={int(loc_vehicle_id)}")
        row_idx: int = 0
        row_num: int = 1
        for order in orders_list:
            _tmp_employee_response: List[Tuple] = self.db.getting(["*"], "employees", "custom", custom_body=f"WHERE ID={order[1]}")
            loc_employee_fullname = _tmp_employee_response[0][1] + " " + _tmp_employee_response[0][2] + " " + _tmp_employee_response[0][3]
            self.add_row_in_table([row_idx, row_num, loc_employee_fullname, order[5], order[6], order[4]])
            row_idx += 1
            if self.additional.tableWidget.rowCount() < len(orders_list):
                self.additional.tableWidget.setRowCount(row_num + 1)
            row_num += 1

    def add_row_in_table(self, item_data: List):
        for column in range(0, 4, 1):
            qtablewidgetitem = QTableWidgetItem(f"{item_data[column + 2]}")
            qtablewidgetitem.setTextAlignment(Qt.AlignCenter)
            qtablewidgetitem.setFlags(qtablewidgetitem.flags() ^ Qt.ItemIsEditable)
            qtablewidgetitem.setToolTip(f"{item_data[column + 2]}")
            self.additional.tableWidget.setItem(item_data[0], column, qtablewidgetitem)

    def closeEvent(self, event: QCloseEvent):
        self.db.__del__()
        event.accept()


class GUI_runner(QMainWindow):
    def __init__(self):
        super(GUI_runner, self).__init__()
        # Последний идентификатор заказа
        self.last_database_id: int = 0
        # Инициализация главного окна и дополнительных форм
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.about = AboutForm()
        self.ui.menu.triggered.connect(self.link_with_author)

        self.employees = Employees()
        self.ui.pushButton_3.clicked.connect(self.open_add_employee)
        self.employees.setWindowModality(Qt.ApplicationModal)

        self.createOrders = ""
        self.ui.pushButton_2.clicked.connect(self.open_create_orders_window)

        self.updateOrders = ""
        self.ui.pushButton.clicked.connect(self.open_update_orders_window)

        self.spravka = ""
        self.ui.pushButton_4.clicked.connect(self.open_spravka_window)

        self.additional = ""
        self.ui.pushButton_5.clicked.connect(self.open_additional_window)

    def link_with_author(self):
        self.about.exec_()

    def open_add_employee(self):
        self.employees = Employees()
        self.employees.show()

    def open_create_orders_window(self):
        self.createOrders = create_orders()
        self.createOrders.show()

    def open_update_orders_window(self):
        self.updateOrders = update_orders()
        self.updateOrders.show()

    def open_spravka_window(self):
        self.spravka = certificates()
        self.spravka.show()

    def open_additional_window(self):
        self.additional = additional()
        self.additional.show()


if __name__ == '__main__':
    app = QApplication(argv)
    window = GUI_runner()
    window.show()
    exit(app.exec_())
