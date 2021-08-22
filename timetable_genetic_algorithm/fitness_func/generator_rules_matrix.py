from typing import Dict, List

from timetable_genetic_algorithm.fitness_utils import ModuleRegistration, Rule, ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.utils import AlgorithmSettings


def generator_rules_matrix(list_of_instances_modules: List[ModuleForFitnessFunctionBase]) -> Dict[Rule, bool]:
    """
    generate rules, temporary generate True like default

    :return: Dict[Rule, bool] | Rule name of rule
    """
    # temporary solution
    return {rule: True for rule in ModuleRegistration().reg_module}
