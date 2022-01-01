import data
import numpy as np
import pandas as p
import robinhood_helper as rh
#constants
BTC_MIN_PURCHASE_SELL_AMOUNT = 100.00
EMA_LOWER_VALUE = 20
EMA_UPPER_VALUE = 40
FMA_SIGNAL_VALUE = 4
    
#get pricing information
def getMACDTrendDifference():
    close_price_df = p.DataFrame(np.array(data.Data().getCryptoHistoricalDataFromKey('BTC', 'day', '5year', '24_7','close_price')))
    k = close_price_df.ewm(span=EMA_LOWER_VALUE, adjust=False, min_periods=EMA_LOWER_VALUE).mean()
    d = close_price_df.ewm(span=EMA_UPPER_VALUE, adjust=False, min_periods=EMA_UPPER_VALUE).mean()
    #SLOW MOVING AVERAGE
    macd_SMA = k - d
    #FAST MOVING AVERAGE
    macd_FMA = macd_SMA.ewm(span=FMA_SIGNAL_VALUE, adjust=False, min_periods=FMA_SIGNAL_VALUE).mean()
    #MACD CONVERGENCE DIFFERENCE
    return (macd_SMA - macd_FMA).values

def tradeOnMACDConvergenceDifference(macdTrendDifferenceValues):
    currentMACDDifference = macdTrendDifferenceValues[-1]
    lastMACDDifference = macdTrendDifferenceValues[-2]
    print("CURRENT MAC DIFFERENCE: " + str(currentMACDDifference))
    print("LAST MACD DIFFERENCE: " + str(lastMACDDifference))
    if (currentMACDDifference > 0 and lastMACDDifference < 0):
        #BUY
        rh.buyCryptoInDollars('BTC', BTC_MIN_PURCHASE_SELL_AMOUNT)
    elif(currentMACDDifference < 0 and lastMACDDifference > 0):
        #SELL
        rh.sellCryptoInDollars('BTC', BTC_MIN_PURCHASE_SELL_AMOUNT)
def run():
    rh.runRobinhoodChecks()
    trendDifference = getMACDTrendDifference()
    tradeOnMACDConvergenceDifference(trendDifference)