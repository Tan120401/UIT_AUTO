# Function test case setting 31
from common_lib.common_lib import open_app, click_object, scroll_center, find_object, write_log_setting, close_app


def setting_31():
    target_window = open_app('Settings')
    click_object(target_window, 'System', '', 'ListItem')

    # Scroll down
    scroll_center(target_window, 'Storage', '', 'Group')
    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    titles = ['Activation', 'Activation state, Active', 'Upgrade your edition of Windows', 'Change product key']
    control_types = ['Group', 'Group', 'Group', 'Text']
    auto_ids = ['', '', '', '']
    object_handles = ['click', 'view', 'click', 'view']
    # Check that the lengths of the lists match
    if len(titles) == len(control_types) == len(auto_ids) == len(object_handles):
        object_result = []
        for title, auto_id, control_type, object_handle in zip(titles, auto_ids, control_types, object_handles):
            if object_handle == 'click':
                object_result = click_object(target_window, title, auto_id, control_type)
            elif object_handle == 'view':
                object_result = find_object(target_window, title, auto_id, control_type)
            if object_result[0]:
                pass_list.append(title)
            else:
                fail_list.append(title)
    else:
        print("Dic object list không đồng nhất")

    # Focus Home settings
    write_log_setting('Setting 31', pass_list, fail_list)

    # close window
    close_app('Settings')

    if len(fail_list) > 0:
        return False
    elif len(pass_list) > 0:
        return True