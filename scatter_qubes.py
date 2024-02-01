import matplotlib.pyplot as plt

x_values = list(range(1, 5000))
y_values = [x**3 for x in x_values]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.YlOrRd_r, s =20) # c = 'green'
# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
# Назначение размера шрифта делений на осях.
ax.tick_params(axis = 'both', which = 'major',labelsize = 14)
# Назначение диапазона для каждой оси.
ax.axis()
plt.show()
#plt.savefig('squares_plot.png', bbox_inches='tight')
