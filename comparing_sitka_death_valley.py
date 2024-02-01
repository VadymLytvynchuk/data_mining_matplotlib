import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_sitka = 'data/sitka_weather_2021_full.csv'
file_death_valley = 'data/death_valley_2021_full.csv'

def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader) # вызывается только один раз для получения первой строки файла c заголовками
        header_diagram = next(reader)
        # Чтение дат, максимальных и минимальных температур из файла.
        dates, highs, lows  = [], [], []
        index_high = header_row.index('TMAX')
        index_low  = header_row.index('TMIN')
        for row in reader:
            current_date = datetime.strptime(row[2],"%Y-%m-%d")
            try:
                high = int(row[index_high]) # TMAX
                low = int(row[index_low])  # TMIN
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                highs.append(high)
                lows.append(low)
                dates.append(current_date)
        #print(highs)
        #print(lows)
    return dates, highs, lows, header_diagram[1]

#for index, column_header in enumerate(header_row):
    # print(index, column_header)

dates_sitka, highs_sitka, lows_sitka, header_diagram    = read_csv(file_sitka)
dates_valley, highs_valley, lows_valley, header_diagram_1 = read_csv(file_death_valley)   

# Plot data from Sitka
plt.style.use('seaborn-v0_8-deep')
fig, ax = plt.subplots()
ax.plot(dates_sitka, highs_sitka, c ='red', alpha = 0.5)
ax.plot(dates_sitka, lows_sitka, c ='blue', alpha = 0.5)
plt.fill_between(dates_sitka, highs_sitka, lows_sitka,  facecolor = 'blue', alpha = 0.1)

# Plot data from Death Valley
ax.plot(dates_valley, highs_valley, c ='orange', alpha = 0.5)
ax.plot(dates_valley, lows_valley, c ='green', alpha = 0.5)
plt.fill_between(dates_valley, highs_valley, lows_valley,  facecolor = 'green', alpha = 0.1)

# Set plot details
# Установка масштаба для оси Y
ax.set_ylim(0, max(max(highs_sitka), max(highs_valley)) + 10)
# Установка подписи для оси Y
ax.set_ylabel("Temperature (F)", fontsize=16)
# Форматирование диаграммы.
title = f"Daily high, low temperatures - 2021\n {header_diagram},\n {header_diagram_1}"
plt.title(title, fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
#plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis='both', which = 'major', labelsize = 16)
plt.show()