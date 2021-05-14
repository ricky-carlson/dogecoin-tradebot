from functions import get_price, market_data, price_change

performance_price = []
time_price = []
change_price = {}

#Sets the amount of times to loop the live price puller
loop_length = 2

#Gets market data every N minutes for X coin
market_data(performance_price, time_price, loop_length)

#Gets price change during every interval
price_change(performance_price, time_price, change_price)
