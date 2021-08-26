from typing import Type

from timetable_genetic_algorithm.fitness_utils.shared_soures import SharedData
from timetable_genetic_algorithm.fitness_utils.module_for_fitness_function_base import ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.utils.SingletonBaseClass import SingletonBaseClass
from timetable_genetic_algorithm.utils import AlgorithmSettings


class ModuleRegistration(metaclass=SingletonBaseClass):
    def __init__(self):
        self.__list_of_registered_modules = []
        self.__modules_object_list = []

    @property
    def reg_module(self):
        return self.__list_of_registered_modules

    @reg_module.setter
    # TODO fix dir(__builtins__) not true implement!
    def reg_module(self, value: Type[ModuleForFitnessFunctionBase]):
        if issubclass(value, ModuleForFitnessFunctionBase) and value.__name__ not in dir(__builtins__):
            self.__list_of_registered_modules.append(value)
        else:
            raise TypeError(f"ModuleRegistration cant register this object, |in class reg| {value}")

    def unregister(self, value):
        self.__list_of_registered_modules.remove(value)

    def generate_modules_object_list(self, settings: AlgorithmSettings, shared_data: SharedData):
        """
        generate list of instances registered classes

        :param settings:
        :param shared_data:
        """
        self.__modules_object_list = [module(shared_data, settings) for module in ModuleRegistration().reg_module]

    def get_modules_object_list(self):
        return self.__modules_object_list


def module_register(cls: Type[ModuleForFitnessFunctionBase]):
    """
    Can register only IModuleForFitnessFunction child classes, other undefined
    Use like decorator @

    :param cls: Input class
    :return: cls: Input class
    :raise: TypeError
    """

    if issubclass(cls, ModuleForFitnessFunctionBase) and cls.__name__ not in dir(__builtins__):
        ModuleRegistration().reg_module = cls
    else:
        raise TypeError(f"ModuleRegistration cant register this object, |in decorator| {cls.__name__}")
    return cls
