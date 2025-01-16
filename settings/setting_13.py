# Function test case setting 12
from common_lib.common_lib import base_setting

def setting_13():
    # dictionaries
    dic_of_objects = {
        'title': 'System, Notifications, Get notifications from apps and other senders, Do not disturb, Turn on do not disturb automatically, Set priority notifications, Focus',
        'auto_id': ", , , , , SystemSettings_Notifications_QuietHours_EditProfile_EntityItem, SystemSettings_Notifications_FocusAssistSettingLink_ButtonEntityItem",
        'control_type': 'ListItem, Group, Group, Text, Group, Group, Group',
        'object_handle': 'click, click, view, view, view, view, view'
    }
    result = base_setting("Setting 13", "Settings", dic_of_objects)
    return result
