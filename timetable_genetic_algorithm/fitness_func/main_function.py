from typing import Type, List

from timetable_genetic_algorithm.fitness_func import generator_rules_matrix
from timetable_genetic_algorithm.fitness_utils import ModuleRegistration
from timetable_genetic_algorithm.fitness_utils.module_for_fitness_function_base import ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.fitness_utils.shared_soures import Lesson, SharedData
from timetable_genetic_algorithm.logger import LoggerUtils
from timetable_genetic_algorithm.utils.Individ import Individ

# don`t touch this imports ->>>
from timetable_genetic_algorithm.fitness_modules import groups_no_gaps, pedagogs_no_gaps

from timetable_genetic_algorithm.utils.algorithm_settings import AlgorithmSettings
from timetable_genetic_algorithm.utils.our_typing import Audience


def get_list_modules_object_list() -> List[ModuleForFitnessFunctionBase]:
    return ModuleRegistration().get_modules_object_list()


def fitness_function(table_settings: AlgorithmSettings, individ: Individ):
    shared_data = SharedData()

    # Initialization list of modules
    ModuleRegistration().generate_modules_object_list(table_settings, shared_data)
    modules = get_list_modules_object_list()
    # shared_data.all_rules = generator_rules_matrix(modules)

    log = LoggerUtils({individ.id_individ: {}})
    name_dict_log = log.penalty[individ.id_individ]
    for timeline in individ.dict_individ.keys():
        for auditory, lesson in individ.dict_individ[timeline].items():
            shared_data.current_timeline = timeline
            shared_data.current_audience = auditory
            shared_data.current_lesson = lesson
            for module in modules:
                name_dict_log[module.get_module_naming()] = \
                    name_dict_log.get(module.get_module_naming(), 0) + module.get_fitness_penalty()

    for module in modules:
        name_dict_log[module.get_module_naming()] = \
            name_dict_log.get(module.get_module_naming(), 0) + module.final_action()
