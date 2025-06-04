from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


path = Path('./weather_data/4033854.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

# Enumerate is useful for retrieving indexed lists
# Example, 0, item 1
for index, column_name in enumerate(header_row):
    print(index, column_name)

# Extract snowfall
dates, snowfall = [], []
for row in reader:
    # .strptime() is extremely strict, any white space will botch the analysis
    current_date = datetime.strptime(row[5].strip(), "%Y-%m-%d")
    try:
        snow = float(row[12])
    except ValueError:
        print(f"Missing data for: {current_date}")
    else:
        dates.append(current_date)
        snowfall.append(snow)

# Plotting the snowfall
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, snowfall, color='blue', alpha=0.5)

# Formatting the plot
ax.set_title('Annual Snowfall Near Wray Colorado', fontsize=16)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # Draws date diagonally to prevent overlapping
ax.set_ylabel('Snowfall (in)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()