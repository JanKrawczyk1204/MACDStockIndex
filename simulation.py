

def simulateStockMarket(data, capital):
    stock = 0
    starting_capital = capital
    for i in range (1, 1000):
        if data.MACD[i-1] < data.Signal[i-1] and data.MACD[i] >= data.Signal[i]:
            capital, stock = buy(data, capital, stock, i)
        if data.MACD[i-1] > data.Signal[i-1] and data.MACD[i] <= data.Signal[i]:
            capital, stock = sell(data, capital, stock, i)
    sell(data, capital, stock, 999)
    print('Starting capital:' + str(starting_capital))
    print('Closing capital: ' + str(capital))
    print('Profit:' + str(capital - starting_capital))


def buy(data, capital, stock, day):
    while capital >= data.Price[day]:
        capital -= data.Price[day]
        stock += 1
    return capital, stock


def sell(data, capital, stock, day):
    capital += stock * data.Price[day]
    stock = 0
    return capital, stock