### Wizualizacja danych
#Wykres kwadratów kolejnych liczb

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]  # Oś X
squares = [1, 4, 9, 16, 25]     # Oś Y

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.scatter(2,4, s=200)

#Zdefiniowanie tytułu wykresu i etykiety osi
ax.set_title("Kwadrat liczby", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

#Zdefiniowanie wielkości etykiet
ax.tick_params(axis='both',which='major',  labelsize=14)

plt.show()

