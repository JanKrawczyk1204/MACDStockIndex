import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def showPrices(data):
    plt.plot(data.Close)
    plt.xlabel("Time (Day)")
    plt.ylabel("Price(USD)")
    plt.title("Microsoft Stock Prices")
    plt.show()

def showMACD(data):
    plt.plot(data.MACD)
    plt.plot(data.Signal)
    plt.show()