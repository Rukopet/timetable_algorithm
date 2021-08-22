from typing import Type, List

from timetable_genetic_algorithm.fitness_utils import SharedData
from timetable_genetic_algorithm.fitness_utils import ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.fitness_utils import ModuleRegistration
from timetable_genetic_algorithm.logger import LoggerUtils
from timetable_genetic_algorithm.utils.Individ import Individ
from timetable_genetic_algorithm.fitness_modules import groups_no_gaps, pedagogs_no_gaps
from timetable_genetic_algorithm.utils.algorithm_settings import AlgorithmSettings


def get_list_modules_object_list() -> List[ModuleForFitnessFunctionBase]:
    return ModuleRegistration().get_modules_object_list()


def fitness_function(table_settings: AlgorithmSettings, individ: Individ):
    shared_data = SharedData(["asd"])
    ModuleRegistration().generate_modules_object_list(table_settings, shared_data)
    modules = get_list_modules_object_list()

    log = LoggerUtils({individ.id_individ: {}})
    name_dict_log = log.penalty[individ.id_individ]
    for timeline in individ.dict_individ.keys():
        for auditory, lesson in individ.dict_individ[timeline].items():
            for module in modules:
                name_dict_log[module.get_module_naming()] = module.get_fitness_penalty()
