from typing import List, Dict

from timetable_genetic_algorithm.fitness_func.main_function import fitness_function
from timetable_genetic_algorithm.logger.logger import LoggerUtils
from timetable_genetic_algorithm.utils.Individ import Individ
from timetable_genetic_algorithm.utils.algorithm_settings import AlgorithmSettings


def get_count_generation():
    return 200


def generate_dict_for_logger(population: List[Individ]) -> Dict[int, Dict[str, int]]:
    ret = {
        ind.id_individ: {"instance": ind}
        for ind in population
    }
    ret["max"] = None
    return ret


def main_loop(table_settings: AlgorithmSettings, population: List[Individ]):
    log = LoggerUtils()
    log.penalty = generate_dict_for_logger(population)
    for generation in range(get_count_generation()):
        for individ in population:
            fitness_function(table_settings, individ, log)
        best_individ = log.best_individ
        if best_individ.get("penalty") == 0:
            break

