from timetable_Genetic_Algorithm.fitness_func.IModuleForFitnessFunction import IModuleForFitnessFunction
from timetable_Genetic_Algorithm.utils.SingletonBaseClass import SingletonBaseClass


class ModuleRegistration(metaclass=SingletonBaseClass):
    def __init__(self):
        self.__list_of_registered_modules = []

    @property
    def reg_module(self):
        return self.__list_of_registered_modules

    @reg_module.setter
    def reg_module(self, value):
        if issubclass(value, IModuleForFitnessFunction) and value.__name__ not in vars(__builtins__):
            self.__list_of_registered_modules.append(value.__name__)
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

    if issubclass(cls, IModuleForFitnessFunction) and cls.__name__ not in vars(__builtins__):
        ModuleRegistration().reg_module = cls
    else:
        raise TypeError(f"ModuleRegistration cant register this object, |in decorator| {cls}")
    return cls
