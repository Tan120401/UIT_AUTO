# Function Test Case setting 22
import psutil

from common_lib.common_lib import base_setting


def setting_22():
    # Lấy thông tin về ổ đĩa C:
    partition_info = psutil.disk_usage('C:\\')
    total = round(partition_info.total / (1024 ** 3))  # Dung lượng tổng cộng (GB)
    # used = partition_info.used / (1024 ** 3)  # Dung lượng đã sử dụng (GB)
    # free = partition_info.free / (1024 ** 3)  # Dung lượng còn lại (GB)

    # print(f"Tổng dung lượng: {total:.2f} GB")

    dic_of_objects = {
        'title': f'System, Storage, ‎Local Disk (C:) - {total} GB, Storage management',
        'auto_id': ", , SystemSettings_StorageSense_Breakdown_TitleTextBlock, ",
        'control_type': 'ListItem, Group, Text, Text',
        'object_handle': 'click, click, click, view'
    }
    result = base_setting("Setting 22", "Settings", dic_of_objects)
    return result
