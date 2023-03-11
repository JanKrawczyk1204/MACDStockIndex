import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from file import importData
from macd import addEMCToData, calculateMACD, calculateSignal
from plot import showPrices, showMACD

if __name__ == '__main__':
        data = importData("MSFT.csv")
        showPrices(data)
        calculateMACD(data)
        showMACD(data)
