"""Domyślnie aplikacja ma porównywać energie kinetyczną jaka mają asteroidy
rozpędzone do określonej prędkości na wykresie energii kinetycznej obiektu o
masie x rozpędzonego do prędkości światłą"""

# Poprawka żeby prawidłowo wykonać to zadanie potrzebujemy relatywistycznej
# postaci wzoru. gdyż wzór (
# m*v**2)/2 jest uproszczony i nie da się
# go zastosować przy prędkości światła... Do dokończenia




import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

c = 299792458


fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(0, 100))
line, = ax.plot([], [])

x_data = []
y_data = []

def init():
    line.set_data([], [])
    return line




def animate(v):
    x_data.append(v)
    y_data.append((1*v**2)/2)

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,

animation = FuncAnimation(fig, func=animate, frames=np.arange(0, c, 1),
                          interval=1)

plt.show()