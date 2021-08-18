from abc import abstractmethod, ABCMeta


class IModuleForFitnessFunction:
    __metaclass__ = ABCMeta

    def __init__(self, settings):
        self.__data_class = None

    @property
    def settings_fitness(self):
        if self.__data_class is None:
            return None
        return self.__data_class

    @settings_fitness.setter
    def settings_fitness(self, value):
        self.__data_class = value

    @settings_fitness.getter
    def settings_fitness(self):
        """
            getter for data class of fitness settings

            :return:  private data class name: __data_class
        """
        return self.__data_class

    @settings_fitness.deleter
    def settings_fitness(self):
        self.__data_class = None
