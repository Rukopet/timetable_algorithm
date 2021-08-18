from abc import abstractmethod, ABCMeta

from timetable_Genetic_Algorithm.fitness_func.module_registration_decorator import module_register


class ModuleForFitnessFunctionBase:
    __metaclass__ = ABCMeta

    def __init__(self, settings):
        self.__data_class = settings

    @abstractmethod
    def get_fitness_penalty(self):
        pass

    @abstractmethod
    def get_module_description(self):
        pass


# TODO delete test code =>>
@module_register
class A(ModuleForFitnessFunctionBase):

    def get_fitness_penalty(self):
        pass

    def get_module_description(self):
        print("A")


def main():

    dell = ["asd", "zxc"]

    from timetable_Genetic_Algorithm.fitness_func.shared_soures import SharedData
    data = SharedData(dell, {i: True for i in dell}, {i: True for i in dell})

    a = A(data)
    print(data.is_current_module_need_check(a.__class__))
    print(data.all_rules)


if __name__ == "__main__":
    main()
