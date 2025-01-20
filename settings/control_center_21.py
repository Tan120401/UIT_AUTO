from time import sleep

from pywinauto import Desktop

from common_lib.common_lib import get_connected_wifi, click_object, scroll_center, write_log_setting, find_object


def control_center_21():
    try:
        # List of result
        pass_list = []
        fail_list = []

        desktop = Desktop(backend="uia")
        taskbar = desktop.window(class_name="Shell_TrayWnd")
        connected_wifi = get_connected_wifi()

        is_wifi = click_object(taskbar, f"Network {connected_wifi}\nInternet access", 'SystemTrayIcon', 'Button')

        quick_setting = desktop.window(title="Quick settings")

        is_bluetooth_icon = find_object(quick_setting, "Bluetooth", 'Microsoft.QuickAction.Bluetooth', 'Button')

        if is_bluetooth_icon[0]:
            bluetooth_state = is_bluetooth_icon[2].get_toggle_state()
            if bluetooth_state == 1:
                is_bluetooth_icon[2].click_input()
                sleep(2)
                bluetooth_state = is_bluetooth_icon[2].get_toggle_state()
                if bluetooth_state == 0:
                    pass_list.append('Bluetooth OFF normally')
                    is_bluetooth_icon[2].click_input()
                    sleep(2)
                    bluetooth_state = is_bluetooth_icon[2].get_toggle_state()
                    if bluetooth_state == 1:
                        pass_list.append('Bluetooth ON normally')
                    else:
                        fail_list.append('Bluetooth ON abnormally')
                else:
                    fail_list.append('Bluetooth OFF abnormally')
            else:
                fail_list.append('Bluetooth default must ON')
        else:
            fail_list.append('Bluetooth button')

        write_log_setting('Control center 21', pass_list, fail_list)

        if len(fail_list) > 0:
            return False
        elif len(pass_list) > 0:
            return True
    except Exception as e:
        print(f'Control center 8  error: {e}')


