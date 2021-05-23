from functions import get_price, live_data, price_change, historic_data, price_chart

performance_price = []
time_price = []
change_price = {}

#Sets the amount of times to loop the live price puller
loop_length = 2

#Gets market data every N minutes for X coin
live_data(performance_price, time_price, loop_length)

#Gets price change during every interval
price_change(performance_price, time_price, change_price)
