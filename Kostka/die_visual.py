from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

#Utworzenie kości typu D6
die = Die()

#Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analiza wyników
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Wizualizacja wybników
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik'}
y_axis_config = {'title': 'Częstotliwośc występowania wartości'}
my_layout = Layout(title='Wyniki rzycania pojedyńczą kością D6 tysiąc razy',
                   xaxis=x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout,}, filename='d6.html')

print(frequencies)