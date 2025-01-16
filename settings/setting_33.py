# Function test case setting 33
from common_lib.common_lib import open_app, click_object, scroll_center, base_setting


def setting_33():
    # dictionaries
    dic_of_objects = {
        'title': 'System, Storage, Recovery, Reset this PC, Advanced startup',
        'auto_id': ", , , , ",
        'control_type': 'ListItem, Group, Group, Text, Text',
        'object_handle': 'click, scroll, click, view, view'
    }
    result = base_setting("Setting 33", "Settings", dic_of_objects)
    return result
