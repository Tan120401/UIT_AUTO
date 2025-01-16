# Function test case setting 58
from common_lib.common_lib import open_app, click_object, scroll_center, write_log_setting, close_app


def setting_58():
    target_window =  open_app('Settings')

    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    is_bluetooth_devices = click_object(target_window,'Bluetooth & devices', '', 'ListItem')
    scroll_center(target_window, 'Cameras', '', 'Group')

    is_auto_play = click_object(target_window, 'AutoPlay', '', 'Text')

    # Focus add device window
    list_objects_check = [is_bluetooth_devices, is_auto_play]

    for obj in list_objects_check:
        if obj[0]:
            pass_list.append(obj[1])
        else:
            fail_list.append(obj[1])

    is_auto_play_default = target_window.child_window(title='Use AutoPlay for all media and devices',auto_id='SystemSettings_Autoplay_IsEnabled_ToggleSwitch', control_type='Button')
    is_auto_play_default_state = is_auto_play_default.get_toggle_state()
    if is_auto_play_default_state == 1:
        pass_list.append(f'{is_auto_play_default.window_text()} default is ON')
    else:
        fail_list.append(f'{is_auto_play_default.window_text()} default is OFF')

    is_removable_drive = target_window.child_window(title="Removable drive", auto_id="SystemSettings_Autoplay_StorageHandler_ComboBox", control_type="ComboBox")
    removable_drive_value = is_removable_drive.selected_text()
    if removable_drive_value is None:
        pass_list.append('Removable drive is Select default app')
    else:
        fail_list.append('Removable drive is not Select default app')

    is_memory_card = target_window.child_window(title="Memory card", auto_id="SystemSettings_Autoplay_CameraStorageHandler_ComboBox", control_type="ComboBox")

    memory_card_value = is_memory_card.selected_text()
    if memory_card_value is None:
        pass_list.append('Memory card is Select default app')
    else:
        fail_list.append('Memory card is not Select default app')

    is_default_app = target_window.child_window(title="Default app settings",auto_id="SystemSettings_XLinks_Local_System_Defaults_Link_HyperlinkButton",control_type="Hyperlink")
    if is_default_app.exists():
        pass_list.append(is_default_app.window_text())
    else:
        fail_list.append(is_default_app.window_text())
    # Focus Home settings
    write_log_setting('Setting 58', pass_list, fail_list)

    # close window
    close_app('Settings')
    if len(fail_list) > 0:
        return False
    elif len(pass_list) > 0:
        return True
