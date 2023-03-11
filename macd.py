import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def calculateEMA(data, day, n):
    ema_nominator = data.Price[day]
    ema_denominator = 1
    alpha = 2 / (n-1)
    for i in range(1, n+1):
        ema_nominator += pow(1-alpha, i)*data.Price[day-i]
        ema_denominator += pow(1-alpha, i)
    return ema_nominator/ema_denominator

def addEMCToData(data, precision, collumn_name):
    ema = []
    for i in range(0,precision):
        ema.append(0)
    for i in range(precision,1000):
        ema.append(calculateEMA(data, i, precision))
    data[collumn_name] = ema

def calculateMACD(data):
    macd = []
    for i in range(0, 26):
        macd.append(0)
    for i in range(26, 1000):
        macd.append(data.EMC26[i] - data.EMC12[i])
    data['MACD'] = macd


def calculateOneSignal(data, day):
    ema_nominator = data.MACD[day]
    ema_denominator = 1
    alpha = 4
    for i in range(1, 10):
        ema_nominator += pow(1-alpha, i)*data.MACD[day-i]
        ema_denominator += pow(1-alpha, i)
    return ema_nominator/ema_denominator


def calculateSignal(data):
    signal = []
    for i in range(0, 35):
        signal.append(0)
    for i in range(35, 1000):
        signal.append(calculateOneSignal(data, i))
    data['Signal'] = signal