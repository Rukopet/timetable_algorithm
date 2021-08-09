import pandas as pd

from timetable_Genetic_Algorithm.utils.algorithm_settings import AlgorithmSettings








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

    def gen_lesson(self):
        pass

    def gen_week(self):
        pass

    @staticmethod
    def gen_overall_pool(settings: AlgorithmSettings):
        df = settings.data_from_front.groupsJSON.valueDF
        return [tuple([tuple([group[0], group[1]]),
                       key,
                       value.get("pedagog"),
                       util_diff_tuples(df.loc[df["number"] == group[0]][["max_days", "saturday_not_study"]].values[0]),
                       settings.TIME_FIRST_LESSON_SECOND_SHIFT
                       if df.loc[df["number"] == group[0]]["second_shift_study"].values[0] else 0])
                for group in settings.GROUPS_LIST
                for key, value in settings.get_group_data(group).items()
                for _ in range(value["load"])]
