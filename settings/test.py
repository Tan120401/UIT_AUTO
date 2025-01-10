import sys
from time import sleep
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtGui

from setting_result_display import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

        self.threads = {}  # Dictionary to manage threads

    def init_ui(self):
        global tableView, model

        # Init table
        tableView = self.ui.tableResult
        self.ui.runBtn.clicked.connect(self.on_btn_run_clicked)

        num_col = 2
        model = QtGui.QStandardItemModel(0, num_col)
        model.setHorizontalHeaderLabels(['Test Case Name', 'Result'])
        header = tableView.horizontalHeader()
        header.setDefaultSectionSize(278)
        tableView.setModel(model)

    def on_btn_run_clicked(self):
        self.threads[1] = Worker(index=1, target=self.init_result)
        # self.threads[2] = Worker(index=2, target=self.handle_result)

        # self.threads[1].signal.connect(self.my_function)
        # self.threads[2].signal.connect(self.my_function)

        self.threads[1].start()
        # self.threads[2].start()

    def my_function(self, index):
        print(f"Thread {index} has finished")

    def init_result(self):
        print('thread init')
        global window, tableView
        item = QtGui.QStandardItem('Setting 3')
        model.setItem(0, 0, item)
        item = QtGui.QStandardItem('Running')
        model.setItem(0, 1, item)
        tableView.setModel(model)
        tableView.viewport().update()

    def handle_result(self):
        print('thread handle')
        sleep(4)

class Worker(QThread):
    signal = pyqtSignal()

    def __init__(self, index=0, target=None):
        super().__init__()
        self.index = index
        self.target = target

    def run(self):
        print('Start thread ... ', self.index)
        if self.target:
            self.target()
        self.signal.emit(self.index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
