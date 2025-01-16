import codecs
import os
from time import sleep
import subprocess

import pyautogui
from AppOpener import open
from pywinauto import Application, Desktop

# The list contain information show on UI
result_of_testcase = []

# Function to write logs
def write_log_setting(testcase_name,pass_list, fail_list):
    # Open log file and write
    with codecs.open("setting_logs.txt", "a", "utf-8") as file:
        file.write(f"*{testcase_name.upper()}\n")
        file.write("-List of pass: ")
        file.write(", ".join(pass_list))
        file.write("\n")
        if len(fail_list) > 0:
            result_of_testcase.append(f"-{testcase_name}: Fail")
            file.write("-List of fail: ")
            file.write(", ".join(fail_list))
            # for fail_ob in fail_list:
            #    file.write(f"{fail_ob}, ")
            file.write("\n")
        else:
            result_of_testcase.append(f"-{testcase_name}: Pass")

# Function init log file
def init_log_file():
    log_file = "setting_logs.txt"

    # check setting log exists
    if os.path.exists(log_file):
        try:
            # delete file
            os.remove(log_file)
            print(f"Deleted existing log file: {log_file}")
        except Exception as e:
            print(f"Error deleting log file: {e}")
    try:
        # Khởi tạo lại file log
        with codecs.open(log_file, "w", "utf-8") as file:
            file.write("")  # Tạo file rỗng
        print(f"Initialized new log file: {log_file}")
    except Exception as e:
        print(f"Error initializing log file: {e}")

# Function to check if objects exist
def base_setting(testcase_name, app_name, dic_object_list):
    # Open app settings
    target_window = open_app(f"{app_name}")
    # Change title, control type, auto_id, object_handle to List
    titles = dic_object_list['title'].split(', ')
    control_types = dic_object_list['control_type'].split(', ')
    auto_ids = dic_object_list['auto_id'].split(', ')
    object_handles = dic_object_list['object_handle'].split(', ')

    # The List contains the pass fail objects
    pass_list = []
    fail_list = []
    # Check that the lengths of the lists match
    if len(titles) == len(control_types) == len(auto_ids) == len(object_handles):
        for title, auto_id, control_type, object_handle in zip(titles, auto_ids, control_types, object_handles):
            object_result =[]
            if object_handle == 'click':
                object_result = click_object(target_window, title, auto_id, control_type)
            elif object_handle == 'view':
                object_result = find_object(target_window, title, auto_id, control_type)
            elif object_handle == 'scroll':
                scroll_center(target_window, title, auto_id, control_type)
                object_result = find_object(target_window, title, auto_id, control_type)
            print(object_result)
            if object_result[0]:
                pass_list.append(title)
            else:
                fail_list.append(title)
    else:
        print("Dic object list not match")

    write_log_setting(testcase_name, pass_list, fail_list)
    # close window
    close_app('Settings')

    if len(fail_list) > 0:
        return False
    elif len(pass_list) >0:
        return True

# Move to object and scroll
def scroll_center(target_window, title, auto_id, control_type):
    scroll_bar = target_window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    scroll_bar_rec = scroll_bar.rectangle()
    pyautogui.moveTo(scroll_bar_rec.left + 20, scroll_bar_rec.top - 20)
    sleep(2)
    pyautogui.scroll(-800)
    sleep(2)

# Function close app
def close_app(app_name):
    app = Application(backend='uia').connect(title_re=app_name)
    target_window = app.window(title_re=app_name)
    target_window.close()

# Function open app return target windows
def open_app(app_name):
    open(app_name, match_closest=False)
    sleep(5)
    app = Application(backend='uia').connect(title_re=app_name)
    target_window = app.window(title_re=app_name)
    return target_window

# Function click object exist
def click_object(window, title, auto_id, control_type):
    object_select = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    if object_select.exists():
        object_select.click_input()
        result = [True,title, object_select]
    else:
        result = [False, title, None]
    print(window.print_control_identifiers())
    sleep(3)
    return result

    # try:
    #     object_select = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    #     if object_select.exists():
    #         object_select.click_input()
    #         logging.info(f"Clicked on the object: {title}")
    #     else:
    #         logging.warning(f"Object not found: {title}")
    #         object_select = title
    # except Exception as e:
    #     logging.error(f"An error occurred: {e}")
    #     object_select = None
    # sleep(2)
    # return object_select

# Function find object
def find_object(window, title, auto_id, control_type):
    object_find = window.child_window(title=title, auto_id=auto_id, control_type=control_type)
    if not object_find.exists():
        result = [False, title, None ]
    else:
        result = [True, title, object_find]
    # sleep(2)
    return result

# Function click object by coordinates
def click_object_by_coordinates(left, top, right, bottom):
    # Define BoundingRectangle
    bounding_rectangle = {'l': left, 't': top, 'r': right, 'b': bottom}

    # Calculate the central coordinates
    center_x = (bounding_rectangle['l'] + bounding_rectangle['r']) // 2
    center_y = (bounding_rectangle['t'] + bounding_rectangle['b']) // 2

    # Move to the central coordinates and click
    pyautogui.moveTo(center_x, center_y)
    pyautogui.click()

# Function to find open windows
def find_open_window(app):
    # List all window
    all_window_active = Desktop(backend='uia').windows()
    is_app = False
    for win in all_window_active:
        if win.window_text() == app:
           is_app = True
           sleep(2)
           win.close()
    return is_app

# Function connected Wi-Fi
def get_connected_wifi():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
        result = result.decode("utf-8", errors="ignore")
        for line in result.split('\n'):
            if "SSID" in line:
                ssid = line.split(":")[1].strip()
                return ssid
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function click element in group
def click_object_within_group(group, name, auto_id, control_type):
    # get all element
    child_elements = group.descendants(control_type=control_type)
    print(child_elements)
    # find elements
    for element in child_elements:
        print(element.window_text())
        if element.window_text() == name and element.automation_id() == auto_id:
            print(element.window_text())
            return element.click_input()
    return False

# target_window = _open_app('Settings')
# object = target_window.child_window(title='Accessibility', auto_id='', control_type='ListItem')
# object.click_input()