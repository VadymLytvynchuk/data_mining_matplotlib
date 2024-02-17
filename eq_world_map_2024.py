
from plotly.graph_objs import Layout
from plotly import offline
from eq_explore_data import reading_json_geo

# Plotting data on a map.
lons, lats, mags, hover_texts, my_layout =  reading_json_geo()
data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text': hover_texts,
    'marker': {
        'size': [5* mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar':{'title':'Magnitude'}
        }
        }]
my_layout = Layout(title= f"{my_layout}")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='data/global_earthquakes_2024.html')