
def calculateEMA(sorce_collumn, day, n):
    ema_nominator = sorce_collumn[day]
    ema_denominator = 1
    alpha = 2 / (n-1)
    for i in range(1, n+1):
        ema_nominator += pow(1-alpha, i)*sorce_collumn[day-i]
        ema_denominator += pow(1-alpha, i)
    return ema_nominator/ema_denominator

def addEMCToData(sorce_collumn, precision):
    ema = []
    for i in range(0, precision):
        ema.append(0)
    for i in range(precision, 1000):
        ema.append(calculateEMA(sorce_collumn, i, precision))
    return ema

def calculateMACD(data):
    data['EMC26'] = addEMCToData(data.Price, 26)
    data['EMC12'] = addEMCToData(data.Price, 12)
    macd = []
    for i in range(0, 26):
        macd.append(0)
    for i in range(26, 1000):
        macd.append(data.EMC26[i] - data.EMC12[i])
    data['MACD'] = macd
    calculateSignal(data)

def calculateSignal(data):
    signal = []
    for i in range(0, 35):
        signal.append(0)
    for i in range(35, 1000):
        signal.append(calculateEMA(data.MACD, i, 9))
    data['Signal'] = signal
