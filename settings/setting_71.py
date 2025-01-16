# Function Test Case setting 71
from common_lib.common_lib import base_setting


def setting_71():
    # dictionaries
    dic_of_objects = {
        'title': f'Network & internet, Mobile hotspot, Share my internet connection from, Share over, Properties',
        'auto_id': ", , , , ",
        'control_type': 'ListItem, Group, Text, Text, Text',
        'object_handle': 'click, click, view, view, view'
    }
    result = base_setting("Setting 71", "Settings", dic_of_objects)
    return result