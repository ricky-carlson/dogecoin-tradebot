import yfinance as yf
import math
from functions import get_price, historic_data, price_change, chart_price

stop_loss = .025 #as percent
entry_percent_limit = .15 #as percent

#Trading Account Parameters
account_capital = 1000 #total trading capital available
trade_size = .45 #Percent of total capital per trade
capital_per_trade = round(account_capital * trade_size, 0) #Amount of capital used per trade

ticker = "fubo".upper()
stock_price = get_price(ticker)
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

#Stop loss & Target Price numbers
target_price = round(entry_price * (1 + .2), 2)
stop_loss_price = round(entry_price * (1 - stop_loss), 2)

#Purchasable shares within trade parameters
if (entry_price > capital_per_trade):
    print("Not enough account capital to make trade!")
    quit()
shares_owned = math.floor((capital_per_trade / entry_price))

#Trade requirements & loss/profit
capital_required = round(entry_price * shares_owned, 2)
max_loss = round((stop_loss_price - entry_price) * shares_owned, 2)
target_profit = round((target_price - entry_price) * shares_owned, 2)

#Current position profit or loss
p_l = round(((stock_price * shares_owned) - capital_required))

print(f"\nStock: {ticker}\nCapital required: ${capital_required}\nShares owned: {shares_owned}\nStop loss price: ${stop_loss_price}\nTarget price: ${target_price}"
      f"\n\nMax loss: ${max_loss}\nProfit at Target Price: ${target_profit}\n\nCurrent profit/loss: ${p_l}"
)

#chart_price(historic_data(ticker, "ytd", "5d"), target_price, stop_loss_price)
