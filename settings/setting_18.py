# Function test case setting 18
from common_lib.common_lib import base_setting

def setting_18():
    # dictionaries
    dic_of_objects = {
        'title': 'System, Power & battery, Power & battery',
        'auto_id': ", , ",
        'control_type': 'ListItem, Text, Text',
        'object_handle': 'click, click, view'
    }
    result = base_setting("Setting 14", "Settings", dic_of_objects)
    return result