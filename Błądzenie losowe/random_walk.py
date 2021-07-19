from random import choice

class RandomWalk():
    """Klasa przeznaczona do wygenerowania bładzenia losowego"""

    def __init__(self, num_points=10000):
        """Inicjalizacja atrybutów bładzenia"""
        self.num_points = num_points

        #Punkt początkowy ma wspólrzędne(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Wygenerowanie wszystkich punktów dla bładzenia losowego."""

        #Wykonywanie kroków aż do chwili osiągniecia oczekiwanej liczby punktów.
        while len(self.x_values) < self.num_points:

            #Ustalenie kierunku oraz odległości do pokonania w tym kierunku.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance

            #Odrzucanie ruchów które prowadzą do nikąd.
            if x_step == 0 and y_step == 0:
                continue

            #Ustalenie następnych wartości X i Y.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

