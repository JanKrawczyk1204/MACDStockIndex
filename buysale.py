import matplotlib.pyplot as plt
import pandas as pd


def buyAndSellDate(data):
    buy_date = []
    sell_date = []
    for i in range(1, 1000):
        if data.MACD[i-1] < data.Signal[i-1] and data.MACD[i] >= data.Signal[i]:
            buy_date.append(data.Date[i])
        if data.MACD[i-1] > data.Signal[i-1] and data.MACD[i] <= data.Signal[i]:
            sell_date.append(data.Date[i])
    return buy_date, sell_date

def buyAndSellToData(data):
    buy_price = []
    buy_day = []
    sell_price = []
    sell_day = []
    for i in range(1, 1000):
        if data.MACD[i-1] < data.Signal[i-1] and data.MACD[i] >= data.Signal[i]:
            buy_price.append(data.Price[i])
            buy_day.append(i)
        if data.MACD[i-1] > data.Signal[i-1] and data.MACD[i] <= data.Signal[i]:
            sell_price.append(data.Price[i])
            sell_day.append(i)
    return buy_price, buy_day, sell_price, sell_day