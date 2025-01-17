import importlib
import os
import sys
from logging import exception
from time import sleep
from traceback import print_tb

from PyQt6 import QtGui
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QApplication

from common_lib.common_lib import init_log_file
from settings.setting_result_display import Ui_MainWindow
from settings.write_report import write_result_report

# Thêm đường dẫn đến common_lib vào hệ thống path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common_lib')))

class Worker(QThread):
    finished = pyqtSignal()  # Signal to indicate the thread is finished

    def __init__(self, target=None):
        super().__init__()
        self.target = target

    def run(self):
        if self.target:
            self.target()
        self.finished.emit()  # Emit the signal when the work is done

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.threads = {}  # Dictionary to manage threads
        self.testcase_name_report = []
        self.testcase_result_report = []

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

    # Function click run
    def on_btn_run_clicked(self):
        # self.list_of_testcase = ['setting_3', 'setting_4', 'setting_5', 'setting_12', 'setting_13', 'setting_18',
        #                          'setting_18', 'setting_22', 'setting_24', 'setting_31', 'setting_32',
        #                          'setting_33', 'setting_38', 'setting_41', 'setting_42', 'setting_43',
        #                          'setting_53', 'setting_54', 'setting_55', 'setting_57', 'setting_58',
        #                          'setting_60','setting_62','setting_63', 'setting_64', 'setting_67', 'setting_68'
        #                          'setting_69','setting_70','setting_71','setting_72', 'setting_74']
        self.list_of_testcase = ['control_center_6']
        self.current_index = 0
        self.run_next_testcase()

    # Function run next test case
    def run_next_testcase(self):
        if self.current_index < len(self.list_of_testcase):
            testcase = self.list_of_testcase[self.current_index]
            try:
                # Run thread init test case in table
                self.threads[self.current_index] = Worker(target=lambda: self.init_result(testcase, self.current_index, self.current_index))
                # Run thread handle
                self.threads[self.current_index].finished.connect(self.start_handle_result_thread)
                self.threads[self.current_index].start()
                print(f"Started init_result thread for testcase {testcase}")
            except Exception as e:
                print(f'Error click: {e}')

    # Function start handle
    def start_handle_result_thread(self):
        testcase = self.list_of_testcase[self.current_index]
        try:
            # run thread handle_result
            self.threads[self.current_index + 1] = Worker(target=lambda: self.handle_result(testcase, self.current_index, self.current_index))

            self.threads[self.current_index + 1].finished.connect(self.on_thread_finished)
            self.threads[self.current_index + 1].start()
            print(f"Started handle_result thread for testcase {testcase}")
        except Exception as e:
            print(f'Error handle: {e}')

    # Function finish handle result
    def on_thread_finished(self):
        print(f"Thread for testcase {self.list_of_testcase[self.current_index]} finished")
        print('curren index: ',self.current_index)
        self.current_index += 1
        if self.current_index < len(self.list_of_testcase) :
            print('curren index 2: ', self.current_index)
            print('list_of_testcase: ', len(self.list_of_testcase))
            self.run_next_testcase()

    # Function init test case result
    def init_result(self, testcase_name, row_index, col_index):
        global window, tableView
        item = QtGui.QStandardItem(f'{testcase_name}')
        model.setItem(row_index, 0, item)
        item = QtGui.QStandardItem('Running')
        model.setItem(row_index, 1, item)
        tableView.setModel(model)
        tableView.viewport().update()

    # Function reload row data
    def reload_row_data(self, result, row_index, col_index):
        global window, tableView
        item = QtGui.QStandardItem(f'{result}')
        model.setItem(row_index, 1, item)
        tableView.setModel(model)

    # Function handle result
    def handle_result(self, testcase_name, row_index, col_index):
        try:
            module_name = f'settings.{testcase_name}'
            module = importlib.import_module(module_name)
            testcase_function = getattr(module, testcase_name)
            result = testcase_function()
            print(f'result {testcase_name}: {result}')
            self.testcase_name_report.append(testcase_name)
            if result:
                self.testcase_result_report.append('Pass')
                self.reload_row_data('Pass', row_index, col_index)
            else:
                self.testcase_result_report.append('Fail')
                self.reload_row_data('Fail', row_index, col_index)
            print(self.testcase_name_report, self.testcase_result_report)
            write_result_report(self.testcase_name_report, self.testcase_result_report)
        except AttributeError:
            print(f'Lỗi xử lý: Hàm {testcase_name} không tồn tại trong module {module_name}.')
        except Exception as e:
            print(f'Lỗi xử lý: {e}')

if __name__ == "__main__":
    init_log_file()
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
