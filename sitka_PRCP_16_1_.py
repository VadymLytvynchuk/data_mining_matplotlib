import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # вызывается только один раз для получения первой строки файла c заголовками
    # Чтение дат, максимальных и минимальных температур из файла.
    dates, highs, lows, prcp  = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        try:
            high = int(row[7]) # TMAX
            low = int(row[8])  # TMIN
            precipitation = float(row[5])  # precipitation (PRCP) 
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)
            prcp.append(precipitation)
    print(highs)
    print(lows)
    print(prcp)
    #for index, column_header in enumerate(header_row):
       # print(index, column_header)
    
    # Нанесение данных на диаграмму.
    plt.style.use('seaborn-v0_8-deep')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c ='red', alpha = 0.5)
    ax.plot(dates, lows, c ='blue', alpha = 0.5)
    ax.plot(dates, prcp, c ='green', alpha = 0.5)
    plt.fill_between(dates, highs, lows,  facecolor = 'blue', alpha = 0.1)
    # Форматирование диаграммы.
    title = "Daily high, low temperatures and precipitation - 2021\n Sitka"
    plt.title(title, fontsize = 24)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize = 16)
    plt.tick_params(axis='both', which = 'major', labelsize = 16)
    plt.show()