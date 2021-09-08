import logging
from copy import copy
from random import choice, shuffle
from typing import List, Tuple, Any

try:
    from typing import Final
except ImportError:
    from typing_extensions import Final

from timetable_genetic_algorithm.utils.algorithm_settings import AlgorithmSettings
from timetable_genetic_algorithm.utils.constants import MAX_LESSONS_IN_DAY
from timetable_genetic_algorithm.utils.our_typing import Groups, Audiences, Group


def checking_discipline(dict_list: list, sought: str) -> bool:
    for val in dict_list:
        if sought in val.values():
            return True
    return False


def checking_group(dict_list: list, sought: tuple) -> bool:
    for val in dict_list:
        if sought == tuple(val.values()):
            return True
    return False


class RandomizerGenerationIncluded:
    """ Simple randomizer for generate populations """

    def __init__(self, len_main_tuple: int, len_audience_tuple: int, groups_list: Groups) -> None:
        """

        :param len_main_tuple:
        :param len_audience_tuple:
        :param groups_list: list groups List

        :var self.bool_group_matrix: asd
        """

        self.groups_list: Final = groups_list
        self.included_list_main_tuple = list(range(0, len_main_tuple))
        self.included_list_audiences_tuple = list(range(0, len_audience_tuple))
        self.len_main_tuple = len_main_tuple
        self.len_audience_tuple = len_audience_tuple

        """ True/False matrix for groups for rejecting repeat """
        len_groups_list = self.groups_list.__len__()
        self.__copy_bool_group_matrix: Final = [False for _ in range(len_groups_list)]
        self.bool_group_matrix = copy(self.__copy_bool_group_matrix)
        self.len_groups_list = len_groups_list

    def get_num_included_random_for_main_tuple(self) -> int:
        ret = choice(self.included_list_main_tuple)
        self.included_list_main_tuple.remove(ret)
        return ret

    def get_num_included_random_for_audience_tuple(self) -> int:
        ret = choice(self.included_list_audiences_tuple)
        self.included_list_audiences_tuple.remove(ret)
        return ret

    def get_tuple_included_random_for_main_tuple(self, main_tuple: list) -> tuple:
        """
        not use now

        :param main_tuple:
        :return:
        """
        ret = choice(self.included_list_main_tuple)
        self.included_list_main_tuple.remove(ret)
        self.__add_group_to_have_lesson_already(main_tuple[ret][0])
        return main_tuple[ret]

    def get_tuple_included_random_for_audience_tuple(self, audience_tuple: Audiences) -> tuple:
        ret = choice(self.included_list_audiences_tuple)
        self.included_list_audiences_tuple.remove(ret)
        return audience_tuple[ret]

    def __check_is_group_have_lesson_already(self, group: Group) -> bool:
        """
        checks if the group is included in this list, who already have lesson

        :param group: Tuple[int, str], example: (1, "А")
        :return: True/False have this group lesson already in current timeline
        """

        index = self.groups_list.index(group)
        if index is None:
            logging.debug(f'group={group}')
            raise ValueError
        p = self.bool_group_matrix[index]
        return self.bool_group_matrix[index]

    def __add_group_to_have_lesson_already(self, group: Group) -> None:
        """
        adds the group to the list, who already have lesson

        :param group: Tuple[int, str], example: (1, "А")
        :return: nothing, None
        """

        index = self.groups_list.index(group)
        if index is None:
            logging.debug(f'group={group}')
            raise ValueError
        self.bool_group_matrix[index] = True
        p = 1

    def get_true_list_time_line_search(self,
                                       main_tuple: list,
                                       timeline: int,
                                       amount_timelines_in_day: int) -> List[int]:
        """
            runs over the list and forms a sheet that satisfies the conditions

            :var main_tuple[index][0]: is some group(1, "А"), in main_tuple

            :param main_tuple: tuple with sig: write signature
            :param timeline: int num, what is the account
            :param amount_timelines_in_day: need MOD big timeline on AMOUNT_TIMELINES_IN_DAY in settings+generations.py -> 53 % 14
            :return: list with int`s, for get needed tuples sig: List[int]
        """

        timemode = timeline % amount_timelines_in_day
        return [
            index for index in self.included_list_main_tuple
            if MAX_LESSONS_IN_DAY.get(main_tuple[index][0][0], 7) > timemode - main_tuple[index][4] >= 0
            and timeline < main_tuple[index][3] * amount_timelines_in_day
            and not self.__check_is_group_have_lesson_already(main_tuple[index][0])

        ]

    def get_true_list_time_line_search_pair(self,
                                            main_tuple: list,
                                            timeline: int,
                                            amount_timelines_in_day: int,
                                            group: tuple,
                                            pair_disc: str) -> List[int]:
        """
            runs over the list and forms a sheet that satisfies the conditions

            :param group:
            :var main_tuple[index][0]: is some group(1, "А"), in main_tuple

            :param main_tuple: tuple with sig: write signature
            :param timeline: int num, what is the account
            :param amount_timelines_in_day: need MOD big timeline on AMOUNT_TIMELINES_IN_DAY in settings+generations.py -> 53 % 14
            :return: list with int`s, for get needed tuples sig: List[int]
        """

        timemode = timeline % amount_timelines_in_day
        return [
            index for index in self.included_list_main_tuple
            if MAX_LESSONS_IN_DAY.get(main_tuple[index][0][0], 7) > timemode - main_tuple[index][4] >= 0
            and timeline < main_tuple[index][3] * amount_timelines_in_day
            and main_tuple[index][0] == group and main_tuple[index][1] == pair_disc

        ]

    def get_true_list_no_spec(self, trust_list: List[int], main_tuple: tuple,
                              table_settings: AlgorithmSettings) -> list:
        return [
            index for index in trust_list
            if main_tuple[index][0] not in table_settings.GROUPS_AUDIENCE_LINK
            and main_tuple[index][1] not in table_settings.DISCIPLINES_AUDIENCE_LINK
            and main_tuple[index][1] not in table_settings.DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK
        ]

    def get_true_list_audience_disc(self, trust_list: List[int], main_tuple: tuple, audience: int,
                                    table_settings: AlgorithmSettings) -> list:
        return [
            index for index in trust_list
            if checking_discipline(table_settings.AUDIENCE_PARAMS[audience], main_tuple[index][1])
        ]

    def get_true_list_audience_group(self, trust_list: List[int], main_tuple: tuple, audience: int,
                                     table_settings: AlgorithmSettings) -> list:
        return [
            index for index in trust_list
            if checking_group(table_settings.AUDIENCE_PARAMS[audience], main_tuple[index][0])
        ]

    def get_true_list_audience_mix(self, trust_list: List[int], main_tuple: tuple, audience: int,
                                   table_settings: AlgorithmSettings) -> list:
        return [
            index for index in trust_list
            if checking_group(table_settings.AUDIENCE_PARAMS[audience], main_tuple[index][0])
            and checking_discipline(table_settings.AUDIENCE_PARAMS[audience], main_tuple[index][1])
        ]

    def get_tuple_include_with_trust(self, trust_list: List[int], main_tuple: list) -> tuple or None:
        if trust_list.__len__() == 0:
            return None
        ret = choice(trust_list)
        self.included_list_main_tuple.remove(ret)
        self.__add_group_to_have_lesson_already(main_tuple[ret][0])
        return main_tuple[ret]

    def get_tuple_include_with_pair(self, trust_list: List[int], main_tuple: list) -> tuple or None:
        if trust_list.__len__() == 0:
            return None
        ret = choice(trust_list)
        self.included_list_main_tuple.remove(ret)
        # self.__add_group_to_have_lesson_already(main_tuple[ret][0])
        return main_tuple[ret]

    def drop_included_main_tuple(self) -> None:
        self.included_list_main_tuple = list(range(0, self.len_main_tuple))

    def drop_included_audience_tuple(self) -> None:
        self.included_list_audiences_tuple = list(range(0, self.len_audience_tuple))

    def drop_bool_copy_matrix(self) -> None:
        """ just refresh bool matrix, use this in every cycle %for in timelines% """

        self.bool_group_matrix = copy(self.__copy_bool_group_matrix)

    def get_shuffled_audiences(self) -> List[int]:
        """

        :return: list shuffled int - indexes of audiences
        """
        shuffle(self.included_list_audiences_tuple)
        return self.included_list_audiences_tuple
