import time
from datetime import datetime
from functions import get_price

#Match performance_price with time_list to create time stamp
performance_price = []
time_list = []

#Loop that gets market data every N minutes for X coin
i = 0
while i < 5:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    time_list.append(current_time)
    performance_price.append(float(get_price("DOGE-USD")))
    
    if len(performance_price) < 5:
        time.sleep(60)
        i += 1
    else:
        i += 1
print(performance_price, time_list)
