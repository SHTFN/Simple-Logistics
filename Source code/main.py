import sys
import sqlite3
from pathlib import Path
from sys import argv
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLineEdit, QDateEdit, QFileDialog
from PyQt5.QtCore import QDate
from addFlightNote import Ui_addFlightNote
from editFlightNote import Ui_editFlightNote
from mainUI import Ui_MainWindow
import ui.icons


# Открытие окна редактирования записи
def openEditNoteWindow():
    DialogWindow = EditFlightNoteDialog()
    DialogWindow.show()
    DialogWindow.exec()


# Открытие окна создания новой записи
def openAddNewNoteWindow():
    DialogWindow = AddFlightNoteDialog()
    DialogWindow.show()
    DialogWindow.exec()


# Главное окно
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('Simple Logistics')

        # Путь к текущей директории файлов
        script_dir = Path(argv[0]).parent.resolve()

        self.statusbar.showMessage('Не забывайте обновлять талицу после каждого изменения!')

        # Подключение к базе данных
        db_path = script_dir / 'flightsDB.sqlite'
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()

        # Подключение функций к QPushButton и QAction
        self.addNoteButton.clicked.connect(openAddNewNoteWindow)
        self.editNoteButton.clicked.connect(openEditNoteWindow)
        self.deleteNoteButton.clicked.connect(self.deleteNote)
        self.updateTableButton.clicked.connect(self.selectData)
        self.exportTable.triggered.connect(self.exportToCSV)

        self.selectData()

    def exportToCSV(self):  # Экспорт таблицы в .csv файл
        response = QFileDialog.getSaveFileName(self,
                                               'Экспорт таблицы',
                                               'table.csv',
                                               'All Files (*)',
                                               options=QFileDialog.Options())
        if response != ('', ''):
            with open(response[0], 'w', newline='') as csvfile:
                writer = csv.writer(
                    csvfile, delimiter=';', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)
                writer.writerow(
                    [self.tableWidget.horizontalHeaderItem(i).text()
                     for i in range(self.tableWidget.columnCount())])
                for i in range(self.tableWidget.rowCount()):
                    row = []
                    for j in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(i, j)
                        if item is not None:
                            row.append(item.text())
                    writer.writerow(row)

    def close(self):
        self.close()

    def selectData(self):  # Чтение данных таблицы из базы данных
        query = "SELECT * FROM flights"
        res = self.cur.execute(query).fetchall()
        title = ['Номер загрузки', 'Дата загрузки', 'Дата выгрузки', 'Точка загрузки', 'Точка выгрузки',
                 'Цена загрузки', 'Простой\nзагрузки', 'ФИО водителя', 'Зарплата\nводителя',
                 'Простой водителя', 'Траты на топливо', 'Доп. траты']
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setRowCount(0)

        # Заполнение QTableWidget
        self.tableWidget.setHorizontalHeaderLabels(title)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def deleteNote(self):  # Удаление записи из таблицы и БД
        idValue = self.idSpinBox.value()
        query = "DELETE FROM flights WHERE id = ?"
        self.cur.execute(query, (idValue,))
        self.con.commit()


# Окно добавления новой записи
class AddFlightNoteDialog(Ui_addFlightNote):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.acceptButton.clicked.connect(self.insertAndSaveNewNote)
        self.rejectButton.clicked.connect(self.close)

        # Подключение к БД
        script_dir = Path(argv[0]).parent.resolve()
        db_path = script_dir / 'flightsDB.sqlite'
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()

    def insertAndSaveNewNote(self):  # Сохранение новой записи в БД
        try:
            values = []
            for row in range(self.gridLayout.rowCount()):
                for col in range(self.gridLayout.columnCount()):
                    item = self.gridLayout.itemAtPosition(row, col).widget()
                    if isinstance(item, QLineEdit):
                        values.append(item.text())
                    elif isinstance(item, QDateEdit):
                        values.append(item.date().toString('dd.MM.yyyy'))  # Если item это QDateEdit,
                        # то получаем из него дату и конвертируем в str
            try:
                values.append(int(values[1]) * 0.3)  # Подсчет значения driversDowntime
            except ValueError:
                values.append('')
            self.cur.execute(
                "INSERT INTO flights (departureDate, downtime, arrivalDate, driversFullName, departurePoint, driversSalary,"
                "arrivalPoint, fuelConsumption, price, additionalExpenses, driversDowntime) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                tuple(values)
            )
            self.con.commit()
            self.close()
        except AttributeError:
            self.close()


