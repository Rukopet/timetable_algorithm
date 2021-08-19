from typing import Type, List

from timetable_genetic_algorithm.fitness_utils import ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.fitness_utils import ModuleRegistration
from timetable_genetic_algorithm.utils.Individ import Individ


def get_list_modules_object_list() -> List[ModuleForFitnessFunctionBase]:
    return ModuleRegistration().get_modules_object_list()


def fitness_function(individ: Individ):
    modules = get_list_modules_object_list()

    for timeline in individ.dict_individ.keys():
        for auditory, lesson in individ.dict_individ[timeline].items():
            for module in modules:
                pass
