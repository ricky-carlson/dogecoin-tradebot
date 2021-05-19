import time
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

#Pulls pricing information from Yahoo Finance using the yfinance library
def get_price(coin):
    coin = yf.download(coin, period="1d", interval="1m")

    coin_price = coin['Close']
    coin_price = coin_price[-1]

    return(round(coin_price, 5))

#Historical Market Data
#Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
#Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
def historic_data(ticker, period, interval):
    ticker = yf.download(ticker, period=period, interval=interval)
    ticker_price = ticker['Close']

    return(round(ticker_price, 2))

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

#Calculates price change between every interval period
def price_change(price, current_time, change):
    for x in range(len(price)):
        if (x + 1) < len(price):
            change[round((price[x + 1] - price[x])/price[x], 5)] = current_time[x + 1]

#Plots price information
#Prints price chart of ticker
#Accepts historic ticker pricing information
#Optional moving average argument, must be of type INT
def price_chart(ticker_data, moving_average = False):
    df = pd.DataFrame(ticker_data)
    plt.plot(df, color="Black")
    if (moving_average != False):
        sma = df.rolling(moving_average).mean()
        plt.plot(sma, color="Blue")
    plt.show()
