import json
from typing import List

import pandas as pd

from timetable_genetic_algorithm.main_algorithm.main_loop_algorithm import main_loop
from timetable_genetic_algorithm.utils.DraftFitness import FitnessSettingData
from timetable_genetic_algorithm.utils.GeneratorLessons import GeneratorLessons
from timetable_genetic_algorithm.utils.Individ import Individ
from timetable_genetic_algorithm.utils.algorithm_settings import AlgorithmSettings
from timetable_genetic_algorithm.utils.custom_settings import DataFromFront
from timetable_genetic_algorithm.utils.generate_population import generate_individ
from timetable_genetic_algorithm.utils.our_typing import Population


def get_data_from_front() -> DataFromFront:
    ret = DataFromFront()
    pd.set_option('display.max_columns', None)
    with open("../data_for_test/disciplines_model.json") as disciplines_json:
        ret.set_disciplines_json(json.load(disciplines_json))
        ret.disciplinesJSON.valueDF.to_csv("../data_for_test/disciplines.csv")
    with open("../data_for_test/group_model.json") as groups_json:
        ret.set_groups_json(json.load(groups_json))
        ret.groupsJSON.valueDF.to_csv("../data_for_test/groups.csv")
    with open("../data_for_test/load_plan.json") as load_plan_json:
        ret.set_load_plan_json(json.load(load_plan_json))
        ret.loadPlanJSON.valueDF.to_csv("../data_for_test/loadPlan.csv")
    with open("../data_for_test/pedagogs_model.json") as pedagogs_json:
        ret.set_pedagogs_json(json.load(pedagogs_json))
        ret.pedagogsJSON.valueDF.to_csv("../data_for_test/pedagogs.csv")
    with open("../data_for_test/auditories.json") as auditories_json:
        ret.set_audiences_json(json.load(auditories_json))
        ret.audiencesJSON.valueDF.to_csv("../data_for_test/audiences.csv")
    return ret


def group_sort(individ: dict) -> dict:
    individ_sort = dict(sorted(individ.items()))
    # print(*[(key, i) for key, i in individ_sort.items()], sep='\n')
    # group = {audience: audiencesDF[audiencesDF["number_audience"] == audience]["params"].tolist()[0]
    #            for audience in all_audiences}
    return individ_sort


def generate_population_sorted(table_settings: AlgorithmSettings,
                               main_tuple: List[tuple],
                               audience_tuple: List[tuple]) -> Population:
    return [
        Individ(dict(sorted(generate_individ(table_settings, main_tuple, audience_tuple).items())), \
                table_settings, individ_id)
        for individ_id in range(table_settings.TOTAL_POPULATION)
    ]


def main():
    front_data = get_data_from_front()
    table_settings = AlgorithmSettings(front_data)

    main_tuple = GeneratorLessons.gen_overall_pool(table_settings)
    audience_tuple = table_settings.get_audience_for_generation()

    population = generate_population_sorted(table_settings, main_tuple, audience_tuple)
    # print(population[0].dict_individ)
    main_loop(table_settings, population, audience_tuple)

    # draft = FitnessSettingData(table_settings, individ)
    # draft.main_loop()
    # #print(draft.dict_count_pedago_nosingle)
    # print("Pedagog error (No single):", draft.count_pedag_error_nosingle)
    # #print(draft.dict_count_pedago_windows)
    # print("Pedagog error (windows):", draft.count_pedag_error_window)
    # print(draft.dict_count_group_nosingle)
    # print("Group error (No single):", draft.count_group_error_nosingle)
    # print("Group error (first lesson):", draft.count_group_error_first_lesson)
    # #print(draft.dict_count_group_windows)
    # print("Group error (windows):", draft.count_group_error_window)
    # #print(draft.dict_count_disc_name)
    # print("Disciplines error (name):", draft.count_disc_error_name)
    # #print(draft.dict_count_disc_type)
    # print("Disciplines error (type):", draft.count_disc_error_type)
    # #print(draft.dict_count_disc_weight_day)
    # print("Disciplines error (weight day):", draft.count_disc_error_weight_day)
    # #print(draft.dict_count_disc_weight_week)
    # print("Disciplines error (weight week):", draft.count_disc_error_weight_week)
    # print("Audiences error (specialization):", draft.count_aud_error_spec)
    # print("Audiences error (hard link):", draft.count_aud_error_hard_link)
    # print(table_settings.GROUPS_AUDIENCE_LINK)
    # print(table_settings.DISCIPLINES_AUDIENCE_LINK)
    # print(table_settings.DISCIPLINE_DICT_WITH_LIST_PAIR)
    # print(table_settings.DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK)


if __name__ == "__main__":
    main()
