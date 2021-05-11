import time
import numpy as np
from datetime import datetime
from functions import get_price

performance_price = []
time_price = []
price_change = {}

time_interval = '1m'

#Loop that gets market data every N minutes for X coin
i = 0
while i < 5:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    time_price.append(current_time)
    performance_price.append(float(get_price("DOGE-USD")))

    if len(performance_price) < 5:
        time.sleep(60)
        i += 1
    else:
        i += 1

#Calculates % change of Nth + 1 price from Nth price
for x in range(len(performance_price)):
    if (x + 1) < len(performance_price):
        price_change[round((performance_price[x + 1] - performance_price[x])/performance_price[x], 5)] = time_interval
    else:
        print("Not enough data to calculate change!")
print("Process complete!")
print(np.average(performance_price))
