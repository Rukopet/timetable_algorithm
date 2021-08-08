from random import choice, shuffle

from timetable_Genetic_Algorithm.utils.algorithm_settings import AlgorithmSettings
from timetable_Genetic_Algorithm.utils.constants import MAX_LESSONS_IN_DAY


def checkin_discipline(dict_list: list, sought: str) -> bool:
    for val in dict_list:
        if sought in val.values():
            return True
    return False


def checkin_group(dict_list: list, sought: tuple) -> bool:
    for val in dict_list:
        if sought == tuple(val.values()):
            return True
    return False


class RandomizerGenerationIncluded:
    """ Simple randomizer for generate populations """

    def __init__(self, len_main_tuple: int, len_audience_tuple: int):
        self.included_list_main_tuple = list(range(0, len_main_tuple))
        self.included_list_audiences_tuple = list(range(0, len_audience_tuple))
        self.len_main_tuple = len_main_tuple
        self.len_audience_tuple = len_audience_tuple

    def getNumIncludedRandomForMainTuple(self) -> int:
        ret = choice(self.included_list_main_tuple)
        self.included_list_main_tuple.remove(ret)
        return ret

    def getNumIncludedRandomForAudienceTuple(self) -> int:
        ret = choice(self.included_list_audiences_tuple)
        self.included_list_audiences_tuple.remove(ret)
        return ret

    def getTupleIncludedRandomForMainTuple(self, main_tuple: list) -> tuple:
        ret = choice(self.included_list_main_tuple)
        self.included_list_main_tuple.remove(ret)
        return main_tuple[ret]

    def getTupleIncludedRandomForAudienceTuple(self, audience_tuple: list) -> tuple:
        ret = choice(self.included_list_audiences_tuple)
        self.included_list_audiences_tuple.remove(ret)
        return audience_tuple[ret]

    def getTrueListTimelineSearch(self, main_tuple: list, timeline: int, amount_timelines_in_day: int) -> list:
        """ need MOD big timeline on AMOUNT_TIMELINES_IN_DAY in settings+generations.py -> 53 % 14 """
        timemode = timeline % amount_timelines_in_day
        return [
            index for index in self.included_list_main_tuple
            if MAX_LESSONS_IN_DAY.get(main_tuple[index][0][0], 7) > timemode - main_tuple[index][4] >= 0
               and timeline <= main_tuple[index][3] * amount_timelines_in_day
        ]

    @staticmethod
    def getTrueListAudienceDisc(trust_list: list, main_tuple: tuple, audience: int,
                                table_settings: AlgorithmSettings) -> list:
        return [
            index for index in trust_list
            if checkin_discipline(table_settings.AUDIENCE_PARAMS[audience], main_tuple[index][1])
        ]

    @staticmethod
    def getTrueListAudienceGroup(trust_list: list, main_tuple: tuple, audience: int,
                                 table_settings: AlgorithmSettings) -> list:
        return [
            index for index in trust_list
            if checkin_group(table_settings.AUDIENCE_PARAMS[audience], main_tuple[index][0])
        ]

    @staticmethod
    def getTrueListAudienceMix(trust_list: list, main_tuple: tuple, audience: int,
                                 table_settings: AlgorithmSettings) -> list:
        return [
            index for index in trust_list
            if checkin_group(table_settings.AUDIENCE_PARAMS[audience], main_tuple[index][0])
            and checkin_discipline(table_settings.AUDIENCE_PARAMS[audience], main_tuple[index][1])
        ]

    def getTupleIncludeWithTrust(self, trust_list: list, main_tuple: list) -> tuple or None:
        if trust_list.__len__() == 0:
            return None
        ret = choice(trust_list)
        self.included_list_main_tuple.remove(ret)
        return main_tuple[ret]

    def dropIncludedMainTuple(self) -> None:
        self.included_list_main_tuple = list(range(0, self.len_main_tuple))

    def dropIncludedAudienceTuple(self) -> None:
        self.included_list_audiences_tuple = list(range(0, self.len_audience_tuple))

    def getShuffledAudiences(self) -> list:
        """ random list shuffle """
        shuffle(self.included_list_audiences_tuple)
        return self.included_list_audiences_tuple
