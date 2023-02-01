import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
import sys
import datetime
import math

columns = ["firstSeen"]
df = pd.read_csv("2018_Departures_Arrivals_Heathrow.csv", usecols=columns)
df["firstSeen"] = pd.to_datetime(df["firstSeen"], unit='s')

times = pd.Series(0, pd.date_range("00:00", "23:00", freq="60min").time)

for i in range(len(df)):
    index = df["firstSeen"][i].hour
    if math.isnan(index):
        pass
    else:
        times[index] += 1

figs, ax = plt.subplots()
ax.set_title("Hourly flight frequencies at Heathrow (2019)")
ax.set_ylabel('Frequency')
ax.set_xlabel('Hour')

ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.xaxis.set_minor_formatter(FormatStrFormatter('% 1.0f'))

for i in range(24):
    plt.bar(i, times[i])


plt.show()


print(times)
