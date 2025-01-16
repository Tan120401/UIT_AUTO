# Function Test Case setting 73
from common_lib.common_lib import base_setting


def setting_44():
    # dictionaries
    dic_of_objects = {
        'title': 'Bluetooth & devices, Mobile devices, Allow this PC to access your mobile devices, Phone Link, Instantly access your mobile device from your PC, Show me suggestions for using my mobile device with Windows',
        'auto_id': ", , , , , ",
        'control_type': 'ListItem, Group, Group, Text, Text, Text',
        'object_handle': 'click, click, view, view, view, view'
    }
    result = base_setting("Setting 44", "Settings", dic_of_objects)
    return result
setting_44()