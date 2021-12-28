import robin_stocks

class Data:
    def hasSufficientBuyingPower(minimumBuyingPower) -> bool:
        buying_power = robin_stocks.robinhood.build_user_profile(info=['account_buying_power'])
        print("Buying Power: " + buying_power)
        return buying_power > minimumBuyingPower