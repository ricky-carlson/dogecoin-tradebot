import time
from datetime import datetime
from functions import get_price

performance_price = []
time_list = []

#Loop that gets market data every N minutes for X coin
i = 0
while i < 2:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    time_list.append(current_time)
    performance_price.append(float(get_price("DOGE-USD")))
    
    if len(performance_price) < 2:
        time.sleep(60)
        i += 1
    else:
        i += 1
print(performance_price, time_list)
