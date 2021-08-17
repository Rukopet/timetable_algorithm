from timetable_Genetic_Algorithm.utils.SingletonBaseClass import SingletonBaseClass


class ModuleRegistrationDecorator(metaclass=SingletonBaseClass):
    def __init__(self):
        self.__list_names = []

    def __call__(self, *args, **kwargs):
        print("k")

    def register_module(self, *args, **kwargs):
        p = 1
        aasd = 3
        # self.__list_names.append(cls.__name__)

    def get_list_names(self):
        return self.__list_names
