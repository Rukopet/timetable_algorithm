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
            elif auidinect -> 1 if 1 -> main_tuple[index][1] pizdushanya fucnya True -> 
            
            elif auidinect -> 1 if 2 -> found num letter -> checkin maintuple True | false
            elif auidinect -> 1 if 3 -> 
            """
            if audience_tuple[audience][1] == 0:
                tmp[audience_tuple[audience]] = cur.getTupleIncludeWithTrust(trust_list, main_tuple)
            elif audience_tuple[audience][1] == 1:
                trust_disciplines = RandomizerGenerationIncluded.getTrueListAudienceDisc(trust_list, main_tuple,
                                                                                         audience_tuple[audience][0],
                                                                                         table_settings)
            #     TODO check all trust list on empty value
            elif audience_tuple[audience][1] == 2:
                trust_group = RandomizerGenerationIncluded.getTrueListAudienceGroup(trust_list, main_tuple,
                                                                                    audience_tuple[audience][0],
                                                                                    table_settings)
                # print(trust_group)
                # print(*[main_tuple[i] for i in trust_group])
                # p = 1
            elif audience_tuple[audience][1] == 3:
                trust_mixed = RandomizerGenerationIncluded.getTrueListAudienceMix(trust_list, main_tuple,
                                                                                    audience_tuple[audience][0],
                                                                                    table_settings)
                print(trust_mixed)
                print(*[main_tuple[i] for i in trust_mixed])
                p = 1
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
