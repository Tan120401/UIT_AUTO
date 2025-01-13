import importlib
import sys
from logging import exception
from time import sleep
from traceback import print_tb

from PyQt6 import QtGui
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QApplication

from common_lib.common_lib import init_log_file
from settings.setting_result_display import Ui_MainWindow

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
        self.list_of_testcase = ['setting_3', 'setting_4']
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
        self.current_index += 1
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
            sleep(2)
            print(f'result {testcase_name}: {result}')
            if result:
                self.reload_row_data('Pass', row_index, col_index)
            else:
                self.reload_row_data('Fail', row_index, col_index)
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
