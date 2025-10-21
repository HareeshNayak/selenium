import pandas as pd

def get_test_data(file_path, sheet_name=None):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df.to_dict(orient='records')
