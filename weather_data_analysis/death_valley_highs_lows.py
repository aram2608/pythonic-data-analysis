from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('/Users/ja1473/pythonic-data-analysis/weather_data/death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract high temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try: # this one is able to hand errors gracefully rather than crash the whole program
        # very slick
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plotting the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.05)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # alpha controls transparency, fill_between fills inbetween two lines

# Formatting the plot
ax.set_title('Daily High and Low Temperatures 2021', fontsize=16)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # Draws date diagonally to prevent overlapping
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()