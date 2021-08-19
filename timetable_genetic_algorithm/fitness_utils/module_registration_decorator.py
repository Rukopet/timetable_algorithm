from timetable_genetic_algorithm.fitness_utils.module_for_fitness_function_base import ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.utils.SingletonBaseClass import SingletonBaseClass


class ModuleRegistration(metaclass=SingletonBaseClass):
    def __init__(self):
        self.__list_of_registered_modules = []

    @property
    def reg_module(self):
        return self.__list_of_registered_modules

    @reg_module.setter
    def reg_module(self, value):
        if issubclass(value, ModuleForFitnessFunctionBase) and value.__name__ not in vars(__builtins__):
            self.__list_of_registered_modules.append(value)
        else:
            raise TypeError(f"ModuleRegistration cant register this object, |in class reg| {value}")

    def unregister(self, value):
        self.__list_of_registered_modules.remove(value)


def module_register(cls):
    """
    Can register only IModuleForFitnessFunction child classes, other undefined
    Use like decorator @

    :param cls: Input class
    :return: cls: Input class
    :raise: TypeError
    """

    if issubclass(cls, ModuleForFitnessFunctionBase) and cls.__name__ not in vars(__builtins__):
        ModuleRegistration().reg_module = cls
    else:
        raise TypeError(f"ModuleRegistration cant register this object, |in decorator| {cls.__name__}")
    return cls
