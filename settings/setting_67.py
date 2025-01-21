# Function Test case setting 63
from common_lib.common_lib import get_connected_wifi, open_app, base_setting

def setting_67():
    # dictionaries
    dic_of_objects = {
        'title': f'Network & internet, Dial-up, Set up a new connection',
        'auto_id': ", , ",
        'control_type': 'ListItem, Group, Text',
        'object_handle': 'click, click, view'
    }
    result = base_setting("Setting 67", "Settings", dic_of_objects)
    return result

