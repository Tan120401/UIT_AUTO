# Function Test case setting 63
from common_lib.common_lib import get_connected_wifi, open_app, base_setting


def setting_62():
    # dictionaries
    dic_of_objects = {
        'title': f'Network & internet, Wi-Fi, Ethernet, VPN, Mobile hotspot, Airplane mode, Proxy, Dial-up, Advanced network settings',
        'auto_id': ", , , , , , , , ",
        'control_type': 'ListItem, Group, Group, Group, Group, Group, Group, Group, Group',
        'object_handle': 'click, view, view, view, view, view, view, view, view'
    }
    result = base_setting("Setting 62", "Settings", dic_of_objects)
    return result
