from typing import List

from timetable_genetic_algorithm.main_algorithm.main_loop_algorithm import main_loop
from timetable_genetic_algorithm.utils.GeneratorLessons import GeneratorLessons
from timetable_genetic_algorithm.utils.Individ import Individ
from timetable_genetic_algorithm.utils.algorithm_settings import AlgorithmSettings
from timetable_genetic_algorithm.utils.custom_settings import DataFromFront, DataOut
from timetable_genetic_algorithm.utils.generate_population import generate_individ
from timetable_genetic_algorithm.utils.our_typing import Population


def group_sort(individ: dict) -> dict:
    individ_sort = dict(sorted(individ.items()))
    return individ_sort


def generate_population_sorted(table_settings: AlgorithmSettings,
                               main_tuple: List[tuple],
                               audience_tuple: List[tuple]) -> Population:
    return [
        Individ(dict(sorted(generate_individ(table_settings, main_tuple, audience_tuple).items())), table_settings,
                individ_id)
        for individ_id in range(table_settings.TOTAL_POPULATION)
    ]


def main(table_settings: AlgorithmSettings):
    main_tuple = GeneratorLessons.gen_overall_pool(table_settings)
    audience_tuple = table_settings.get_audience_for_generation()
    population = generate_population_sorted(table_settings, main_tuple, audience_tuple)
    return main_loop(table_settings, population, audience_tuple)


def get_data_from_request(request_data: dict) -> DataFromFront:
    from datetime import datetime
    return_data = DataFromFront(request_data)
    return_data.data_out = DataOut(email=request_data["client_mail"],
                                   filename=datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '.xls')
    return_data.set_groups_json(request_data['groups'])
    return_data.set_disciplines_json(request_data['disciplines'])
    return_data.set_audiences_json(request_data['audiences'])
    return_data.set_load_plan_json(request_data['load_plan'])
    return_data.set_pedagogs_json(request_data['pedagogs'])
    return return_data


def server_entry_point(request_data):
    """

    :param request_data:
    :return: Any exception or data out
    """
    data = get_data_from_request(request_data)
    table_settings = AlgorithmSettings(data)
    table_settings.DEBUG = 1
    return main(table_settings), data.data_out.filename


def console_entry_point(source_path: str, out_file: str = 'out_timetable.xls'):
    from timetable_genetic_algorithm.utils import FILENAMES_FOR_DATA

    data = DataFromFront()
    for json_name in FILENAMES_FOR_DATA:
        data.setter_for_json_data(source_path, json_name)
    data.data_out = DataOut(filename=out_file)
    table_setting = AlgorithmSettings(data)
    table_setting.DEBUG = 1
    return main(table_setting)
