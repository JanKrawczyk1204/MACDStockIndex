import matplotlib.pyplot as plt
from buysale import buyAndSellToData

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

def showPricesWithBuyAndSell(data):
    buy_price, buy_day, sell_price, sell_day = buyAndSellToData(data)
    plt.plot(buy_day, buy_price, 'go', label='Buy')
    plt.plot(sell_day, sell_price, 'bo', label='Sell')
    plt.plot(data.Price, label='Price')
    plt.legend()
    plt.show()