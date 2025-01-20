# Tìm thanh Taskbar
from time import sleep

from pywinauto import Desktop

from common_lib.common_lib import get_connected_wifi, click_object, find_object, write_log_setting

def control_center_6():
    try:
        # List of result
        pass_list = []
        fail_list = []

        desktop = Desktop(backend="uia")
        taskbar = desktop.window(class_name="Shell_TrayWnd")

        connected_wifi = get_connected_wifi()

        is_wifi = click_object(taskbar, f"Network {connected_wifi}\nInternet access", 'SystemTrayIcon', 'Button')

        quick_setting = desktop.window(title="Quick settings")

        is_manage_wifi = click_object(quick_setting, 'Manage Wi-Fi connections', 'SplitL2Button', 'Button')

        is_wifi_list = find_object(quick_setting, '', 'SystemSettings_Connections_Adapter_Wi-Fi_Wi-Fi_ListView', 'List')

        object_list = [is_wifi, is_manage_wifi]
        for obj in object_list:
            if obj[0]:
                pass_list.append(obj[1])
            else:
                fail_list.append(obj[1])

        # get all element
        child_elements = is_wifi_list[2].descendants(control_type='ListItem')
        wifi_list = []
        # find elements
        for element in child_elements:
            element_text = element.window_text().split(', ')
            # print(element_text[0])
            wifi_list.append(element_text[0])

        if len(wifi_list) > 0:
            pass_list.append('AP items can be connected are show')
        else:
            fail_list.append("AP items can be connected aren't show")

        is_wifi[2].click_input()

        write_log_setting('Control center 6', pass_list, fail_list)
        if len(fail_list) > 0:
            return False
        elif len(pass_list) > 0:
            return True
    except Exception as e:
        print(f'Control center 8  error: {e}')

