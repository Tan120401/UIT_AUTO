# Function Test case setting 63
from common_lib.common_lib import base_setting

def setting_69():
    # dictionaries
    dic_of_objects = {
        'title': f'Network & internet, Airplane mode, Airplane mode, Wireless devices',
        'auto_id': ", , SystemSettings_Radio_IsAirplaneModeEnabled_ToggleSwitch, ",
        'control_type': 'ListItem, Group, Button, Text',
        'object_handle': 'click, click, click, click'
    }

    result = base_setting("Setting 69", "Settings", dic_of_objects)
    return result
setting_69()