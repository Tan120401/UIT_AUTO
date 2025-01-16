# Function Test Case setting 72
from common_lib.common_lib import base_setting


def setting_72():
    # dictionaries
    dic_of_objects = {
        'title': f'Network & internet, Proxy, Automatic proxy setup, Manual proxy setup',
        'auto_id': ", , , ",
        'control_type': 'ListItem, Group, Text, Text',
        'object_handle': 'click, click, view, view'
    }
    result = base_setting("Setting 72", "Settings", dic_of_objects)
    return result