from typing import Type, List

from timetable_genetic_algorithm.fitness_utils import ModuleRegistration
from timetable_genetic_algorithm.fitness_utils.module_for_fitness_function_base import ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.fitness_utils.shared_soures import Lesson, SharedData
from timetable_genetic_algorithm.logger import LoggerUtils
from timetable_genetic_algorithm.utils.Individ import Individ

# don`t touch this imports ->>>
from timetable_genetic_algorithm.fitness_modules import groups_no_gaps, pedagogs_no_gaps, pedagogs_uniqueness, \
    groups_uniqueness, groups_num_lesson, discipline_name, discipline_type, audience_specialization, \
    audience_hard_link, discipline_weight_day, discipline_weight_week

from timetable_genetic_algorithm.utils.algorithm_settings import AlgorithmSettings


def get_list_modules_object_list() -> List[ModuleForFitnessFunctionBase]:
    return ModuleRegistration().get_modules_object_list()


def fitness_function(table_settings: AlgorithmSettings, individ: Individ, log: LoggerUtils):
    shared_data = SharedData()

    # Initialization list of modules
    ModuleRegistration().generate_modules_object_list(table_settings, shared_data)
    modules = get_list_modules_object_list()
    # shared_data.all_rules = generator_rules_matrix(modules)

    # get ref on dict in log for current individ
    current_individ_dict = log.penalty[individ.id_individ]

    for timeline in individ.dict_individ.keys():
        for auditory, lesson in individ.dict_individ[timeline].items():
            shared_data.current_timeline = timeline
            shared_data.current_audience = auditory
            shared_data.current_lesson = lesson
            for module in modules:
                current_individ_dict[module.get_module_naming()] = \
                    current_individ_dict.get(module.get_module_naming(), 0) + module.get_fitness_penalty()

    sum_penalty = 0
    for module in modules:
        current_individ_dict[module.get_module_naming()] = \
            current_individ_dict.get(module.get_module_naming(), 0) + module.final_action()
        sum_penalty += current_individ_dict[module.get_module_naming()]
    current_individ_dict["sum"] = sum_penalty

