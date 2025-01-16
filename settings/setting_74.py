# Function Test Case setting 73
from common_lib.common_lib import base_setting


def setting_74():
    # dictionaries
    dic_of_objects = {
        'title': 'Personalization, Background, Colors, Themes, Dynamic Lighting, Lock screen, Text input, Start, Taskbar, Fonts, Device usage',
        'auto_id': ", , , , , , , , , , ",
        'control_type': 'ListItem, Group, Group, Group, Group, Group, Group, Group, Group, Group, Group',
        'object_handle': 'click, view, view, view, view, view, view, view, view, view, view'
    }
    result = base_setting("Setting 74", "Settings", dic_of_objects)
    return result