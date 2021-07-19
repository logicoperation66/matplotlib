import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Tworzenie nowego bładzenia losowego dopuki program pozostaje aktywny.
while True:
    # Przygotowanie danych bładzenia losowego i wyświetlanie punktów.
    number_of_points = int(input("Podaj ile losowych punktów wygenerować: "))
    rw = RandomWalk(number_of_points)
    rw.fill_walk()

    # Wyświetlanie punktów blądzenia losowego.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(18,10))

    ax.scatter(rw.x_values, rw.y_values, c=range(rw.num_points), cmap=plt.cm.Blues,
                edgecolor='none', s=3)

    #ax.plot(rw.x_values, rw.y_values, linewidth=3)

    #Podkreślenie pierwszego i ostatniego punktu bładzenia losowego.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)
    #Ukrycie osi.
    ax.get_xaxis().set_visible(0)
    ax.get_yaxis().set_visible(0)

    plt.show()
    keep_running = input("Utwórz kolejne bładzenie losowe? (t/n): \n")
    if keep_running == 'n':
        break

