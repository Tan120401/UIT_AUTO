# Function test case setting 55
from common_lib.common_lib import open_app, click_object, scroll_center, find_object, write_log_setting, close_app


def setting_55():
    target_window =  open_app('Settings')

    is_bluetooth_devices = click_object(target_window, 'Bluetooth & devices', '', 'ListItem')

    scroll_center(target_window, 'Cameras', '', 'Group')

    is_touchpad = click_object(target_window, 'Touchpad', '', 'Group')

    is_touchpad_in = find_object(target_window, 'Touchpad', '', 'Group')

    is_gestures = find_object(target_window, 'Gestures & interaction', '', 'Text')

    is_related_settings = find_object(target_window, 'Related settings', '', 'Text')


    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    #Focus add device window
    list_objects_check = [is_bluetooth_devices, is_touchpad, is_touchpad_in, is_gestures, is_related_settings]

    for obj in list_objects_check:
        if obj[0]:
            pass_list.append(obj[1])
        else:
            fail_list.append(obj[1])

    # Focus Home settings
    write_log_setting('Setting 55', pass_list, fail_list)

    # close window
    close_app('Settings')
    if len(fail_list) > 0:
        return False
    elif len(pass_list) > 0:
        return True
