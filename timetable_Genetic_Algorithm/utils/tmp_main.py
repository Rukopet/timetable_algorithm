import json
import pandas as pd

from timetable_Genetic_Algorithm.utils.GeneratorLessons import GeneratorLessons
from timetable_Genetic_Algorithm.utils.RandomizerGenerationExcluded import RandomizerGenerationExcluded, \
    RandomizerGenerationIncluded
from timetable_Genetic_Algorithm.utils.algorithm_settings import AlgorithmSettings
from timetable_Genetic_Algorithm.utils.custom_settings import DataFromFront


def main():
    wow = DataFromFront()
    pd.set_option('display.max_columns', None)
    with open("../data_for_test/disciplines_model.json") as disciplines_json:
        wow.setDisciplinesJSON(json.load(disciplines_json))
        wow.disciplinesJSON.valueDF.to_csv("../data_for_test/disciplines.csv")
    with open("../data_for_test/group_model.json") as groups_json:
        wow.setGroupsJSON(json.load(groups_json))
        wow.groupsJSON.valueDF.to_csv("../data_for_test/groups.csv")
    with open("../data_for_test/load_plan.json") as load_plan_json:
        wow.setLoadPlanJSON(json.load(load_plan_json))
        wow.loadPlanJSON.valueDF.to_csv("../data_for_test/loadPlan.csv")
    with open("../data_for_test/pedagogs_model.json") as pedagogs_json:
        wow.setPedagogsJSON(json.load(pedagogs_json))
        wow.pedagogsJSON.valueDF.to_csv("../data_for_test/pedagogs.csv")
    with open("../data_for_test/auditories.json") as auditories_json:
        wow.setAudiencesJSON(json.load(auditories_json))
        wow.audiencesJSON.valueDF.to_csv("../data_for_test/audiences.csv")

    table_settings = AlgorithmSettings(wow)
    print(table_settings.AUDIENCE_LIST)
    main_tuple = GeneratorLessons.gen_overall_pool(table_settings)
    audience_tuple = table_settings.getAudienceForGeneration()
    if table_settings.OTHER_DATA.get("whole_time") != len(main_tuple):
        raise ValueError("cheto ne cxodutcya brat")

    # pop = {
    #     timeline: {
    #         audience:
    #     }
    #     for timeline in range(table_settings.AMOUNT_TIMELINES_IN_DAY * table_settings.MAX_DAYS_FROM_JSON)
    #     for audience in table_settings.AUDIENCE_LIST§
    # }
    pop = {}
    cur = RandomizerGenerationIncluded(table_settings.OTHER_DATA.get("whole_time"), len(audience_tuple), 0)
    for timeline in range(table_settings.AMOUNT_TIMELINES_IN_DAY * table_settings.MAX_DAYS_FROM_JSON):
        delll = []
        tmp = {}
        for audience in cur.getShuffledAudiences():
            if cur.included_list_main_tuple.__len__() == 0:
                break
            trust_list = cur.getTrueListTimelineSearch(main_tuple, timeline, table_settings.AMOUNT_TIMELINES_IN_DAY)
            delll = trust_list
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



if __name__ == "__main__":
    main()
