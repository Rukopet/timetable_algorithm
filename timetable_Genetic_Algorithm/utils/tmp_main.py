import json
import pandas as pd

from timetable_Genetic_Algorithm.utils import AlgorithmSettings
from timetable_Genetic_Algorithm.utils import DataFromFront


def main():
    wow = DataFromFront()
    pd.set_option('display.max_columns', None)
    with open("../data_for_test/disciplines_model.json") as disciplines_json:
        wow.setDisciplinesJSON(json.load(disciplines_json))
    with open("../data_for_test/group_model.json") as groups_json:
        wow.setGroupsJSON(json.load(groups_json))
        # print(wow.groupsJSON.valueDF)
    with open("../data_for_test/load_plan.json") as load_plan_json:
        wow.setLoadPlanJSON(json.load(load_plan_json))
    with open("../data_for_test/pedagogs_model.json") as pedagogs_json:
        wow.setPedagogsJSON(json.load(pedagogs_json))
        # print(wow.pedagogsJSON.valueDF)
    with open("../data_for_test/auditories.json") as auditories_json:
        wow.setAudiencesJSON(json.load(auditories_json))
        # print(wow.audiencesJSON.valueDF)

    table_settings = AlgorithmSettings(wow)

    print(table_settings.GROUPS_RANGE,
          table_settings.main_data,
          table_settings.PEDAGOGS_LIST,
          table_settings.DISCIPLINES_LIST,
          table_settings.GROUPS_LIST, sep="\n")


if __name__ == "__main__":
    main()
