import time
import numpy as np
from datetime import datetime
from functions import get_price

performance_price = []
time_price = []
price_change = {}
loopNum = 5
time_interval = '1m'

#Loop that gets market data every N minutes for X coin
i = 0
while i < loopNum:
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time_price.append(current_time)
    performance_price.append(float(get_price("DOGE-USD")))
    
    time.sleep(60) 
    i += 1

#Calculates % change of Nth + 1 price from Nth price
for price in range(len(performance_price) -1):
    if (price + 1) =< len(performance_price):
        price_change[round((performance_price[price + 1] - performance_price[price])/performance_price[price], 5)]
    else:
        print("Finished Calculations")
        
        

print("Process complete!")
print("Average Price: " + np.average(performance_price))
print("Price Changes " + price_change)

