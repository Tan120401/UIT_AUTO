from time import sleep

from pywinauto import Desktop

from common_lib.common_lib import get_connected_wifi, click_object, find_object, write_log_setting


def control_center_8():
    try:
        # List of result
        pass_list = []
        fail_list = []

        desktop = Desktop(backend="uia")
        taskbar = desktop.window(class_name="Shell_TrayWnd")

        connected_wifi = get_connected_wifi()

        is_wifi = click_object(taskbar, f"Network {connected_wifi}\nInternet access", 'SystemTrayIcon', 'Button')

        quick_setting = desktop.window(title="Quick settings")

        is_wifi_icon = find_object(quick_setting, "Wi-Fi", 'Microsoft.QuickAction.WiFi', 'Button')
        is_bluetooth_icon= find_object(quick_setting, "Bluetooth", 'Microsoft.QuickAction.Bluetooth', 'Button')
        is_airplane_icon = find_object(quick_setting, 'Airplane mode', 'Microsoft.QuickAction.AirplaneMode', 'Button')

        object_list = [is_wifi, is_wifi_icon, is_bluetooth_icon, is_airplane_icon]
        for obj in object_list:
            if obj[0]:
                pass_list.append(obj[1])
            else:
                fail_list.append(obj[1])

        air_plane_state = is_airplane_icon[2].get_toggle_state()
        wifi_state = is_wifi_icon[2].get_toggle_state()
        bluetooth_state = is_bluetooth_icon[2].get_toggle_state()

        print(quick_setting.print_control_identifiers())

        if air_plane_state == 0 and wifi_state == 1 and bluetooth_state == 1:
            pass_list.append('Air plane default OFF, Wi-Fi and Bluetooth ON')
            is_airplane_icon[2].click_input()
            sleep(3)
        else:
            fail_list.append('Air plane default OFF, Wi-Fi and Bluetooth not match')

        air_plane_state = is_airplane_icon[2].get_toggle_state()
        wifi_state = is_wifi_icon[2].get_toggle_state()
        bluetooth_state = is_bluetooth_icon[2].get_toggle_state()

        if air_plane_state == 1 and wifi_state == 0 and bluetooth_state == 0:
            pass_list.append('Air plane default ON, Wi-Fi and Bluetooth OFF')
            is_airplane_icon[2].click_input()
            sleep(3)
        else:
            fail_list.append('Air plane default ON, Wi-Fi and Bluetooth not match')

        #wait for wifi reconnect
        sleep(20)
        write_log_setting('Control center 8', pass_list, fail_list)

        if len(fail_list) > 0:
            return False
        elif len(pass_list) > 0:
            return True
    except Exception as e:
        print(f'Control center 8  error: {e}')
control_center_8()
