"""
constants for genetic algorithm
P_* - probability
"""
import os

P_MUTATION = 0.8
TOTAL_POPULATION = 10
P_CROSSOVER = 0.8
AMOUNT_TIMELINES_IN_DAY = 14
TIME_FIRST_LESSON_SECOND_SHIFT = 6
COUNT_GENERATIONS = 1
EXIT_OF_ALGORITHM = 1000

from pathlib import Path
DATA_PATH = str(Path(os.path.abspath(__file__)).parent.parent.parent) + '/data' + '/'

p = 0
