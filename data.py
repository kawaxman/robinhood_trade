import robin_stocks

class Data:
    def hasSufficientBuyingPower(self, minimumBuyingPower):
        buying_power = robin_stocks.robinhood.profiles.load_account_profile()['crypto_buying_power']
        print("Current buying power: " + buying_power)
        return float(buying_power) > float(minimumBuyingPower)

    def getPercentageChange(self, new, old):
        return ((new - old)/old) * 100
    


class StockData(Data):
    def test2(self):
        print('test')
        

class CryptoData(Data):
    #param: interval - The time between data points. Can be ’15second’, ‘5minute’, ‘10minute’, ‘hour’, ‘day’, or ‘week’. Default is ‘hour’.
    #param: span - The entire time frame to collect data points. Can be ‘hour’, ‘day’, ‘week’, ‘month’, ‘3month’, ‘year’, or ‘5year’. Default is ‘week’
    def getCryptoIntervalPriceChangeFromCurrent(self, cryptoTicker, interval = 'hour', span = 'week'):
        data = robin_stocks.robinhood.get_crypto_historicals(cryptoTicker, interval, span)
        current_price = robin_stocks.robinhood.get_crypto_quote(cryptoTicker)['mark_price']
        # for t in data:
        #     print(t)
        #     print(self.getPercentageChange(float(current_price), float(t['low_price'])))