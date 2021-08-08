from timetable_Genetic_Algorithm.utils.GeneratorLessons import GeneratorLessons
from timetable_Genetic_Algorithm.utils.RandomizerGenerationExcluded import RandomizerGenerationIncluded
from timetable_Genetic_Algorithm.utils.algorithm_settings import AlgorithmSettings


def getTimeLineSequence(table_settings: AlgorithmSettings) -> list:
    sequence = [1, 2, 3, 0, 4, 5] if table_settings.bool_SCHOOL_STUDY_SATURDAY else [1, 2, 3, 0, 4]
    timeline_list = [i * table_settings.AMOUNT_TIMELINES_IN_DAY + lesson
                     for lesson in range(table_settings.AMOUNT_TIMELINES_IN_DAY)
                     for i in sequence]
    return timeline_list


def generateIndivid(table_settings: AlgorithmSettings):
    main_tuple = GeneratorLessons.gen_overall_pool(table_settings)
    audience_tuple = table_settings.getAudienceForGeneration()

    if table_settings.OTHER_DATA.get("whole_time") != len(main_tuple):
        raise ValueError("cheto ne cxodutcya brat")

    print(audience_tuple)
    pop = {}
    cur = RandomizerGenerationIncluded(table_settings.OTHER_DATA.get("whole_time"), len(audience_tuple))
    for timeline in getTimeLineSequence(table_settings):
        delll = []
        tmp = {}
        for audience in cur.getShuffledAudiences():
            if cur.included_list_main_tuple.__len__() == 0:
                break
            trust_list = cur.getTrueListTimelineSearch(main_tuple, timeline, table_settings.AMOUNT_TIMELINES_IN_DAY)
            delll = trust_list
            """
            if main -> audience -> 1 if 0 ->
            includetrust
            elif auidinect -> 1 if 1 -> main_tuple[index][1] in 
            """
            tmp[audience_tuple[audience]] = cur.getTupleIncludeWithTrust(trust_list, main_tuple)
        pop[timeline] = tmp
        if cur.included_list_main_tuple.__len__() == 0:
            break
        cur.dropIncludedAudienceTuple()
        # cur.dropIncludedMainTuple()
        # print(timeline % 14)
        # print(delll)
    print(*[(key, i) for key, i in pop.items()], sep='\n')
    print(cur.included_list_main_tuple)

    return pop
