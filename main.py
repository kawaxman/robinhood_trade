import os
import pyotp
import robin_stocks
import robinhood_trading_scripts as robinhoodTradingScripts
def login():
    totp  = pyotp.TOTP(os.getenv('totp_key')).now()
    login = robin_stocks.robinhood.login(os.getenv('user_name'), os.environ.get('password'), mfa_code=totp)

def main():
    print("Running main() function")
    login()
    robinhoodTradingScripts.check_account_balance()

if __name__=="__main__":
    main()