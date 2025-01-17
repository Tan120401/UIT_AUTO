from common_lib.common_lib import base_setting, click_object, open_app, scroll_center, find_object, write_log_setting, \
    close_app


def setting_60():
    target_window = open_app('Settings')

    # list of result
    pass_list = []
    fail_list = []

    is_bluetooth_devices = click_object(target_window, 'Bluetooth & devices', '', 'ListItem')
    is_cameras = scroll_center(target_window, 'Cameras', '', 'Group')
    is_usb = click_object(target_window, 'USB', '', 'Group')

    # list of object
    object_list = [is_bluetooth_devices, is_usb]

    for obj in object_list:
        if obj[0]:
            pass_list.append(obj[1])
        else:
            fail_list.append(obj[1])

    is_connection_noti = find_object(target_window, 'Connection notifications', 'SystemSettings_Usb_ErrorNotify_ToggleSwitch', 'Button')
    is_show_noti = find_object(target_window, 'Show a notification if this PC is charging slowly over USB', 'SystemSettings_Usb_WeakChargerNotify_ToggleSwitch', 'Button')
    is_usb_battery = find_object(target_window, 'USB battery saver', 'SystemSettings_Usb_AttemptRecoveryFromPowerDrain_ToggleSwitch', 'Button')

    object_list_check_default = [is_connection_noti, is_show_noti, is_usb_battery]

    for obj in object_list_check_default:
        if obj[0]:
            if obj[2].get_toggle_state() == 1:
                pass_list.append(f'{obj[1]} default is ON')
            else:
                fail_list.append(f'{obj[1]} default is OFF')
        else:
            fail_list.append(obj[1])
    write_log_setting('Setting 60', pass_list, fail_list)

    # close window
    close_app('Settings')
    if len(fail_list) > 0:
        return False
    elif len(pass_list) > 0:
        return True
