# Function Test case setting 63
from common_lib.common_lib import get_connected_wifi, open_app, base_setting


def setting_63():
    connected_wifi = get_connected_wifi()

    open_app('Settings')
    # dictionaries
    dic_of_objects = {
        'title': f'Network & internet, Wi-Fi, Wi-Fi, {connected_wifi} properties, Show available networks, Manage known networks, Hardware properties, Random hardware addresses',
        'auto_id': ", , , , , , , ",
        'control_type': 'ListItem, Group, Button, Text, Text, Text, Text, Text',
        'object_handle': 'click, click, view, view, view, view, view, view'
    }
    result = base_setting("Setting 63", "Settings", dic_of_objects)
    return result
