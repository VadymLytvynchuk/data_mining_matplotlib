
from plotly.graph_objs import Layout
from plotly import offline
from world_fires_data_reader import read_csv

# Plotting data on a map.
dates, lons, lats, brightness =  read_csv()
data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text': brightness,
    'marker': {
        'color': brightness,
        'colorscale': 'YlOrRd',
        'reversescale': False,
        'colorbar':{'title':'Temperature'}
        }
        }]
my_layout = Layout(title= f" World fires map")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='data/world_fires_map.html')