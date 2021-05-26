import yfinance as yf
from functions import get_price, historic_data, price_change, chart_price

ticker = "sq".upper()

stock_price = get_price(ticker)
stop_loss = .025 #as percent
entry_percent_limit = .15 #as percent

shares_owned = 2 #quantity of shares owned

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

capital_required = round(entry_price * shares_owned, 2)
max_loss = round((stop_loss_price - entry_price) * shares_owned, 2)
profit = round((target_price - entry_price) * shares_owned, 2)

print(f"\nStock: {ticker}\nCapital required: ${capital_required}\nStop loss price: ${stop_loss_price}\nTarget price: ${target_price}\n\nMax loss: ${max_loss}\nProfit at Target Price: ${profit}")


chart_price(historic_data(ticker, "ytd", "5d"), target_price, stop_loss_price)

