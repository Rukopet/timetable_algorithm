from random import shuffle
from typing import List

from timetable_genetic_algorithm.utils.GeneratorLessons import GeneratorLessons
from timetable_genetic_algorithm.utils.RandomizerGenerationExcluded import RandomizerGenerationIncluded
from timetable_genetic_algorithm.utils.algorithm_settings import AlgorithmSettings


def get_time_line_sequence(table_settings: AlgorithmSettings) -> list:
    sequence = [1, 2, 3, 0, 4, 5] if table_settings.bool_SCHOOL_STUDY_SATURDAY else [1, 2, 3, 0, 4]
    timeline_list = [i * table_settings.AMOUNT_TIMELINES_IN_DAY + lesson
                     for lesson in range(table_settings.AMOUNT_TIMELINES_IN_DAY)
                     for i in sequence]
    return timeline_list


def get_cur_trust_list(cur, main_tuple, timeline, table_settings, audience_tuple, audience) -> List[int]:
    trust_list = cur.get_true_list_time_line_search(main_tuple, timeline,
                                                    table_settings.AMOUNT_TIMELINES_IN_DAY)

    """
    if main -> audience -> 1 if 0 ->
    includetrust
    elif auidinect -> 1 if 1 -> main_tuple[index][1] pizdushanya fucnya True -> 
    elif auidinect -> 1 if 2 -> found num letter -> checkin maintuple True | false
    elif auidinect -> 1 if 3 -> 
    """
    if audience_tuple[audience][1] == 0:
        trust_list = cur.get_true_list_no_spec(trust_list, main_tuple, table_settings)
    elif audience_tuple[audience][1] == 1:
        trust_list = cur.get_true_list_audience_disc(trust_list, main_tuple,
                                                     audience_tuple[audience][0],
                                                     table_settings)
    #     TODO check all trust list on empty value
    elif audience_tuple[audience][1] == 2:
        trust_list = cur.get_true_list_audience_group(trust_list, main_tuple,
                                                      audience_tuple[audience][0],
                                                      table_settings)

    elif audience_tuple[audience][1] == 3:
        trust_list = cur.get_true_list_audience_mix(trust_list, main_tuple,
                                                    audience_tuple[audience][0],
                                                    table_settings)
    return trust_list


def check_pair_discipline(shuffled_audiences, audience, tmp, table_settings, audience_tuple, cur, main_tuple, timeline)\
        -> None:
    i = shuffled_audiences.index(audience)
    discipline = tmp[audience_tuple[audience]][1]
    group = tmp[audience_tuple[audience]][0]
    flag = 0
    if i < len(shuffled_audiences) - 1:
        for id_aud in shuffled_audiences[i + 1:]:
            shuffle(table_settings.DISCIPLINE_DICT_WITH_LIST_PAIR[discipline])
            for pair_disc in table_settings.DISCIPLINE_DICT_WITH_LIST_PAIR[discipline]:
                if pair_disc not in table_settings.DISCIPLINES_AUDIENCE_LINK and \
                        pair_disc not in table_settings.DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK or \
                        pair_disc in table_settings.DISCIPLINES_AUDIENCE_LINK and \
                        audience_tuple[id_aud][0] in table_settings.DISCIPLINES_AUDIENCE_LINK[pair_disc] or \
                        pair_disc in table_settings.DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK and \
                        audience_tuple[id_aud][0] == \
                        table_settings.DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK[pair_disc]:

                    trust_list = cur.get_true_list_time_line_search_pair(main_tuple,
                                                                         timeline,
                                                                         table_settings.AMOUNT_TIMELINES_IN_DAY,
                                                                         group, pair_disc)
                    if audience_tuple[id_aud][1] == 0:
                        trust_list = cur.get_true_list_no_spec(trust_list, main_tuple, table_settings)
                    elif audience_tuple[id_aud][1] == 1:
                        trust_list = cur.get_true_list_audience_disc(trust_list, main_tuple,
                                                                     audience_tuple[id_aud][0],
                                                                     table_settings)
                    #     TODO check all trust list on empty value
                    elif audience_tuple[id_aud][1] == 2:
                        trust_list = cur.get_true_list_audience_group(trust_list, main_tuple,
                                                                      audience_tuple[id_aud][0],
                                                                      table_settings)

                    elif audience_tuple[id_aud][1] == 3:
                        trust_list = cur.get_true_list_audience_mix(trust_list, main_tuple,
                                                                    audience_tuple[id_aud][0],
                                                                    table_settings)
                    tmp[audience_tuple[id_aud]] = cur.get_tuple_include_with_pair(trust_list, main_tuple)
                    shuffled_audiences.remove(id_aud)
                    flag = 1
                    break
            if flag == 1:
                break


def generate_individ(table_settings: AlgorithmSettings):
    main_tuple = GeneratorLessons.gen_overall_pool(table_settings)
    audience_tuple = table_settings.get_audience_for_generation()

    if table_settings.OTHER_DATA.get("whole_time") != len(main_tuple):
        raise ValueError("cheto ne cxodutcya brat")

    pop = {}
    cur = RandomizerGenerationIncluded(table_settings.OTHER_DATA.get("whole_time"), len(audience_tuple),
                                       table_settings.GROUPS_LIST)

    table_settings.DEBUG = 1

    for timeline in get_time_line_sequence(table_settings):
        tmp = {}
        shuffled_audiences = cur.get_shuffled_audiences()
        for audience in shuffled_audiences:
            if cur.included_list_main_tuple.__len__() == 0:
                break
            trust_list = get_cur_trust_list(cur, main_tuple, timeline, table_settings, audience_tuple, audience)
            tmp[audience_tuple[audience]] = cur.get_tuple_include_with_trust(trust_list, main_tuple)
            if tmp[audience_tuple[audience]] is not None \
                    and tmp[audience_tuple[audience]][1] in table_settings.DISCIPLINES_LIST_WITH_PAIR:
                check_pair_discipline(shuffled_audiences, audience, tmp, table_settings, audience_tuple, cur,
                                      main_tuple, timeline)
        pop[timeline] = tmp
        cur.drop_included_audience_tuple()
        cur.drop_bool_copy_matrix()
    return pop
