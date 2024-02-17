import csv
from datetime import datetime

filename = 'data/World_fires_Global_48h.csv'


def read_csv():
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader) # вызывается только один раз для получения первой строки файла c заголовками
        #header_diagram = next(reader)
        # Чтение дат, максимальных и минимальных температур из файла.
        dates, lons, lats, brightness  = [], [], [], []
        index_latitude  = header_row.index('latitude')
        index_longitude = header_row.index('longitude')
        index_brightness  = header_row.index('brightness')
        index_date = header_row.index('acq_date')
        for row in reader:
            current_date = datetime.strptime(row[index_date],"%Y-%m-%d")
            try:
                longitude = float(row[index_longitude]) # longitude
                latitude  = float(row[index_latitude])  # latitude
                bright_kelvin = float(row[index_brightness]) # brightness (measured in Kelvin)
                bright_cels = int(bright_kelvin- 273.15)
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                lons.append(longitude)
                lats.append(latitude)
                dates.append(current_date)
                brightness.append(bright_cels)
        #print(highs)
        #print(lows)
    return dates, lons, lats, brightness