# Окно редактирования записей
class EditFlightNoteDialog(Ui_editFlightNote):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.acceptButton.clicked.connect(self.insertAndSaveNewNote)
        self.rejectButton.clicked.connect(self.close)
        self.idSpinBox.valueChanged.connect(self.changeInputObj)

        # Подключение к БД
        script_dir = Path(argv[0]).parent.resolve()
        db_path = script_dir / 'flightsDB.sqlite'
        self.con = sqlite3.connect(db_path)
        self.cur = self.con.cursor()

    # Получение отредактированной записи по ID
    def changeInputObj(self):
        query = "SELECT * FROM flights WHERE id = ?"
        self.res = self.cur.execute(query, (int(self.idSpinBox.value()),)).fetchall()  # Получение значений из QLineEdit

        try:
            self.res = list(self.res[0])
        except IndexError:
            self.res = self.res
        if len(self.res) == 0:
            self.flightStatusLabel.setText('Запись по данному ID не найдена')
            self.departureDateEdit.setDate(QDate.fromString('01.01.2000', 'dd.MM.yyyy'))
            self.arrivalDateEdit.setDate(QDate.fromString('01.01.2000', 'dd.MM.yyyy'))
            self.departurePointEdit.setText('')
            self.arrivalPointEdit.setText('')
            self.priceEdit.setText('')
            self.downtimeEdit.setText('')
            self.driversFullNameEdit.setText('')
            self.driversSalaryEdit.setText('')
            self.fuelConsumptionEdit.setText('')
            self.additionalExpensesEdit.setText('')
        else:
            del self.res[9]
            self.flightStatusLabel.setText('По данному ID была найдена такая запись')
            self.departureDateEdit.setDate(QDate.fromString(self.res[1], 'dd.MM.yyyy'))
            self.arrivalDateEdit.setDate(QDate.fromString(self.res[2], 'dd.MM.yyyy'))
            self.departurePointEdit.setText(self.res[3])
            self.arrivalPointEdit.setText(self.res[4])
            self.priceEdit.setText(str(self.res[5]))
            self.downtimeEdit.setText(str(self.res[6]))
            self.driversFullNameEdit.setText(self.res[7])
            self.driversSalaryEdit.setText(str(self.res[8]))
            self.fuelConsumptionEdit.setText(str(self.res[9]))
            self.additionalExpensesEdit.setText(str(self.res[10]))
            if self.downtimeEdit.text() != '' and self.downtimeEdit.text() != 'None':
                self.res.insert(9, int(self.res[6]) * 0.3)
            else:
                self.res.insert(9, '')

    def insertAndSaveNewNote(self):  # Сохранение отредактированной записи в БД
        try:
            self.res = self.res[1:] + self.res[:1]
            values = [self.departureDateEdit.date().toString('dd.MM.yyyy'),
                      self.arrivalDateEdit.date().toString('dd.MM.yyyy'), self.departurePointEdit.text(),
                      self.arrivalPointEdit.text(), self.priceEdit.text(), self.downtimeEdit.text(),
                      self.driversFullNameEdit.text(), self.driversSalaryEdit.text()]
            if self.downtimeEdit.text() != '':
                values.append(int(self.downtimeEdit.text()) * 0.3)
            else:
                values.append(self.downtimeEdit.text())
            values.append(self.fuelConsumptionEdit.text())
            values.append(self.additionalExpensesEdit.text())
            values.append(int(self.idSpinBox.value()))
            self.cur.execute(
                "UPDATE flights"
                "   SET departureDate = ?,"
                "arrivalDate = ?,"
                "departurePoint = ?,"
                "arrivalPoint = ?,"
                "price = ?,"
                "downtime = ?,"
                "driversFullName = ?,"
                "driversSalary = ?,"
                "driversDowntime = ?,"
                "fuelConsumption = ?,"
                "additionalExpenses = ?"
                "WHERE id = ?",
                tuple(values)
            )
            self.con.commit()
            self.close()
        except AttributeError:
            self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.setFixedSize(1540, 640)
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
