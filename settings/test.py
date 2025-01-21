import importlib
import os
import sys

from PyQt6 import QtGui
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout

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
        self._is_running = True  # Cờ để kiểm soát việc chạy luồng

    def run(self):
        if self.target:
            self.target()
        self.finished.emit()

    def stop(self):
        self._is_running = False  # Đặt cờ thành False để dừng luồng

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.threads = []  # List to manage threads
        self.testcase_name_report = []
        self.testcase_result_report = []

    def init_ui(self):
        global tableView, model

        # Init table
        tableView = self.ui.tableResult
        self.ui.runBtn.clicked.connect(self.on_btn_run_clicked)
        self.ui.stopBtn.clicked.connect(self.on_btn_stop_clicked)
        self.ui.stopBtn.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(tableView)
        layout.addWidget(self.ui.runBtn)
        layout.addWidget(self.ui.stopBtn)
        self.setLayout(layout)

        num_col = 2
        model = QtGui.QStandardItemModel(0, num_col)
        model.setHorizontalHeaderLabels(['Test Case Name', 'Result'])
        header = tableView.horizontalHeader()
        header.setDefaultSectionSize(278)
        tableView.setModel(model)

    # Function click run
    def on_btn_run_clicked(self):
        self.clear_table_data()  # Xóa dữ liệu trên bảng trước khi chạy lại
        self.ui.runBtn.setEnabled(False)
        self.ui.stopBtn.setEnabled(True)
        self.ui.openlogBtn.setEnabled(False)
        self.list_of_testcase = ['control_center_6', 'control_center_7', 'control_center_12', 'control_center_16', 'control_center_21', 'control_center_8']
        self.current_index = 0
        self.run_next_testcase()

    # Function click stop
    def on_btn_stop_clicked(self):
        self.stop_all_threads()
        self.ui.runBtn.setEnabled(True)
        self.ui.stopBtn.setEnabled(False)

    def stop_all_threads(self):
        for thread in self.threads:
            print(thread)
            thread.stop()
        self.threads.clear()

    # Function clear table data
    def clear_table_data(self):
        global model
        model.removeRows(0, model.rowCount())

    # Function run next test case
    def run_next_testcase(self):
        if self.current_index < len(self.list_of_testcase):
            testcase = self.list_of_testcase[self.current_index]
            try:
                thread = Worker(target=lambda: self.init_result(testcase, self.current_index, self.current_index))
                self.threads.append(thread)
                thread.finished.connect(self.start_handle_result_thread)
                thread.start()
                print(f"Started init_result thread for testcase {testcase}")
            except Exception as e:
                print(f'Error click: {e}')

    # Function start handle
    def start_handle_result_thread(self):
        if self.current_index >= len(self.threads) or not self.threads[self.current_index]._is_running:
            return
        testcase = self.list_of_testcase[self.current_index]
        try:
            thread = Worker(target=lambda: self.handle_result(testcase, self.current_index, self.current_index))
            self.threads.append(thread)
            thread.finished.connect(self.on_thread_finished)
            thread.start()
            print(f"Started handle_result thread for testcase {testcase}")
        except Exception as e:
            print(f'Error handle: {e}')

    # Function finish handle result
    def on_thread_finished(self):
        print(f"Thread for testcase {self.list_of_testcase[self.current_index]} finished")
        self.current_index += 1
        if self.current_index < len(self.list_of_testcase):
            self.run_next_testcase()
        else:
            self.ui.runBtn.setEnabled(True)
            self.ui.stopBtn.setEnabled(False)

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
