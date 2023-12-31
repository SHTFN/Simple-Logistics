# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1540, 662)
        MainWindow.setStyleSheet("QMainWindow {\n"
"     background-color: #707070;\n"
"    border-radius: 5px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 498, 1521, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addNoteButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addNoteButton.sizePolicy().hasHeightForWidth())
        self.addNoteButton.setSizePolicy(sizePolicy)
        self.addNoteButton.setStyleSheet("QPushButton{\n"
"    color: #FAFAFA;\n"
"    background-color: #939393;\n"
"    border-radius:6px;\n"
"    height: 25px;\n"
"    font: 10pt \"Comfortaa\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #888888;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #888888;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/add/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addNoteButton.setIcon(icon)
        self.addNoteButton.setObjectName("addNoteButton")
        self.horizontalLayout.addWidget(self.addNoteButton)
        self.editNoteButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.editNoteButton.setStyleSheet("QPushButton{\n"
"    color: #FAFAFA;\n"
"    background-color: #939393;\n"
"    border-radius:6px;\n"
"    height: 25px;\n"
"    font: 10pt \"Comfortaa\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #888888;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #888888;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/edit/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editNoteButton.setIcon(icon1)
        self.editNoteButton.setObjectName("editNoteButton")
        self.horizontalLayout.addWidget(self.editNoteButton)
        self.updateTableButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.updateTableButton.setStyleSheet("QPushButton{\n"
"    color: #FAFAFA;\n"
"    background-color: #939393;\n"
"    border-radius:6px;\n"
"    height: 25px;\n"
"    font: 10pt \"Comfortaa\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #888888;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #888888;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/update/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updateTableButton.setIcon(icon2)
        self.updateTableButton.setObjectName("updateTableButton")
        self.horizontalLayout.addWidget(self.updateTableButton)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(9, 9, 1521, 481))
        self.tableWidget.setStyleSheet("background-color: #FAFAFA;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(10, 570, 21, 21))
        self.idLabel.setStyleSheet("color: #FAFAFA;")
        self.idLabel.setObjectName("idLabel")
        self.idSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.idSpinBox.setEnabled(True)
        self.idSpinBox.setGeometry(QtCore.QRect(29, 570, 1501, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idSpinBox.sizePolicy().hasHeightForWidth())
        self.idSpinBox.setSizePolicy(sizePolicy)
        self.idSpinBox.setMaximum(100000)
        self.idSpinBox.setObjectName("idSpinBox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 540, 1521, 27))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.deleteNoteButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.deleteNoteButton.setEnabled(True)
        self.deleteNoteButton.setStyleSheet("QPushButton{\n"
"    color: #FAFAFA;\n"
"    background-color: #939393;\n"
"    border-radius:6px;\n"
"    height: 25px;\n"
"    font: 10pt \"Comfortaa\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #888888;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #888888;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/bin/bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteNoteButton.setIcon(icon3)
        self.deleteNoteButton.setObjectName("deleteNoteButton")
        self.horizontalLayout_2.addWidget(self.deleteNoteButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1540, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("color: #FAFAFA;")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exportTable = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/export/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportTable.setIcon(icon4)
        self.exportTable.setObjectName("exportTable")
        self.closeProgram = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/cancel/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeProgram.setIcon(icon5)
        self.closeProgram.setObjectName("closeProgram")
        self.menu.addAction(self.exportTable)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addNoteButton.setText(_translate("MainWindow", "Добавить"))
        self.editNoteButton.setText(_translate("MainWindow", "Редактировать"))
        self.updateTableButton.setText(_translate("MainWindow", "Обновить таблицу"))
        self.idLabel.setText(_translate("MainWindow", " ID"))
        self.deleteNoteButton.setText(_translate("MainWindow", "Удалить"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.exportTable.setText(_translate("MainWindow", "Экспорт таблицы в .csv"))
        self.exportTable.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.closeProgram.setText(_translate("MainWindow", "Закрыть программу"))
import ui.icons
