import pandas as pd

from timetable_Genetic_Algorithm.utils.algorithm_settings import AlgorithmSettings


# class Tmp(list):
#     def __init__(self, ):
#         super().__init__()
#         [num_groups, letter_group, pedagog_name]


class Lesson:
    """ intersection of main many; timeline unit """

    def __init__(self, num_groups: int, letter_group: str, pedagog_name: str):
        self.audience = None
        self.linked = False
        self.locked = False
        self.pedagog_name = pedagog_name
        self.current_tuple = None


class GeneratorLessons:
    """ main generator whole table, one on which individ """
    j = 1

    def __init__(self, settings: AlgorithmSettings, week: list):
        self._settings = settings
        self.main_tuple_list = week
        # self.main_dataDF = pd.DataFrame.from_dict(settings.main_data, )
        # print(self.main_dataDF)

    def gen_lesson(self):
        pass

    def gen_week(self):
        pass

    @staticmethod
    def gen_overall_pool(settings: AlgorithmSettings):
        return [tuple([group[0], group[1], key, value.get("pedagog")])
                for group in settings.GROUPS_LIST
                for key, value in settings.getGroupData(group).items()
                for _ in range(value["load"])]
