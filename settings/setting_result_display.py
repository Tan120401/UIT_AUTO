# Form implementation generated from reading ui file 'setting_result_display.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 689)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 140, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.runBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.runBtn.setGeometry(QtCore.QRect(20, 50, 111, 41))
        self.runBtn.setObjectName("runBtn")
        self.stopBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(160, 50, 111, 41))
        self.stopBtn.setObjectName("stopBtn")
        self.tableResult = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableResult.setGeometry(QtCore.QRect(20, 180, 560, 450))
        self.tableResult.setObjectName("tableResult")
        self.exitBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(300, 50, 111, 41))
        self.exitBtn.setObjectName("exitBtn")
        self.openlogBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.openlogBtn.setGeometry(QtCore.QRect(450, 50, 111, 41))
        self.openlogBtn.setObjectName("openlogBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test result"))
        self.label.setText(_translate("MainWindow", "Test Result Settings"))
        self.runBtn.setText(_translate("MainWindow", "Run"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.openlogBtn.setText(_translate("MainWindow", "Open Log"))
