from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('/Users/ja1473/pythonic-data-analysis/weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_name in enumerate(header_row):
    print(index, column_name)

# Extract high temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plotting the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')

# Formatting the plot
ax.set_title('Daily High and Low Temperatures 2021', fontsize=16)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # Draws date diagonally to prevent overlapping
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()