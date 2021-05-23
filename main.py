from functions import get_price, live_data, price_change, historic_data, price_chart

performance_price = []
time_price = []
change_price = {}

#Sets the amount of times to loop the live price puller
loop_length = 2

exchange_fee = .002 # % Fee charged to buy/sell on specified exchange


current_price = get_price("DOGE-USD")

purchase_price = round(current_price * (1 + exchange_fee), 6)
transaction_cost = round(purchase_price - current_price, 6)
breakeven_price = round(purchase_price + (purchase_price * exchange_fee), 6)
breakeven_percent = (breakeven_price - current_price)/current_price

print(f"Current price: ${current_price}\nPurchase price: ${purchase_price}\nBreakeven price: ${breakeven_price}\nBreakeven percent: {round(breakeven_percent*100, 2)}%")

