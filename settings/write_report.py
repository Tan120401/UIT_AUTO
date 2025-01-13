import pandas as pd


def write_result_report(testcase_name, result):
    file_path = 'UIT_Report.xlsx'

    data = {
        'Test Case': testcase_name,
        'Result': result
    }

    # Create DataFrame
    df = pd.DataFrame(data)
    df.to_excel(file_path, sheet_name='Settings', index=False)
    dfread = pd.read_excel(file_path, sheet_name='Settings')
    print(dfread)

testcase_name = ['test1', 'test2']
result = ['Pass', 'Fail']
write_result_report(testcase_name, result)