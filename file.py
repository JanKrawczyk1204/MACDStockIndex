import pandas as pd

def importData(path):
    raw_data = pd.read_csv(path)
    data = pd.DataFrame()
    data['Date'] = raw_data.Date
    data['Price'] = raw_data.Close
    return data