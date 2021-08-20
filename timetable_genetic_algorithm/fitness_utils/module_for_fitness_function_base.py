from abc import abstractmethod, ABCMeta


class ModuleForFitnessFunctionBase:
    __metaclass__ = ABCMeta

    def __init__(self, shared_data, settings):
        self._data_class = shared_data
        self._settings = settings

    @abstractmethod
    def get_fitness_penalty(self) -> int:
        pass

    @abstractmethod
    def get_module_description(self):
        pass

    @abstractmethod
    def get_module_naming(self) -> str:
        pass

    @abstractmethod
    def change_shared_data(self):
        pass
