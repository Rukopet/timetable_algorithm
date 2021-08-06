import pandas as pd

from timetable_Genetic_Algorithm.utils.constants import RUSSIAN_ALPHABET
from timetable_Genetic_Algorithm.utils.custom_settings import DataFromFront


class AlgorithmSettings:
    """ settings for whole project """
    DEBUG = 0

    GROUPS_RANGE = {"min": 1, "max": 11}

    # dict with min and max num of groups
    GROUPS_LIST = []

    # [["num", "letter"]]
    PEDAGOGS_LIST = []

    # list of all disciplines in school
    DISCIPLINES_LIST = []

    # list of disciplines in school with some pairs
    DISCIPLINES_LIST_WITH_PAIR = []

    # sum all working hours for all groups
    WHOLE_TIME = 0

    # whole pedagogs
    main_data = {}

    # for validate data
    __pedagogs_load = {}

    def __init__(self, data_front: DataFromFront):
        self._validationSetMainData(data_front)

    def _validationSetMainData(self, data_front: DataFromFront):
        try:
            if list(data_front.__dict__.values()).count(None) != 0:
                err_msg = ""
                for key, value in self.__dict__.items():
                    if value is None:
                        err_msg += key + " "
                raise ValueError("Need set all JSON values before convert: " + err_msg)

            # take min max
            self.GROUPS_RANGE["min"] = data_front.groupsJSON.valueDF['number'].dropna().min()
            self.GROUPS_RANGE["max"] = data_front.groupsJSON.valueDF['number'].dropna().max()

            # call list generators for all groups from DataFrame
            self.GROUPS_LIST = AlgorithmSettings.__gen_group_list_from_df(data_front.groupsJSON.valueDF)

            # call list generators for all pedagogs from DataFrame
            self.PEDAGOGS_LIST = AlgorithmSettings.__gen_pedagogs_list_from_df(data_front.pedagogsJSON.valueDF)

            # call for all subjects
            self.DISCIPLINES_LIST = AlgorithmSettings.__gen_all_disciplines(data_front.disciplinesJSON.valueDF)
            self.DISCIPLINES_LIST_WITH_PAIR = AlgorithmSettings.__gen_disciplines_with_pairs(
                data_front.disciplinesJSON.valueDF)

            # call generate main data struct
            self.__gen_main_data_and_validate(data_front)
        except Exception as e:
            raise e

    @staticmethod
    def __gen_group_list_from_df(df: pd.DataFrame) -> list:
        return [[row["number"], RUSSIAN_ALPHABET[count]]
                for index, row in df.iterrows()
                for count in range(row["count"])]

    @staticmethod
    def __gen_pedagogs_list_from_df(df: pd.DataFrame) -> list:
        return df["ped_name"].unique()

    @staticmethod
    def __gen_all_disciplines(df: pd.DataFrame):
        return df["discipline"].unique()

    @staticmethod
    def __gen_disciplines_with_pairs(df: pd.DataFrame):
        return df.dropna()["discipline"].unique()

    @staticmethod
    def __get_disc_group_fill_data(main_data: dict, teacher: str, discipline: str, groups: list):
        try:
            for group in groups:
                main_data[tuple(group.values())] = main_data.get(tuple(group.values()), {})
                main_data[tuple(group.values())][discipline] = {
                    "pedagog": teacher,
                    "weight": None,
                    "load": None,
                    "type_discipline": None
                }
        except Exception as e:
            raise e



    @staticmethod
    def __fill_main_data_load_for_group(main_data: dict, keys: tuple, discipline: str,
                                        load: int, pedagogs_load: dict, sum_time: int):
        if discipline in []:
            return
        group = main_data.get(keys)
        if group is None:
            raise ValueError(f"Uncreated groups in main data")
        group = group.get(discipline)
        if group is None:
            raise ValueError(f"Wrong discipline in loadplan - {discipline} "
                             f"not implemented in pedagogs_model")
        main_data[keys][discipline]["load"] = load
        ped_name = main_data.get(keys).get(discipline, {}).get("pedagog")
        if ped_name is None:
            raise ValueError(f"Bad teacher values in main_data, need check pedagogs table")
        sum_time += load
        pedagogs_load[ped_name] = pedagogs_load.get(ped_name, 0) + load

    def __gen_main_data_and_validate(self, data_front: DataFromFront):
        try:
            ped_table = data_front.pedagogsJSON.valueDF
            for teacher in self.PEDAGOGS_LIST:
                teacher_df = ped_table[ped_table["ped_name"] == teacher]

                """fast alternative to iterrows() just list generator"""
                [AlgorithmSettings.__get_disc_group_fill_data(self.main_data, teacher, row[0], row[1])
                 for row in zip(teacher_df['discipline'], teacher_df['groups'])]

            load_table = data_front.loadPlanJSON.valueDF
            for key, value in self.main_data.items():
                groupDF = load_table[(load_table["num"] == key[0]) & (load_table["letter"] == key[1])]
                if groupDF.dropna().empty:
                    raise ValueError(f'Don`t have {str(key[0], key[1])} in loadplans table')

                """fast alternative to iterrows() just list generator"""
                [AlgorithmSettings.__fill_main_data_load_for_group(self.main_data, key, row[0], row[1],
                                                                   self.__pedagogs_load, self.WHOLE_TIME)
                 for row in zip(groupDF['discipline'], groupDF['load'])]
            print(self.main_data)
        except Exception as e:
            raise e
