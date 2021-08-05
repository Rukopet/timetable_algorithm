import pandas as pd

from .custom_settings import DataFromFront
from .constants import RUSSIAN_ALPHABET


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
        for group in groups:
            main_data[tuple(group.values())] = main_data.get(tuple(group.values()))\
                .append({discipline: {"pedagog": teacher,
                                      "weight": None,
                                      "load": None}}) if main_data.get(tuple(group.values())) is None else []

    def __gen_main_data_and_validate(self, data_front: DataFromFront):
        # sum_work_hours_for_teacher = 0
        # for group in self.GROUPS_LIST:
        ped_table = data_front.pedagogsJSON.valueDF
        for teacher in self.PEDAGOGS_LIST:
            teacher_df = ped_table[ped_table["ped_name"] == teacher]

            # fast alternative to iterrows() just list generator
            [AlgorithmSettings.__get_disc_group_fill_data(self.main_data, teacher, row[0], row[1])
             for row in zip(teacher_df['discipline'], teacher_df['groups'])]

        print(self.main_data)
