# Function Test case setting 69
from time import sleep

from pywinauto import Desktop

from common_lib.common_lib import open_app, get_connected_wifi, write_log_setting, close_app


def setting_70():
    # List result
    pass_list = []
    fail_list = []

    target_window = open_app('Settings')

    # Kết nối với desktop
    desktop = Desktop(backend="uia")

    # Tìm thanh Taskbar
    taskbar = desktop.window(class_name="Shell_TrayWnd")

    is_network = target_window.child_window(title='Network & internet', control_type='ListItem')
    if is_network.exists():
        is_network.click_input()
        sleep(2)
    else:
        fail_list.append('Network & internet')
    # airplane mode button
    is_airplane_mode = target_window.child_window(title="Airplane Mode", auto_id="SystemSettings_Radio_IsAirplaneModeEnabled_ToggleSwitch", control_type="Button")
    if is_airplane_mode.exists():
        is_airplane_mode_state = is_airplane_mode.get_toggle_state()

        # Set airplane is ON
        if is_airplane_mode_state == 0:
            is_airplane_mode.click_input()
            sleep(10)
        is_airplane_mode_state = is_airplane_mode.get_toggle_state()
        if is_airplane_mode_state == 1:
            is_airplane_mode_icon = taskbar.child_window(title="Network No internet access\nAirplane mode",
                                                         auto_id="SystemTrayIcon", control_type="Button")
            if is_airplane_mode_icon.exists():
                pass_list.append('Airplane mode is ON -> icon is match')
            else:
                fail_list.append('Airplane mode is ON -> icon is not match')
            # Set airplane mode is OFF
            is_airplane_mode.click_input()
            sleep(10)
        is_airplane_mode_state = is_airplane_mode.get_toggle_state()
        if is_airplane_mode_state == 0:
            connected_wifi = get_connected_wifi()
            is_icon_wifi = taskbar.child_window(title=f"Network {connected_wifi}\nInternet access",
                                                auto_id="SystemTrayIcon", control_type="Button")
            if is_icon_wifi.exists():
                pass_list.append('Airplane mode is OFF -> icon is match')
            else:
                fail_list.append('Airplane mode is OFF -> icon is not match')
    else:
        fail_list.append('Airplane Mode')
    # Write log setting
    write_log_setting('Setting 70', pass_list, fail_list)

    # close window
    close_app('Settings')
    if len(fail_list) > 0:
        return False
    elif len(pass_list) > 0:
        return True
