from pywinauto import Desktop

from common_lib.common_lib import get_connected_wifi, click_object, find_object, scroll_center, write_log_setting


def control_center_12():
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
        scroll_center(quick_setting, 'Nearby sharing', 'Microsoft.QuickAction.NearShare', 'Button')

        is_project_button = click_object(quick_setting, 'Project', 'Microsoft.QuickAction.ProjectL2', 'Button')

        is_project_group = find_object(quick_setting, 'Project', 'PageWindow', 'Group')

        object_list = [is_wifi, is_project_button, is_project_group]
        for obj in object_list:
            if obj[0]:
                pass_list.append(obj[1])
            else:
                fail_list.append(obj[1])

        # get all element
        child_elements = is_project_group[2].descendants(control_type='ListItem')
        project_mode_default = ['PC screen only', 'Duplicate', 'Extend', 'Second screen only']
        project_mode = []
        # find elements
        for element in child_elements:
            element_text = element.window_text().split(', ')
            project_mode.append(element_text[0])
        if project_mode == project_mode_default:
            pass_list.append('Project mode normally')
        else:
            fail_list.append('Project mode abnormally')

        is_wifi[2].click_input()

        write_log_setting('Control center 12', pass_list, fail_list)

        if len(fail_list) > 0:
            return False
        elif len(pass_list) > 0:
            return True
    except Exception as e:
        print(f'Control center error: {e}')

