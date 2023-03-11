

def buyAndSellDate(data):
    buy_date = []
    sell_date = []
    for i in range(1, 1000):
        if data.MACD[i-1] < data.Signal[i-1] and data.MACD[i] >= data.Signal[i]:
            buy_date.append(data.Date[i])
        if data.MACD[i-1] > data.Signal[i-1] and data.MACD[i] <= data.Signal[i]:
            sell_date.append(data.Date[i])
    return buy_date, sell_date

