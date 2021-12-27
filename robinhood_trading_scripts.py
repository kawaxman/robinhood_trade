import robin_stocks
def check_account_balance():
    print(robin_stocks.robinhood.profiles.load_account_profile())