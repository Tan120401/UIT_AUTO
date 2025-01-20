from time import sleep

from pywinauto import Desktop

from common_lib.common_lib import get_connected_wifi, click_object, scroll_center, write_log_setting, find_object


def control_center_16():
    try:
        # List of result
        pass_list = []
        fail_list = []

        desktop = Desktop(backend="uia")
        taskbar = desktop.window(class_name="Shell_TrayWnd")
        connected_wifi = get_connected_wifi()

        is_wifi = click_object(taskbar, f"Network {connected_wifi}\nInternet access", 'SystemTrayIcon', 'Button')

        quick_setting = desktop.window(title="Quick settings")

        scroll_center(quick_setting, 'Airplane mode', 'Microsoft.QuickAction.AirplaneMode', 'Button')
        is_nearby_share = find_object(quick_setting, 'Nearby sharing', 'Microsoft.QuickAction.NearShare', 'Button')

        if is_nearby_share[0]:
            nearby_share_state = is_nearby_share[2].get_toggle_state()
            if nearby_share_state == 0:
                is_nearby_share[2].click_input()
                sleep(2)
                nearby_share_state = is_nearby_share[2].get_toggle_state()
                if nearby_share_state == 1:
                    pass_list.append('Nearby share ON normally')
                    is_nearby_share[2].click_input()
                    nearby_share_state = is_nearby_share[2].get_toggle_state()
                    if nearby_share_state == 0:
                        pass_list.append('Nearby share OFF normally')
                    else:
                        fail_list.append('Nearby share OFF abnormally')
                else:
                    fail_list.append('Nearby share ON abnormally')
            else:
                fail_list.append('Nearby share default must OFF')
        else:
            fail_list.append('Nearby share button')

        is_wifi[2].click_input()

        write_log_setting('Control center 16', pass_list, fail_list)

        if len(fail_list) > 0:
            return False
        elif len(pass_list) > 0:
            return True
    except Exception as e:
        print(f'Control center 8  error: {e}')


