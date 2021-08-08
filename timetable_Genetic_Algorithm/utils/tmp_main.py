import json
import pandas as pd

from timetable_Genetic_Algorithm.utils.GeneratorLessons import GeneratorLessons
from timetable_Genetic_Algorithm.utils.RandomizerGenerationExcluded import RandomizerGenerationExcluded, \
    RandomizerGenerationIncluded
from timetable_Genetic_Algorithm.utils.algorithm_settings import AlgorithmSettings
from timetable_Genetic_Algorithm.utils.custom_settings import DataFromFront
from timetable_Genetic_Algorithm.utils.generate_population import generateIndivid


def getDataFromFront() -> DataFromFront:
    ret = DataFromFront()
    pd.set_option('display.max_columns', None)
    with open("../data_for_test/disciplines_model.json") as disciplines_json:
        ret.setDisciplinesJSON(json.load(disciplines_json))
        ret.disciplinesJSON.valueDF.to_csv("../data_for_test/disciplines.csv")
    with open("../data_for_test/group_model.json") as groups_json:
        ret.setGroupsJSON(json.load(groups_json))
        ret.groupsJSON.valueDF.to_csv("../data_for_test/groups.csv")
    with open("../data_for_test/load_plan.json") as load_plan_json:
        ret.setLoadPlanJSON(json.load(load_plan_json))
        ret.loadPlanJSON.valueDF.to_csv("../data_for_test/loadPlan.csv")
    with open("../data_for_test/pedagogs_model.json") as pedagogs_json:
        ret.setPedagogsJSON(json.load(pedagogs_json))
        ret.pedagogsJSON.valueDF.to_csv("../data_for_test/pedagogs.csv")
    with open("../data_for_test/auditories.json") as auditories_json:
        ret.setAudiencesJSON(json.load(auditories_json))
        ret.audiencesJSON.valueDF.to_csv("../data_for_test/audiences.csv")
    return ret


def getTimeLineSequence(table_settings: AlgorithmSettings) -> list:
    sequence = [1, 2, 3, 0, 4, 5] if table_settings.bool_SCHOOL_STUDY_SATURDAY else [1, 2, 3, 0, 4]
    timeline_list = [i * table_settings.AMOUNT_TIMELINES_IN_DAY + lesson
                     for lesson in range(table_settings.AMOUNT_TIMELINES_IN_DAY)
                     for i in sequence]
    return timeline_list


def main():
    front_data = getDataFromFront()

    table_settings = AlgorithmSettings(front_data)
    individ = generateIndivid(table_settings)


if __name__ == "__main__":
    main()
