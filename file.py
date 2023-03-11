import pandas as pd

def importData(path):
    data = pd.read_csv(path)
    data = data.drop(['High', 'Low', 'Open', 'Adj Close', 'Volume'], 1)
    return data
