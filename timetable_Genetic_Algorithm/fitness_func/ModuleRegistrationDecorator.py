from timetable_Genetic_Algorithm.utils.SingletonBaseClass import SingletonBaseClass


class ModuleRegistrationDecorator(metaclass=SingletonBaseClass):
    __list_of_registered_classes = []

    def __init__(self, class_for_registration, *args, **kwargs):
        self.__list_of_registered_classes.append(class_for_registration)

    def __call__(self, *args, **kwargs):
        print("k")

    def get_list_names(self):
        return self.__list_of_registered_classes
