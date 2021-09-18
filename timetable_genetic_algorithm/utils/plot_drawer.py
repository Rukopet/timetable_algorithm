import matplotlib.pyplot as plt


class PlotDrawer:
    def __init__(self):
        self._mean_fitness_values = []
        self._max_fitness_values = []

    def mean_append(self, mean: int):
        self._mean_fitness_values.append(mean)

    def max_append(self, best: int):
        self._max_fitness_values.append(best)

    def show_plot(self):
        plt.plot(self._max_fitness_values, color='green')
        plt.plot(self._mean_fitness_values, color='red')
        plt.xlabel('Поколение')
        plt.ylabel('Макс/средняя приспособленность')
        plt.title('Зависимость максимальной и средней приспособленности от поколения')
        plt.show()
