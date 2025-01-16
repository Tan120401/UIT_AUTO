# Function test case setting 43
from common_lib.common_lib import open_app, click_object, find_object, write_log_setting, close_app


def setting_43():

    target_window = open_app('Settings')

    # The List contains the pass fail objects
    pass_list = []
    fail_list = []

    is_bluetooth_device = click_object(target_window, 'Bluetooth & devices', '', 'ListItem')

    is_printers_scanners = click_object(target_window, 'Printers & scanners', '', 'Text')
    is_add_printer = find_object(target_window, 'Add a printer or scanner', '', 'Text')
    is_printer_preferences = find_object(target_window, 'Printer preferences', '', 'Text')
    is_related_settings = find_object(target_window, 'Related settings', '', 'Text')
    is_print_server_properties = find_object(target_window, 'Print server properties', '', 'Text')

    #Focus add device window
    list_objects_check = [is_bluetooth_device, is_printers_scanners, is_add_printer, is_printer_preferences, is_related_settings, is_print_server_properties]

    for obj in list_objects_check:
        if obj[0]:
            pass_list.append(obj[1])
        else:
            fail_list.append(obj[1])
    # get value on or off
    is_manage_my_default_printer = target_window.child_window(title='Let Windows manage my default printer', auto_id='SystemSettings_DefaultPrinterManagedByWindows_ToggleSwitch',control_type='Button')
    is_default_printer_state = is_manage_my_default_printer.get_toggle_state()
    if is_default_printer_state == 1:
        pass_list.append(f'{is_manage_my_default_printer.window_text()} default is ON')
    else:
        fail_list.append(f'{is_manage_my_default_printer.window_text()} default is OFF')

    is_download_drivers = target_window.child_window(title='Download drivers and device software over metered connections', control_type='Button')
    is_default_is_download_driver_state = is_download_drivers.get_toggle_state()
    if is_default_is_download_driver_state == 0:
        pass_list.append(f'{is_download_drivers.window_text()} default is OFF')
    else:
        fail_list.append(f'{is_download_drivers.window_text()} default is ON')
    # Focus Home settings
    write_log_setting('Setting 43', pass_list, fail_list)

    # close window
    close_app('Settings')
    if len(fail_list) > 0:
        return False
    elif len(pass_list) > 0:
        return True
