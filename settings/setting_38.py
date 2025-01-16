# Function test case setting 38
from common_lib.common_lib import open_app, click_object, scroll_center, base_setting


def setting_38():
    # dictionaries
    dic_of_objects = {
        'title': 'System, Storage, About, Device specifications, Windows specifications, Support, Related',
        'auto_id': ", , , , , , ",
        'control_type': 'ListItem, Group, Group, Group, Group, Group, Text',
        'object_handle': 'click, scroll, click, view, view, view, view'
    }
    result = base_setting("Setting 38", "Settings", dic_of_objects)
    return result
