from timetable_genetic_algorithm.fitness_utils import ModuleRegistration
from timetable_genetic_algorithm.utils import AlgorithmSettings


def generator_rules_matrix():
    """
    generate rules, temporary generate True like default

    :param settings: AlgorithmSettings
    :return: Dict[Rule, bool] | Rule name of rule
    """
    # temporary solution
    return {rule: True for rule in ModuleRegistration().reg_module}
