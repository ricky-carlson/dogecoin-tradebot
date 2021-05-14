import time
import yfinance as yf
from datetime import datetime

#Pulls pricing information from Yahoo Finance using the yfinance library
def get_price(coin):
    coin = yf.download(coin, period="1d", interval="1m")

    coin_price = coin['Close']
    coin_price = coin_price[-1]

    return(round(coin_price, 5))

#Gets market data every N minutes for X coin
def market_data(price, current_time, loop):
    i = 0
    while i < loop:
        now = datetime.now()
        time_now = now.strftime("%H:%M:%S")

        current_time.append(time_now)
        price.append(float(get_price("DOGE-USD")))

        if len(price) < loop:
            time.sleep(60)
            i += 1
        else:
            i += 1

def price_change(price, current_time, change):
    for x in range(len(price)):
        if (x + 1) < len(price):
            change[round((price[x + 1] - price[x])/price[x], 5)] = current_time[x+1]
