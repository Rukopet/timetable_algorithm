from timetable_genetic_algorithm.utils import AlgorithmSettings, TYPE_DISCIPLINES, MAX_LESSONS_IN_DAY, \
    WEIGHT_DISCIPLINES
from timetable_genetic_algorithm.utils.settings_generations import AMOUNT_TIMELINES_IN_DAY

NO_SINGLE_PEDAGOG = 1000

NO_SINGLE_GROUP = 1000

WINDOWS_PEDAGOG = 100

WINDOWS_GROUP = 1000

FIRST_LESSON_GROUP = 1000

DISCIPLINES_NAME = 100

DISCIPLINES_TYPE = 100

DISCIPLINES_WEIGHT_DAY = 100

DISCIPLINES_WEIGHT_WEEK = 100

AUDIENCE_HARD_LINK = 1000

AUDIENCE_SPECIALIZATION = 100


class FitnessSettingData:
    """draft fitness class"""

    def __init__(self, settings: AlgorithmSettings, individ: dict):
        """
        init class object function

        :type settings: AlgorithmSettings
        :type individ: dict
        """
        self.settings = settings
        self.individ = individ

        self.dict_count_pedago_nosingle = {}
        self.dict_count_group_nosingle = {}
        self.dict_count_pedago_windows = {}
        self.dict_count_group_windows = {}
        self.dict_count_disc_name = {}
        self.dict_count_disc_type = {}
        self.dict_count_disc_weight_day = {}
        self.dict_count_disc_weight_week = {}

        self.count_pedag_error_nosingle = 0
        self.count_group_error_nosingle = 0
        self.count_group_error_first_lesson = 0
        self.count_pedag_error_window = 0
        self.count_group_error_window = 0
        self.count_disc_error_name = 0
        self.count_disc_error_type = 0
        self.count_disc_error_weight_day = 0
        self.count_disc_error_weight_week = 0

    def count_pedago_no_single(self, lesson: tuple, timeline: int):
        """
        Pedagogs fitness function for check of single timeline - single pedagog

        :param lesson: tuple
        :param timeline: int
        :return: None
        """
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
        """
        Pedagogs fitness function for check of no windows in each pedagogs schedule

        :param lesson: tuple
        :param timeline: int
        :return: None
        """
        day = timeline // AMOUNT_TIMELINES_IN_DAY
        time = timeline % AMOUNT_TIMELINES_IN_DAY
        if lesson:
            if day in self.dict_count_pedago_windows.keys():
                if lesson[2] in self.dict_count_pedago_windows[day].keys():
                    if time > self.dict_count_pedago_windows[day][lesson[2]]:
                        self.count_pedag_error_window += (time - self.dict_count_pedago_windows[day][lesson[2]] - 1) \
                                                         * WINDOWS_PEDAGOG
                        self.dict_count_pedago_windows[day][lesson[2]] = time
                else:
                    self.dict_count_pedago_windows[day][lesson[2]] = time
            else:
                self.dict_count_pedago_windows[day] = {lesson[2]: time}

    def count_group_windows(self, lesson: tuple, timeline: int):
        """
         Groups fitness function for check of no windows in each Group schedule

        :param lesson: tuple
        :param timeline: int
        :return: None
        """
        day = timeline // AMOUNT_TIMELINES_IN_DAY
        time = timeline % AMOUNT_TIMELINES_IN_DAY
        if lesson:
            if day in self.dict_count_group_windows.keys():
                if lesson[0] in self.dict_count_group_windows[day].keys():
                    if time > self.dict_count_group_windows[day][lesson[0]]:
                        self.count_group_error_window += (time - self.dict_count_group_windows[day][lesson[0]] - 1) \
                                                         * WINDOWS_GROUP
                        self.dict_count_group_windows[day][lesson[0]] = time
                else:
                    self.dict_count_group_windows[day][lesson[0]] = time
            else:
                self.dict_count_group_windows[day] = {lesson[0]: time}

    def count_group_no_single(self, lesson: tuple, timeline: int):
        """
        Groups fitness function for check of single timeline - single Group
        except discipline with pair (single timeline - two groups)
        TODO: check pair disciplines!!!
        :param lesson: tuple
        :param timeline: int
        :return: None
        """
        if lesson:
            if timeline in self.dict_count_group_nosingle:
                if lesson[0] in self.dict_count_group_nosingle[timeline]:
                    self.dict_count_group_nosingle[timeline][lesson[0]] += 1
                    if lesson[1] not in self.settings.DISCIPLINES_LIST_WITH_PAIR or \
                            lesson[1] in self.settings.DISCIPLINES_LIST_WITH_PAIR and \
                            self.dict_count_group_nosingle[timeline][lesson[0]] > 2:
                        self.count_group_error_nosingle += NO_SINGLE_GROUP
                    if lesson[1] in self.settings.DISCIPLINES_LIST_WITH_PAIR and \
                            self.dict_count_group_nosingle[timeline][lesson[0]] == 2 and \
                            self.dict_count_disc_name[timeline // AMOUNT_TIMELINES_IN_DAY][lesson[0]] in \
                            self.settings.DISCIPLINE_DICT_WITH_LIST_PAIR:
                        self.count_group_error_nosingle -= NO_SINGLE_GROUP
                else:
                    self.dict_count_group_nosingle[timeline][lesson[0]] = 1
                    if lesson[1] in self.settings.DISCIPLINES_LIST_WITH_PAIR:
                        self.count_group_error_nosingle += NO_SINGLE_GROUP
            else:
                self.dict_count_group_nosingle[timeline] = {lesson[0]: 1}

    def count_group_first_lesson(self, lesson: tuple, timeline: int):
        """
         Groups fitness function for check of start and end lessons in each day for each group
        :param lesson: tuple
        :param timeline: int
        :return: None
        """
        if lesson:
            if lesson[4] > timeline or timeline > lesson[4] + MAX_LESSONS_IN_DAY[lesson[0][0]]:
                self.count_group_error_first_lesson += FIRST_LESSON_GROUP

    def count_audience_spec(self, lesson: tuple, timeline: int, audience: tuple):
        """
        Check audience specialization (disciplines)
        :param audience: tuple
        :param lesson: tuple
        :param timeline: int
        :return: None
        """
        pass

    def count_audience_hard_link(self, lesson: tuple, timeline: int, audience: tuple):
        """
        Check audience hard link (disciplines and groups)
        TODO: make hard link for group and disciplines with audience (settings)
        :param audience: tuple
        :param lesson: tuple
        :param timeline: int
        :return: None
        """
        pass

    def count_disc_name(self, lesson: tuple, timeline: int):
        """
        Check pair some close disciplines with equal names
        :param lesson: tuple
        :param timeline: int
        :return: None
        """
        time = timeline % AMOUNT_TIMELINES_IN_DAY
        day = timeline // AMOUNT_TIMELINES_IN_DAY
        if lesson:
            if day not in self.dict_count_disc_name:
                self.dict_count_disc_name[day] = {}
            if time == lesson[4] or lesson[0] not in self.dict_count_disc_name[day]:
                self.dict_count_disc_name[day][lesson[0]] = lesson[1]
            else:
                if self.dict_count_disc_name[day][lesson[0]] == lesson[1]:
                    self.count_disc_error_name += DISCIPLINES_NAME
                else:
                    self.dict_count_disc_name[day][lesson[0]] = lesson[1]

    def count_disc_type(self, lesson: tuple, timeline: int):
        """
        Check pair some close disciplines with equal types
        :param lesson: tuple
        :param timeline: int
        :return: None
        """
        time = timeline % AMOUNT_TIMELINES_IN_DAY
        day = timeline // AMOUNT_TIMELINES_IN_DAY
        if lesson:
            if day not in self.dict_count_disc_type:
                self.dict_count_disc_type[day] = {}
            if time == lesson[4] or lesson[0] not in self.dict_count_disc_type[day]:
                if lesson[1] in TYPE_DISCIPLINES:
                    self.dict_count_disc_type[day][lesson[0]] = TYPE_DISCIPLINES[lesson[1]]
                else:
                    self.dict_count_disc_type[day][lesson[0]] = None
            else:
                if lesson[1] in TYPE_DISCIPLINES and \
                        self.dict_count_disc_type[day][lesson[0]] == TYPE_DISCIPLINES[lesson[1]]:
                    self.count_disc_error_type += DISCIPLINES_TYPE
                else:
                    if lesson[1] in TYPE_DISCIPLINES:
                        self.dict_count_disc_type[day][lesson[0]] = TYPE_DISCIPLINES[lesson[1]]
                    else:
                        self.dict_count_disc_type[day][lesson[0]] = None

    def make_dict_disc_weight_day(self, lesson: tuple, timeline: int):
        """
        Make dict for check for each groups discipline's weight in each day
        :param lesson: tuple
        :param timeline: int
        :return: None
        """
        day = timeline // AMOUNT_TIMELINES_IN_DAY
        if lesson:
            if day not in self.dict_count_disc_weight_day:
                self.dict_count_disc_weight_day[day] = {}
            if lesson[0] not in self.dict_count_disc_weight_day[day]:
                if lesson[0][0] in WEIGHT_DISCIPLINES and lesson[1] in WEIGHT_DISCIPLINES[lesson[0][0]]:
                    self.dict_count_disc_weight_day[day][lesson[0]] = [WEIGHT_DISCIPLINES[lesson[0][0]][lesson[1]]]
                else:
                    self.dict_count_disc_weight_day[day][lesson[0]] = [1]
            else:
                if lesson[0][0] in WEIGHT_DISCIPLINES and lesson[1] in WEIGHT_DISCIPLINES[lesson[0][0]]:
                    self.dict_count_disc_weight_day[day][lesson[0]].append(WEIGHT_DISCIPLINES[lesson[0][0]][lesson[1]])
                else:
                    self.dict_count_disc_weight_day[day][lesson[0]].append(1)

    def count_disc_weight_day(self):
        """
        Check for each groups discipline's weight in each day
        :return: None
        """
        for day, dict_group in self.dict_count_disc_weight_day.items():
            for group, list_weight in dict_group.items():
                length = len(list_weight)
                if group not in self.dict_count_disc_weight_week:
                    self.dict_count_disc_weight_week[group] = [sum(list_weight)]
                else:
                    self.dict_count_disc_weight_week[group].append(sum(list_weight))
                if length == 4:
                    if list_weight[0] > list_weight[1]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[0] > list_weight[2]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[3] > list_weight[1]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[3] > list_weight[2]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                if length == 5:
                    if list_weight[0] > list_weight[1]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[0] > list_weight[2]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[0] > list_weight[3]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[4] > list_weight[1]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[4] > list_weight[2]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[4] > list_weight[3]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                if length == 6:
                    if list_weight[0] > list_weight[1]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[0] > list_weight[2]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[0] > list_weight[3]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[0] > list_weight[4]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[5] > list_weight[1]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[5] > list_weight[2]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[5] > list_weight[3]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[5] > list_weight[4]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                if length == 7:
                    if list_weight[0] > list_weight[1]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[0] > list_weight[2]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[0] > list_weight[3]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[0] > list_weight[4]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[5] > list_weight[1]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[5] > list_weight[2]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[5] > list_weight[3]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[5] > list_weight[4]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[6] > list_weight[1]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[6] > list_weight[2]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[6] > list_weight[3]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY
                    if list_weight[6] > list_weight[4]:
                        self.count_disc_error_weight_day += DISCIPLINES_WEIGHT_DAY

    def count_disc_weight_week(self):
        """
        Check for each groups discipline's weight in whole week
        :return: None
        """
        for group, list_weight in self.dict_count_disc_weight_week.items():
            length = len(list_weight)
            if length == 5:
                if list_weight[0] > list_weight[1]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
                if list_weight[0] > list_weight[2]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
                if list_weight[0] > list_weight[3]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
                if list_weight[4] > list_weight[1]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
                if list_weight[4] > list_weight[2]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
                if list_weight[4] > list_weight[3]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
            if length == 6:
                if list_weight[0] > list_weight[1]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
                if list_weight[0] > list_weight[2]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
                if list_weight[0] > list_weight[3]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
                if list_weight[0] > list_weight[4]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
                if list_weight[5] > list_weight[1]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
                if list_weight[5] > list_weight[2]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
                if list_weight[5] > list_weight[3]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK
                if list_weight[5] > list_weight[4]:
                    self.count_disc_error_weight_week += DISCIPLINES_WEIGHT_WEEK

    def main_loop(self):
        """
        main loop for each lesson in school schedule

        :return: None
        """
        for timeline in self.individ.keys():
            for auditory, lesson in self.individ[timeline].items():
                self.count_pedago_no_single(lesson, timeline)
                self.count_pedago_windows(lesson, timeline)
                self.count_group_no_single(lesson, timeline)
                self.count_group_first_lesson(lesson, timeline % AMOUNT_TIMELINES_IN_DAY)
                self.count_group_windows(lesson, timeline)
                self.count_disc_name(lesson, timeline)
                self.count_disc_type(lesson, timeline)
                self.count_audience_spec(lesson, timeline, auditory)
                self.make_dict_disc_weight_day(lesson, timeline)
        self.count_disc_weight_day()
        self.count_disc_weight_week()
