# Function test case setting 57
from common_lib.common_lib import open_app, click_object, scroll_center, find_object, write_log_setting, base_setting


def setting_57():

    # dictionaries
    dic_of_objects = {
        'title': 'Bluetooth & devices, Cameras, AutoPlay, Use AutoPlay for all media and devices, Choose AutoPlay defaults, Related settings',
        'auto_id': ", , , SystemSettings_Autoplay_IsEnabled_ToggleSwitch, SettingsGroupControlTemplate_DisplayName, RelatedLinksGroupHeader",
        'control_type': 'ListItem, Group, Text, Button, Text, Text',
        'object_handle': 'click, scroll, click, view, view, view'
    }
    result = base_setting("Setting 57", "Settings", dic_of_objects)
    return result

