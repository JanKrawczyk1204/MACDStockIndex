import matplotlib.pyplot as plt
from buysale import buyAndSellToData, betterBuyAndSellToData

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
    plt.xlabel("Time (Day)")
    plt.ylabel("Price(USD)")
    plt.title("Microsoft Stock Prices \nWith MACD calculated points")
    plt.legend()
    plt.show()

def showHistogram(days, capital_changes):
    plt.bar(days, capital_changes)
    plt.xlabel("Time (Day)")
    plt.ylabel('Gain or loss (USD)')
    plt.title('Daily gain or lost')
    plt.show()

def showPriceswithTrandLine(data):
    buy_price, buy_day, sell_price, sell_day = betterBuyAndSellToData(data)
    plt.plot(buy_day, buy_price, 'go', label='Buy')
    plt.plot(sell_day, sell_price, 'bo', label='Sell')
    plt.plot(data.Price, label='Price')
    plt.plot(data.TrendLine, label='Trend line')
    plt.xlabel("Time (Day)")
    plt.ylabel("Price(USD)")
    plt.title("Microsoft Stock Prices \nWith MACD calculated points and trend line")
    plt.legend()
    plt.show()
