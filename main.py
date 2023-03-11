import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from file import importData
from macd import addEMCToData, calculateMACD, calculateSignal
from plot import showPrices, showMACD

if __name__ == '__main__':
        data = importData("MSFT.csv")
        addEMCToData(data, 26, 'EMC26')
        addEMCToData(data, 12, 'EMC12')
        calculateMACD(data)
        calculateSignal(data)
        showPrices(data)
        showMACD(data)
