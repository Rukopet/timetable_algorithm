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
    main_loop(table_settings, population, audience_tuple)


if __name__ == "__main__":
    main()
