import plotly.graph_objects as go
from random_walk import RandomWalk
from plotly import offline
    
rw = RandomWalk()
rw.fill_walk()

fig = go.Figure(data=[go.Scatter(x=rw.x_values, y=rw.y_values)])
fig.update_xaxes(range=[min(rw.x_values), max(rw.x_values)])  # Используем min и max для определения диапазона
offline.plot(fig, filename='Plotly_files/random_walk_plot.html', auto_open=True)