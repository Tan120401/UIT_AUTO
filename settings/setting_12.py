# Function test case setting 12
from common_lib.common_lib import base_setting

def setting_12():
    # dictionaries
    dic_of_objects = {
        'title': 'System, Sound, Output, Input, Advanced',
        'auto_id': ", , , , ",
        'control_type': 'ListItem, Group, Text, Text, Text',
        'object_handle': 'click, click, view, view, view'
    }
    result = base_setting("Setting 12", "Settings", dic_of_objects)
    return result