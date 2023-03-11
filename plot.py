import matplotlib.pyplot as plt


def showPrices(data):
    plt.plot(data.Price)
    plt.xlabel("Time (Day)")
    plt.ylabel("Price(USD)")
    plt.title("Microsoft Stock Prices")
    plt.show()

def showMACD(data):
    plt.plot(data.MACD, label='MACD')
    plt.plot(data.Signal, label='Signal')
    plt.xlabel("Time (Day)")
    plt.ylabel("MACD Value")
    plt.title("MACD")
    plt.legend()
    plt.show()

#def showPricesWithBuyAndSell(data, buy_date, sell_date):
