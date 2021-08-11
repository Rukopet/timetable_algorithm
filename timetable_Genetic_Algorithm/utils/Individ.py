from timetable_Genetic_Algorithm.utils.algorithm_settings import AlgorithmSettings
import openpyxl


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
