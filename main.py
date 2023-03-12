from file import importData
from macd import calculateMACD
from plot import showPrices, showMACD, showPricesWithBuyAndSell
from buysale import buyAndSellDate, buyAndSellToData

if __name__ == '__main__':
        data = importData("MSFT.csv")
        showPrices(data)
        calculateMACD(data)
        showMACD(data)
        buy_date, sell_date = buyAndSellDate(data)
        print(buy_date)
        print(sell_date)
        showPricesWithBuyAndSell(data)
