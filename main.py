import time
from datetime import datetime
from functions import get_price

performance_price = []
time_price = []
price_change = {}

#Loop that gets market data every N minutes for X coin
i = 0
while i < 2:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    time_price.append(current_time)
    performance_price.append(float(get_price("DOGE-USD")))

    if len(performance_price) < 2:
        time.sleep(60)
        i += 1
    else:
        i += 1

#Calculates change of Nth + 1 price from Nth price 
for i in range(len(performance_price)):
    if (i + 1) < len(performance_price):
        price_change[round(performance_price[i + 1] - performance_price[i], 5)] = time_price[i]
    print("Not enough data to calculate change!")
print(price_change)
