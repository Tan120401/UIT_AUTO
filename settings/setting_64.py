# Function Test case setting 64
from time import sleep

from pywinauto import Desktop

from common_lib.common_lib import open_app, click_object, get_connected_wifi, write_log_setting, close_app


def setting_64():
    # List result
    pass_list = []
    fail_list = []

    # Open app settings
    target_window = open_app('Settings')
    is_network = click_object(target_window, 'Network & internet', '', 'ListItem')

    # Kết nối với desktop
    desktop = Desktop(backend="uia")

    # Tìm thanh Taskbar
    taskbar = desktop.window(class_name="Shell_TrayWnd")

    is_wifi = target_window.child_window(title="Wi-Fi", auto_id="SystemSettings_Network_Wifi_QuickAction_ToggleSwitch", control_type="Button")
    if is_wifi.exists():
        is_wifi_state = is_wifi.get_toggle_state()
        sleep(5)
        if is_wifi_state == 0:
            is_wifi.click_input()
            sleep(15)
            is_wifi_state = is_wifi.get_toggle_state()
        if is_wifi_state == 1:
            connected_wifi = get_connected_wifi()

            # Icon wifi connected in task bar
            is_icon_wifi = taskbar.child_window(title=f"Network {connected_wifi}\nInternet access",
                                                auto_id="SystemTrayIcon", control_type="Button")
            sleep(2)
            if is_icon_wifi.exists():
                pass_list.append('Wifi connected and icon is match')
            else:
                fail_list.append('Wifi connected and icon is not match')
            is_wifi.click_input()
            sleep(15)

            # Icon global network not connected
            is_icon_global = taskbar.child_window(title="Network No internet access\nNo connections available",
                                                  auto_id="SystemTrayIcon", control_type="Button")
            if is_icon_global.exists():
                pass_list.append('Wifi not connected and icon is match')
            else:
                fail_list.append('Wifi not connected and icon is not match')
            is_wifi.click_input()
            sleep(15)
    else:
        fail_list.append(is_wifi.window_text())

    # Write log setting
    write_log_setting('Setting 64', pass_list, fail_list)
    # close window
    close_app('Settings')
    if len(fail_list) > 0:
        return False
    elif len(pass_list) > 0:
        return True
