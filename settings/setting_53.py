# Function test case setting 53
from common_lib.common_lib import base_setting


def setting_53():

    # dictionaries
    dic_of_objects = {
        'title': 'Bluetooth & devices, Cameras, Search for cameras, Connected cameras, Related settings',
        'auto_id': ", , SystemSettings_Camera_DeviceAdd_Button, SystemSettings_Camera_DeviceList_GroupTitleTextBlock, ",
        'control_type': 'ListItem, Group, Button, Text, Text',
        'object_handle': 'click, click, view, view, view'
    }
    result = base_setting("Setting 53", "Settings", dic_of_objects)
    return result
