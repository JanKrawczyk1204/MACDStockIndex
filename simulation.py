from  plot import showHistogram

def simulateStockMarket(data, capital):
    stock = 0
    capital_over_time = []
    days = []
    capital_over_time.append(0)
    days.append(0)
    starting_capital = capital
    for i in range(1, 1000):
        if data.MACD[i-1] < data.Signal[i-1] and data.MACD[i] >= data.Signal[i]:
            capital, stock = buy(data, capital, stock, i)
        if data.MACD[i-1] > data.Signal[i-1] and data.MACD[i] <= data.Signal[i]:
            capital, stock = sell(data, capital, stock, i)
        capital_over_time.append(calculateCapital(data, capital, stock, i) - calculateCapital(data, capital, stock, i-1))
        days.append(i)
    sell(data, capital, stock, 999)
    print('Starting capital:' + str(round(starting_capital, 2)))
    print('Closing capital: ' + str(round(capital, 2)))
    print('Profit:' + str(round(capital - starting_capital, 2)) + ' ' + str(round((capital-starting_capital)/starting_capital * 100, 2)) + '%')
    showHistogram(days, capital_over_time)


def buy(data, capital, stock, day):
    while capital >= data.Price[day]:
        capital -= data.Price[day]
        stock += 1
    return capital, stock


def sell(data, capital, stock, day):
    capital += stock * data.Price[day]
    stock = 0
    return capital, stock

def calculateCapital(data, capital, stock, day):
    return capital + stock*data.Price[day]