import os
import pyotp
import robin_stocks
import BTC_MACD_Script as btcScript

def login():
    totp  = pyotp.TOTP('JFVEEUPDGHHDRVD3').now()
    login = robin_stocks.robinhood.login(os.getenv('user_name'), os.environ.get('password'), mfa_code=totp)

def main():
    print("Running scripts")
    login()
    btcScript.run()

if __name__=="__main__":
    main()