# Function test case setting 41
from common_lib.common_lib import base_setting

def setting_41():
    # dictionaries
    dic_of_objects = {
        'title': 'Bluetooth & devices, View more devices, Bluetooth, Other devices, Related settings',
        'auto_id': ", , , , ",
        'control_type': 'ListItem, Button, Text, Text, Text',
        'object_handle': 'click, click, view, view, view'
    }

    result = base_setting("Setting 41", "Settings", dic_of_objects)
    return result

