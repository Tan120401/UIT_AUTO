# Function test case setting 54
from common_lib.common_lib import open_app, base_setting


def setting_54():
    open_app('Settings')
    # dictionaries
    dic_of_objects = {
        'title': 'Bluetooth & devices, Mouse, Primary mouse button, Mouse pointer speed, Enhance pointer precision, Scrolling, Related settings',
        'auto_id': ", , , , , , ",
        'control_type': 'ListItem, Group, Text, Text, Text, Text, Text',
        'object_handle': 'click, click, view, view, view, view, view'
    }
    result = base_setting("Setting 54", "Settings", dic_of_objects)
    return result
