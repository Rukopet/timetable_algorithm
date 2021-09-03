from typing import List, Dict

from timetable_genetic_algorithm.fitness_func.main_function import fitness_function
from timetable_genetic_algorithm.utils.Individ import Individ
from timetable_genetic_algorithm.utils.algorithm_settings import AlgorithmSettings


def get_count_generation():
    return 200


def main_loop(table_settings: AlgorithmSettings, population: List[Dict]):
    tmp_ind = Individ(population[0], table_settings, 0)
    for generation in range(get_count_generation()):
        ...
    fitness_function(table_settings, tmp_ind)
