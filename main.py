import os
import pyotp
import robin_stocks
import robinhood_trading_scripts as robinhoodTradingScripts
import data

def login():
    totp  = pyotp.TOTP('JFVEEUPDGHHDRVD3').now()
    login = robin_stocks.robinhood.login(os.getenv('user_name'), os.environ.get('password'), mfa_code=totp)

def runFiveMinuteIntervalScripts():
    print("Running 5 minute interval scripts")
    login()
    d = data.CryptoData()
    d.getCryptoIntervalPriceChangeFromCurrent('BTC', 'hour', 'day')

def runTenMinuteIntervalScripts():
    print("Running 10 minute interval scripts")
    login()
    robinhoodTradingScripts.check_account_balance()

def runThirtyMinuteIntervalScripts():
    print("Running 30 minute interval scripts")
    login()
    robinhoodTradingScripts.check_account_balance()

if __name__=="__main__":
    runFiveMinuteIntervalScripts()