import robin_stocks

#constants
robinhood_account_minimum = 5.00

def account_balance_check() -> bool:
    buying_power = robin_stocks.robinhood.build_user_profile(info=['account_buying_power'])
    print("Buying Power: " + buying_power)
    return buying_power > robinhood_account_minimum

