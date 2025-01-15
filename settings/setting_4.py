from time import sleep

from common_lib.common_lib import base_setting


def setting_4():
    # dictionaries
    dic_of_objects = {
        'title': 'Home, Recommended settings, Cloud storage, Bluetooth devices, Personalize your device, Try Microsoft 365',
        'auto_id': ", TitleContent, , TitleContent, TitleContent, ",
        'control_type': 'ListItem, Text, Text, Text, Text, Text',
        'object_handle': 'click, view, view, view, view, view'
    }
    result =base_setting("Setting 4", "Settings", dic_of_objects)
    return result