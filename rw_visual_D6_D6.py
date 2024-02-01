import matplotlib.pyplot as plt
from die import Die


fig, ax = plt.subplots()
# Создание двух кубиков D6.
die_1 = Die()
die_2 = Die()
max_result = die_1.num_sides + die_2.num_sides
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
bar_labels = ['red', 'blue', '_red', 'orange']

counts = [ str(i)  for i in range(2,(die_1.num_sides + die_2.num_sides)+1)]
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Анализ результатов.
frequencies = []   

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

ax.bar(counts,frequencies ,color = bar_colors)

ax.set_ylabel('Frequency of Result')
ax.set_title('Results of rolling two D6 1000 times')

plt.show()

