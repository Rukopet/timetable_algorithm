from timetable_Genetic_Algorithm.utils.algorithm_settings import AlgorithmSettings


class Lesson:
    """ intersection of main many; timeline unit """

    def __init__(self, num_groups: int, letter_group: str, pedagog_name: str):
        self.linked = False
        self.locked = False
        self.pedagog_name = pedagog_name
        self.main_list = [num_groups, letter_group, pedagog_name]


class GeneratorLessons:
    """ main generator whole table, one on which individ """

    def __int__(self, settings: AlgorithmSettings):
        self._settings = settings

    def gen_lesson(self):
        pass

    def gen_weak(self):
        pass
