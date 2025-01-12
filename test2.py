import sys
from time import sleep

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import pyqtSignal, QThread, QTimer
from PyQt6 import QtGui

from common_lib.common_lib import base_setting
from setting_result_display import Ui_MainWindow

def setting_3():
    # dictionaries
    dic_of_objects = {
        'title': 'Find a setting, Home, System',
        'auto_id': ', , ',
        'control_type': 'Text, ListItem, ListItem',
        'object_handle': 'view, view, view'
    }
    result = base_setting("Setting 3", "Settings", dic_of_objects)
    return result

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
        self.threads[2] = Worker(index=2, target=self.handle_result)

        self.threads[1].signal.connect(self.my_function)
        self.threads[2].signal.connect(self.my_function)

        self.threads[1].start()
        self.threads[2].start()

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

    # Function reload result on table
    def reload_table(self, result):
        global window, tableView
        item = QtGui.QStandardItem(f'{result}')
        model.setItem(0, 1, item)
        tableView.setModel(model)

    def handle_result(self):
        print('thread handle')
        try:
            result = setting_3()
            sleep(2)
            if result:
                self.reload_table('Pass')
            else:
               self.reload_table('Fail')
        except Exception as e:
            print(f'Error: {e}')

class Worker(QThread):
    signal = pyqtSignal(int)  # Signal with an integer argument

    def __init__(self, index=0, target=None):
        super().__init__()
        self.index = index
        self.target = target

    def run(self):
        print('Start thread ... ', self.index)
        if self.target:
            self.target()
        self.signal.emit(self.index)  # Emit the signal with index

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
