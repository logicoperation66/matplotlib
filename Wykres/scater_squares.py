##Metoda scatter do wyświetlania serii punktów

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, s=5)

#Zdefiniowanie tytułu wykresu i etykiety osi
ax.set_title("Kwadrat liczby", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

#Zdefiniowanie zakresu dla każdej osi
ax.axis([0, 1100, 0, 1100000])

plt.savefig('sqares_plot.png', bbox_inches='tight')
