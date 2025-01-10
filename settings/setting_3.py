import sys
import threading
from time import sleep

import timer
from PyQt6 import uic
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6.QtCore import QTimer, QThread, pyqtSignal

from common_lib.common_lib import base_setting

# Function test case setting 3
def setting_3():
    # dictionaries
    dic_of_objects = {
        'title': 'Find a setting, Home, System, Bluetooth & devices, Network & internet, Personalization, Apps, Accounts, '
                 'Time & language, Gaming, Accessibility, Privacy & security, Windows Update',
        'auto_id': ', , , , , , , , , , , , ',
        'control_type': 'Text, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem',
        'object_handle': 'view, view, view, view, view, view, view, view, view, view, view, view, view'
    }
    result = base_setting("Setting 3", "Settings", dic_of_objects)
    return result

class Worker(QThread):
    finished = pyqtSignal()
    def __init__(self, target):
        super().__init__()
        self.target = target
        print(f'Worker initialized with target: {target.__name__}')
    def run(self):
        try:
            print('abc')
            print('thread', self.target.__name)
            self.target()
            self.finished.emit()
            print('thread finished', self.target.__name)
        except Exception as e:
            print(f'Error: {e}')

# Function reload result on table
def reload_table(result):
    global window, tableView
    item = QtGui.QStandardItem(f'{result}')
    model.setItem(0, 1, item)
    tableView.setModel(model)
    print('reload')

def on_thread_finished():
    print("success")

# Function click btnRun
def on_btn_run_clicked():
    try:
        print('button click')
        thread1 = Worker(target=init_result)
        thread2 = Worker(target=handle_result)
        thread1.finished.connect(on_thread_finished)
        thread1.start()
        print('thread 1 started')

        thread2.finished.connect(on_thread_finished)
        thread2.start()
        print('thread 2 started')
    except Exception as e:
        print(f'Error: {e}')

def init_result():
    # global window, tableView
    # item = QtGui.QStandardItem('Setting 3')
    # model.setItem(0, 0, item)
    # item = QtGui.QStandardItem('Running')
    # model.setItem(0, 1, item)
    # tableView.setModel(model)
    # tableView.viewport().update()
    print('init')

def handle_result():
    print('handle')
    # try:
    #     result = True
    #     sleep(2)
    #     # QTimer.singleShot(2000, lambda: reload_table('pass'))
    #     # reload_table('pass')
    #     # if result:
    #     print('handle')
    #     # else:
    #     #     QTimer.singleShot(2000, lambda: reload_table('fail'))
    # except Exception as e:
    #     print(f'Error: {e}')

# Initialize UI
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("setting_result_display.ui")

# Initialize table
tableView = window.findChild(QtWidgets.QTableView, 'tableResult')
btnRun = window.findChild(QtWidgets.QPushButton, 'runBtn')
btnRun.clicked.connect(on_btn_run_clicked)

num_col = 2
model = QtGui.QStandardItemModel(0, num_col)
model.setHorizontalHeaderLabels(['Test Case Name', 'Result'])
header = tableView.horizontalHeader()
header.setDefaultSectionSize(278)

tableView.setModel(model)
window.show()

app.exec()

