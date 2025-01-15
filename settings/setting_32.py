# Function test case setting 32
from time import sleep

from common_lib.common_lib import open_app, click_object, scroll_center, click_object_within_group, find_open_window, \
    write_log_setting, close_app


def setting_32():
    target_window = open_app('Settings')
    click_object(target_window, 'System', '', 'ListItem')

    # Scroll down
    scroll_center(target_window, 'Storage', '', 'Group')

    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    is_troubleshoot = click_object(target_window, 'Troubleshoot', '', 'Group')
    is_other_troubleshoot = click_object(target_window, 'Other troubleshooters', '', 'Text')

    # Assess object pass/fail
    list_of_object = [is_troubleshoot, is_other_troubleshoot]
    for obj in list_of_object:
        if obj[0]:
            pass_list.append(obj[1])
        else:
            fail_list.append(obj[1])

    # Click troubleshoot audio
    print(target_window.print_control_identifiers())
    is_audio = click_object(target_window, 'Audio', 'TroubleshooterCollection_1_EntityItem', 'Group')

    if is_audio[0]:
        # click_object_by_coordinates(2448, 314, 2708, 378)

        # is_audio_run = click_object(target_window, 'Run', 'TroubleshooterCollection_1_Button', 'Button')
        is_audio_run = click_object_within_group(is_audio[2], 'Run', 'TroubleshooterCollection_1_Button', 'Button')
        print(is_audio_run)
        sleep(2)
        is_audio_troubleshoot = find_open_window('Get Help')
        if is_audio_troubleshoot:
            pass_list.append('Audio Troubleshoot normally')
        else:
            fail_list.append('Audio Troubleshoot abnormally')
    # print(target_window.print_control_identifiers())
    # # Click troubleshoot audio
    is_network = click_object(target_window, 'Network and Internet', 'TroubleshooterCollection_1_EntityItem', 'Group')
    if is_network:
        is_network_run = click_object_within_group(is_network[2], 'Run', 'TroubleshooterCollection_1_Button', 'Button')
        sleep(2)
        is_audio_troubleshoot = find_open_window('Get Help')
        if is_audio_troubleshoot:
            pass_list.append('Network and Internet Troubleshoot normally')
        else:
            fail_list.append('Network and Internet Troubleshoot abnormally')

    write_log_setting('Setting 32', pass_list, fail_list)

    # close window
    close_app('Settings')

    if len(fail_list) > 0:
        return False
    elif len(pass_list) > 0:
        return True
