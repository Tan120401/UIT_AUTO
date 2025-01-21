from common_lib.common_lib import base_setting

def setting_5():
    # dictionaries
    dic_of_objects = {
        'title': 'System, Display, Brightness & color, Scale & layout, Related settings',
        'auto_id': ", , , , ",
        'control_type': 'ListItem, Text, Text, Text, Text',
        'object_handle': 'click, click, view, view, view'
    }
    result = base_setting("Setting 5", "Settings", dic_of_objects)
    return result
