from typing import Dict, List

from timetable_genetic_algorithm.fitness_utils import ModuleRegistration
from timetable_genetic_algorithm.fitness_utils.module_for_fitness_function_base import ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.fitness_utils.our_typing import Rule
from timetable_genetic_algorithm.utils import AlgorithmSettings


def generator_rules_matrix(list_of_instances_modules: List[ModuleForFitnessFunctionBase]) -> Dict[Rule, bool]:
    """
    generate rules, temporary generate True like default

    :return: Dict[Rule, bool] | Rule name of rule
    """
    # temporary solution
    return {rule.get_module_naming(): True for rule in list_of_instances_modules}
