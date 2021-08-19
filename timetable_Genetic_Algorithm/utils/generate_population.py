from timetable_Genetic_Algorithm.utils.GeneratorLessons import GeneratorLessons
from timetable_Genetic_Algorithm.utils.RandomizerGenerationExcluded import RandomizerGenerationIncluded
from timetable_Genetic_Algorithm.utils.algorithm_settings import AlgorithmSettings


def get_time_line_sequence(table_settings: AlgorithmSettings) -> list:
    sequence = [1, 2, 3, 0, 4, 5] if table_settings.bool_SCHOOL_STUDY_SATURDAY else [1, 2, 3, 0, 4]
    timeline_list = [i * table_settings.AMOUNT_TIMELINES_IN_DAY + lesson
                     for lesson in range(table_settings.AMOUNT_TIMELINES_IN_DAY)
                     for i in sequence]
    return timeline_list


def generate_individ(table_settings: AlgorithmSettings):
    main_tuple = GeneratorLessons.gen_overall_pool(table_settings)
    audience_tuple = table_settings.get_audience_for_generation()

    if table_settings.OTHER_DATA.get("whole_time") != len(main_tuple):
        raise ValueError("cheto ne cxodutcya brat")

    # print(audience_tuple)
    pop = {}
    cur = RandomizerGenerationIncluded(table_settings.OTHER_DATA.get("whole_time"), len(audience_tuple),
                                       table_settings.GROUPS_LIST)

    table_settings.DEBUG = 1

    for timeline in get_time_line_sequence(table_settings):
        tmp = {}
        for audience in cur.get_shuffled_audiences():
            if cur.included_list_main_tuple.__len__() == 0:
                break
            trust_list = cur.get_true_list_time_line_search(main_tuple, timeline,
                                                            table_settings.AMOUNT_TIMELINES_IN_DAY)
            delll = trust_list

            """
            if main -> audience -> 1 if 0 ->
            includetrust
            elif auidinect -> 1 if 1 -> main_tuple[index][1] pizdushanya fucnya True -> 
            elif auidinect -> 1 if 2 -> found num letter -> checkin maintuple True | false
            elif auidinect -> 1 if 3 -> 
            """

            if audience_tuple[audience][1] == 1:
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
            tmp[audience_tuple[audience]] = cur.get_tuple_include_with_trust(trust_list, main_tuple)

        pop[timeline] = tmp
        cur.drop_included_audience_tuple()
        cur.drop_bool_copy_matrix()
    return pop
