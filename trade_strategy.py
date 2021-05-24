import matplotlib.pyplot as plt
import yfinance as yf
from functions import get_price

ticker = "fubo".upper()

stock_price = get_price(ticker)
stop_loss = .025 #as percent
entry_percent_limit = .15 #as percent

shares_owned = 20

i = False
while i == False:
    try:
        entry_price = float(input(f"Price must be +/- ${round(entry_percent_limit*stock_price, 2)} above or below ${stock_price}\nEnter entry price: "))
        break
    except:
        print("Your input is not valid, please re-try!")


if (entry_price > stock_price * (1 + entry_percent_limit)) or (entry_price < stock_price * (1 - entry_percent_limit)):
    print("Not a valid entry point!")
    quit()

target_price = round(entry_price * (1 + .2), 2)
stop_loss_price = round(entry_price * (1 - stop_loss), 2)

print(f"\n{ticker} stop loss price: ${stop_loss_price}\n{ticker} target price: ${target_price}")
