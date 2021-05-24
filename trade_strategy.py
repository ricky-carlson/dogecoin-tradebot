import matplotlib.pyplot as plt
import yfinance as yf
from functions import get_price

ticker = "DKNG"

stock_price = get_price(ticker)
stop_loss = .05 #as percent

print(f"{ticker} current stock price: ${stock_price}")

i = False
while i == False:
    try:
        entry_price = float(input("Enter entry price: "))
        i = True
        break
    except:
        print("Your input is not valid, please re-try")

if (entry_price > stock_price * 1.15) or (entry_price < stock_price * .85):
    print("Not a valid entry point")
    quit()

target_price = round(entry_price * (1 + .2), 2)
stop_loss_price = round(entry_price * (1 - stop_loss), 2)

print(f"Stop loss percent below current price: {stop_loss*100}%\n{ticker} stop loss price: ${stop_loss_price}\n{ticker} target price: ${target_price}")
