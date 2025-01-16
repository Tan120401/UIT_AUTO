from common_lib.common_lib import base_setting
def setting_3():
    # dictionaries
    dic_of_objects = {
        'title': 'Find a setting, Home, System, Bluetooth & devices, Network & internet, Personalization, Apps, Accounts, '
                 'Time & language, Gaming, Accessibility, Privacy & security, Windows Update',
        'auto_id': ', , , , , , , , , , , , ',
        'control_type': 'Text, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem, ListItem',
        'object_handle': 'view, view, view, view, view, view, view, view, view, view, view, view, view'
    }
    result = base_setting("Setting 3", "Settings", dic_of_objects)
    return result
