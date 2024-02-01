from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Создание двух кубиков D6.
die_1 = Die()
die_2 = Die()
# Моделирование серии бросков с сохранением результатов в списке.
#results = []
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]
#for roll_num in range(1000):
   # result = die_1.roll() * die_2.roll()
   # results.append(result)

# Анализ результатов.
#frequencies = []   
max_result = die_1.num_sides + die_2.num_sides
frequencies =[results.count(value) for value in range(2, max_result+1)]
#for value in range(2, max_result+1): 
    #frequency = results.count(value)
    #frequencies.append(frequency)
print(frequencies)
# Визуализация результатов.
x_values = list(range(2, max_result+1)) 
data = [Bar(x=x_values, y = frequencies)] # набор данных, который будет форматироваться в виде столбцовой диаграммы

x_axis_config = {'title': 'Result', 'dtick': 1}  # 'dtick' управляет расстоянием между делениями на оси x
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6  1000 times',
                    xaxis=x_axis_config, yaxis= y_axis_config ) # Layout возвращает объект, который задает макет и конфигурацию диаграммы в целом
offline.plot({'data':data, 'layout': my_layout}, filename='Plotly_files/d6_d6.html')