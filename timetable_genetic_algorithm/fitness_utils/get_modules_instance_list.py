from timetable_genetic_algorithm.fitness_utils import ModuleForFitnessFunctionBase, SharedData
from timetable_genetic_algorithm.utils import AlgorithmSettings
from timetable_genetic_algorithm.fitness_utils import ModuleRegistration


def get_modules_object_list(settings: AlgorithmSettings, shared_data: SharedData):
    """

    :param settings:
    :param shared_data:
    :return:
    """
    return [module(settings, shared_data) for module in ModuleRegistration().reg_module]
