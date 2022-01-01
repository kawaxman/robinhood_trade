import robin_stocks

class Data: 
    #param: ticker- the crypto ticker
    #param: interval - The time between data points. Can be ’15second’, ‘5minute’, ‘10minute’, ‘hour’, ‘day’, or ‘week’. Default is ‘hour’.
    #param: span - The entire time frame to collect data points. Can be ‘hour’, ‘day’, ‘week’, ‘month’, ‘3month’, ‘year’, or ‘5year’. Default is ‘week’
    #param: bound - The times of day to collect data points. ‘Regular’ is 6 hours a day, ‘trading’ is 9 hours a day, ‘extended’ is 16 hours a day, ‘24_7’ is 24 hours a day. Default is ‘24_7’
    def getCryptoHistoricalDataFromKey(self, ticker, interval = 'hour', span = 'week', bound = '24_7', key = ''):
        return robin_stocks.robinhood.get_crypto_historicals(ticker, interval, span, bound, key)