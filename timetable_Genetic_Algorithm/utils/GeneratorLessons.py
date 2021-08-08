import pandas as pd

from timetable_Genetic_Algorithm.utils.algorithm_settings import AlgorithmSettings


def util_diff_tuples(x):
    return int(x[0]) - int(x[1])


class Individ:
    """ individ with reload __str__ """

    def __init__(self, dict_ind: dict, settings: AlgorithmSettings):
        self.dict_individ = dict_ind
        self.settings = settings

    # def __str__(self):
    #     for day in range(6):
    #         print("--------------------------" * 2, f'day {day}', "--------------------------" * 3, sep=' | ')
    #         for timeline in range(self.settings.AMOUNT_TIMELINES_IN_DAY):
    #             lst = [x for x in range(self.dict_individ[timeline])]
    #             print(timeline, *lst, sep="\t|\t", end="--------------------------" * 3)
    #         print()


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
        df = settings.data_from_front.groupsJSON.valueDF
        return [tuple([tuple([group[0], group[1]]),
                       key,
                       value.get("pedagog"),
                       util_diff_tuples(df.loc[df["number"] == group[0]][["max_days", "saturday_not_study"]].values[0]),
                       settings.TIME_FIRST_LESSON_SECOND_SHIFT
                       if df.loc[df["number"] == group[0]]["second_shift_study"].values[0] else 0])
                for group in settings.GROUPS_LIST
                for key, value in settings.getGroupData(group).items()
                for _ in range(value["load"])]
