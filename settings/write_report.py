import pandas as pd
import os

def write_result_report(testcase_name, result):
    file_path = 'UIT_Report.xlsx'

    data = {
        'Test Case': testcase_name,
        'Result': result
    }

    df = pd.DataFrame(data)


    df.to_excel(file_path, sheet_name='Settings', index=False)

    # Read back the file to verify
    dfread = pd.read_excel(file_path, sheet_name='Settings')
    print(dfread)

# Example usage

