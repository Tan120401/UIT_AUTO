from time import sleep

from common_lib.common_lib import open_app, click_object, find_object, scroll_center, write_log_setting, close_app


def setting_24():
    target_window = open_app('Settings')
    # List of result
    pass_list = []
    fail_list = []

    is_system = click_object(target_window, 'System', '', 'ListItem')
    is_storage = click_object(target_window, 'Storage', '', 'Group')
    object_check_list = [is_system, is_storage]

    for obj in object_check_list:
        if obj[0]:
            pass_list.append(obj[1])
        else:
            fail_list.append(obj[1])

    is_storage_sense_toggle = find_object(target_window,'Storage Sense','SystemSettings_StorageSense_SmartPoliciesAdvanced_GlobalToggleRejuv_ToggleSwitch','Button')
    if is_storage_sense_toggle[0]:
        is_storage_sense_state = is_storage_sense_toggle[2].get_toggle_state()
        if is_storage_sense_state == 1:
            # Click storage OFF
            is_storage_sense_toggle[2].click_input()
            sleep(2)
            is_storage_sense_state = is_storage_sense_toggle[2].get_toggle_state()
            if is_storage_sense_state == 0:
                pass_list.append('Storage Sense set OFF normally')
            else:
                fail_list.append('Storage Sense set OFF abnormally')

            # Click storage ON
            is_storage_sense_toggle[2].click_input()
            sleep(2)
            is_storage_sense_state = is_storage_sense_toggle[2].get_toggle_state()
            if is_storage_sense_state == 1:
                pass_list.append('Storage Sense set ON normally')
            else:
                fail_list.append('Storage Sense set ON abnormally')
        else:
            # Click storage ON
            is_storage_sense_toggle[2].click_input()
            sleep(2)
            is_storage_sense_state = is_storage_sense_toggle[2].get_toggle_state()
            if is_storage_sense_state == 1:
                pass_list.append('Storage Sense set ON normally')
            else:
                fail_list.append('Storage Sense set ON abnormally')

            # Click storage OFF
            is_storage_sense_toggle[2].click_input()
            sleep(2)
            is_storage_sense_state = is_storage_sense_toggle[2].get_toggle_state()
            if is_storage_sense_state == 0:
                pass_list.append('Storage Sense set OFF normally')
            else:
                fail_list.append('Storage Sense set OFF abnormally')
        # Click storage sense
        is_storage_sense_state = is_storage_sense_toggle[2].get_toggle_state()
        if is_storage_sense_state == 1:
            is_storage_sense = click_object(target_window, 'Storage Sense', '', 'Group')
        else:
            is_storage_sense_toggle.click_input()
            is_storage_sense = click_object(target_window, 'Storage Sense', '', 'Group')

        # Scroll
        scroll_center(target_window, 'Configure cleanup schedules', '', 'Text')
        # Run Storage Sense now'
        is_run_storage_sense = click_object(target_window, 'Run Storage Sense now',
                                             'SystemSettings_StorageSense_SmartPolicy_ExecuteNow_ApplyButton',
                                             'Button')
        if is_run_storage_sense[0]:
            pass_list.append(is_run_storage_sense[1])
        else:
            fail_list.append(is_run_storage_sense[1])
    else:
        fail_list.append('Storage Sense')

    # Write log setting
    write_log_setting('Setting 24', pass_list, fail_list)

    # close window
    close_app('Settings')
    if len(fail_list) > 0:
        return False
    elif len(pass_list) > 0:
        return True

