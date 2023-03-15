from file import importData
from macd import calculateMACD, calculateTradeLine
from plot import showPrices, showMACD, showPricesWithBuyAndSell, showPriceswithTrandLine
from buysale import buyAndSellDate
from simulation import simulateStockMarket, betterStockSimulation

if __name__ == '__main__':
        data = importData("MSFT.csv")
        showPrices(data)
        calculateMACD(data)
        showMACD(data)
        buy_date, sell_date = buyAndSellDate(data)
        print(buy_date)
        print(sell_date)
        showPricesWithBuyAndSell(data)
        simulateStockMarket(data, 1000)
        calculateTradeLine(data)
        showPriceswithTrandLine(data)
        betterStockSimulation(data, 1000)
