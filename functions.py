import yfinance as yf

def get_price(coin):
    coin = yf.download(coin, period="1d", interval="1m")

    coin_price = coin['Close']
    coin_price = coin_price[-1]

    return(round(coin_price, 5))