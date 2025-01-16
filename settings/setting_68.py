# Function Test case setting 68
from common_lib.common_lib import open_app, base_setting


def setting_68():
    # dictionaries
    dic_of_objects = {
        'title': f'Network & internet, VPN, VPN connections, Advanced settings for all VPN connections',
        'auto_id': ", , , ",
        'control_type': 'ListItem, Group, Text, Text',
        'object_handle': 'click, click, view, view'
    }
    result = base_setting("Setting 68", "Settings", dic_of_objects)
    return result

