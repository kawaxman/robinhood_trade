import robin_stocks

#constants
robinhood_account_minimum = 5.00

#param- transactionsAmount: the transaction amount in dollars
def hasSufficientBuyingPower(transactionAmount = 0):
        buying_power = float(robin_stocks.robinhood.profiles.load_account_profile()['crypto_buying_power']) - transactionAmount
        print("Current buying power: " + str(buying_power))
        return buying_power > robinhood_account_minimum

#param- ticker: stock ticker (ex:'BTC')
#param- dollarAmount: the amount of dollars to buy of the cryptocurrency
def buyCryptoInDollars(ticker, dollarAmount):
    print("Attempting to buy $" + str(dollarAmount) + " of " + ticker + ".")
    if (hasSufficientBuyingPower(dollarAmount)):
        robin_stocks.robinhood.order_buy_crypto_by_price(ticker,dollarAmount)
        print("Order has been placed")
    else:
        print("There is not enough buying power over the specified account minimum to complete this transaction.")

#param- ticker: stock ticker (ex:'BTC')
#param- dollarAmount: the amount of dollars to buy of the cryptocurrency
def sellCryptoInDollars(ticker, dollarAmount):
    print("Attempting to sell $" + str(dollarAmount) + " of " + ticker + ".")
    return robin_stocks.robinhood.order_sell_crypto_by_price(ticker, dollarAmount)

def checkCryptoUnfilledOrders():
    orders = robin_stocks.robinhood.orders.get_all_open_crypto_orders()
    for order in orders:
        if (order['state'] != 'filled'):
            robin_stocks.robinhood.cancel_crypto_order(order['id'])
            print("Cancelled an unfilled order.")

def runRobinhoodChecks():
    checkCryptoUnfilledOrders()