from dataclasses import dataclass

from timetable_genetic_algorithm.utils import AlgorithmSettings, MAX_LESSONS_IN_DAY
from timetable_genetic_algorithm.utils.settings_generations import AMOUNT_TIMELINES_IN_DAY

NO_SINGLE_PEDAGOG = 1000

NO_SINGLE_GROUP = 1000

WINDOWS_PEDAGOG = 100

WINDOWS_GROUP = 1000

FIRST_LESSON_GROUP = 1000


class FitnessSettingData:
    """draft fitness class"""

    def __init__(self, settings: AlgorithmSettings, individ: dict):
        """

        :type settings: AlgorithmSettings
        :type individ: dict
        """
        self.settings = settings
        self.individ = individ
        self.dict_count_pedago_nosingle = {}
        self.dict_count_group_nosingle = {}
        self.dict_count_pedago_windows = {}
        self.dict_count_group_windows = {}
        self.count_pedag_error_nosingle = 0
        self.count_group_error_nosingle = 0
        self.count_group_error_first_lesson = 0
        self.count_pedag_error_window = 0
        self.count_group_error_window = 0

    def count_pedago_no_single(self, lesson: tuple, timeline: int):
        if lesson:
            if timeline in self.dict_count_pedago_nosingle:
                if lesson[2] in self.dict_count_pedago_nosingle[timeline]:
                    self.dict_count_pedago_nosingle[timeline][lesson[2]] += 1
                    self.count_pedag_error_nosingle += NO_SINGLE_PEDAGOG
                else:
                    self.dict_count_pedago_nosingle[timeline][lesson[2]] = 1
            else:
                self.dict_count_pedago_nosingle[timeline] = {lesson[2]: 1}

    def count_pedago_windows(self, lesson: tuple, timeline: int):
        day = timeline // AMOUNT_TIMELINES_IN_DAY
        time = timeline % AMOUNT_TIMELINES_IN_DAY
        if lesson:
            if day in self.dict_count_pedago_windows.keys():
                if lesson[2] in self.dict_count_pedago_windows[day].keys():
                    if time > self.dict_count_pedago_windows[day][lesson[2]] \
                            [len(self.dict_count_pedago_windows[day][lesson[2]]) - 1]:
                        self.count_pedag_error_window += (time - self.dict_count_pedago_windows[day][lesson[2]] \
                            [len(self.dict_count_pedago_windows[day][lesson[2]]) - 1] - 1) * WINDOWS_PEDAGOG
                        self.dict_count_pedago_windows[day][lesson[2]].append(time)
                else:
                    self.dict_count_pedago_windows[day][lesson[2]] = [time]
            else:
                self.dict_count_pedago_windows[day] = {lesson[2]: [time]}

    def count_group_windows(self, lesson: tuple, timeline: int):
        day = timeline // AMOUNT_TIMELINES_IN_DAY
        time = timeline % AMOUNT_TIMELINES_IN_DAY
        if lesson:
            if day in self.dict_count_group_windows.keys():
                if lesson[0] in self.dict_count_group_windows[day].keys():
                    if time > self.dict_count_group_windows[day][lesson[0]] \
                            [len(self.dict_count_group_windows[day][lesson[0]]) - 1]:
                        self.count_group_error_window += (time - self.dict_count_group_windows[day][lesson[0]] \
                            [len(self.dict_count_group_windows[day][lesson[0]]) - 1] - 1) * WINDOWS_GROUP
                        self.dict_count_group_windows[day][lesson[0]].append(time)
                else:
                    self.dict_count_group_windows[day][lesson[0]] = [time]
            else:
                self.dict_count_group_windows[day] = {lesson[0]: [time]}

    def count_group_no_single(self, lesson: tuple, timeline: int):
        if lesson:
            if timeline in self.dict_count_group_nosingle:
                if lesson[0] in self.dict_count_group_nosingle[timeline]:
                    self.dict_count_group_nosingle[timeline][lesson[0]] += 1
                    if lesson[1] not in self.settings.DISCIPLINES_LIST_WITH_PAIR or\
                            lesson[1] in self.settings.DISCIPLINES_LIST_WITH_PAIR and\
                            self.dict_count_group_nosingle[timeline][lesson[0]] > 2:
                        self.count_group_error_nosingle += NO_SINGLE_GROUP
                    if lesson[1] in self.settings.DISCIPLINES_LIST_WITH_PAIR and\
                            self.dict_count_group_nosingle[timeline][lesson[0]] == 2:
                        self.count_group_error_nosingle -= NO_SINGLE_GROUP
                else:
                    self.dict_count_group_nosingle[timeline][lesson[0]] = 1
                    if lesson[1] in self.settings.DISCIPLINES_LIST_WITH_PAIR:
                        self.count_group_error_nosingle += NO_SINGLE_GROUP
            else:
                self.dict_count_group_nosingle[timeline] = {lesson[0]: 1}

    def count_group_first_lesson(self, lesson: tuple, timeline: int):
        if lesson:
            if lesson[4] > timeline or timeline > lesson[4] + MAX_LESSONS_IN_DAY[lesson[0][0]]:
                self.count_group_error_first_lesson += FIRST_LESSON_GROUP

    def main_loop(self):
        for timeline in self.individ.keys():
            for lesson in self.individ[timeline].values():
                self.count_pedago_no_single(lesson, timeline)
                self.count_pedago_windows(lesson, timeline)
                self.count_group_no_single(lesson, timeline)
                self.count_group_first_lesson(lesson, timeline % AMOUNT_TIMELINES_IN_DAY)
                self.count_group_windows(lesson, timeline)
