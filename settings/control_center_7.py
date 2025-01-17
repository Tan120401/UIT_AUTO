# Tìm thanh Taskbar
from time import sleep

from pywinauto import Desktop

from common_lib.common_lib import get_connected_wifi, click_object, find_object, write_log_setting

def control_center_7():
    # List of result
    pass_list = []
    fail_list = []

    desktop = Desktop(backend="uia")
    taskbar = desktop.window(class_name="Shell_TrayWnd")

    connected_wifi = get_connected_wifi()

    is_icon_wifi = click_object(taskbar, f"Network {connected_wifi}\nInternet access", 'SystemTrayIcon', 'Button')

    quick_setting = desktop.window(title="Quick settings")
    # print(quick_setting.print_control_identifiers())

    is_all_setting_icon = click_object(quick_setting,'All settings', 'Microsoft.QuickAction.AllSettings', 'Button')

    object_list = [is_icon_wifi, is_all_setting_icon]
    for obj in object_list:
        if obj[0]:
            pass_list.append(obj[1])
        else:
            fail_list.append(obj[1])

    all_window_active = Desktop(backend='uia').windows()
    for win in all_window_active:
        if win.window_text() == 'Settings':
            sleep(2)
            win.close()
            pass_list.append('All setting select')

    write_log_setting('Control center 7', pass_list, fail_list)

    if len(fail_list) > 0:
        return False
    elif len(pass_list) > 0:
        return True

control_center_7()
