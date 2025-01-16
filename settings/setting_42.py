# Function test case setting 42
from pywinauto import Application
from pywinauto.findwindows import find_window

from common_lib.common_lib import open_app, click_object, find_object, write_log_setting, close_app


def setting_42():

    target_window = open_app('Settings')

    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    is_bluetooth_device = click_object(target_window, 'Bluetooth & devices', '', 'ListItem')
    is_add_device = click_object(target_window, 'Add device', '', 'Text')

    # Focus add device window
    window_handle = find_window(title_re='.*Add a device.*', backend='uia')
    app_bluetooth = Application(backend='uia').connect(handle=window_handle)
    bluetooth_window = app_bluetooth.window(handle=window_handle)

    is_bluetooth = find_object(bluetooth_window, 'Bluetooth', 'BluetoothDevicesButton', 'Button')
    is_wireless = find_object(bluetooth_window, 'Wireless display or dock', 'DisplayDevicesButton', 'Button')
    is_everything = find_object(bluetooth_window, 'Everything else', 'OtherDevicesButton', 'Button')

    list_objects_check = [is_bluetooth_device, is_add_device, is_bluetooth, is_wireless, is_everything]


    for obj in list_objects_check:
        if obj[0]:
            pass_list.append(obj[1])
        else:
            fail_list.append(obj[1])

    bluetooth_window.close()

    # Focus Home settings
    write_log_setting('Setting 42', pass_list, fail_list)

    # close window
    close_app('Settings')
    if len(fail_list) > 0:
        return False
    elif len(pass_list) > 0:
        return True

