from abc import abstractmethod, ABCMeta
from typing import Optional


class ModuleForFitnessFunctionBase:
    __metaclass__ = ABCMeta

    # flag for identify needed actions for post cycle actions
    IS_HAVE_FINAL_ACTION = False

    def __init__(self, shared_data, settings):
        self.shared_data = shared_data
        self.settings = settings

    @abstractmethod
    def get_fitness_penalty(self) -> int:
        pass

    @abstractmethod
    def get_module_description(self) -> str:
        pass

    @abstractmethod
    def get_module_naming(self) -> str:
        pass

    @abstractmethod
    def change_shared_data(self) -> None:
        pass

    def final_action(self) -> int:
        return 0
