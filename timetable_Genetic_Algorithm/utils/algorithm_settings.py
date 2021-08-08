import pandas as pd

from timetable_Genetic_Algorithm.utils.constants import RUSSIAN_ALPHABET, TYPE_DISCIPLINES, WEIGHT_DISCIPLINES
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
    """
    keys:
        "whole_time"
    """
    OTHER_DATA = {}

    # whole pedagogs
    main_data = {}

    # for validate data
    __pedagogs_load = {}

    # list auditories
    AUDIENCE_LIST = []

    """
    keys:
        num_audience --> params
    """
    AUDIENCE_PARAMS = {}

    TOTAL_POPULATION = 400

    def __init__(self, data_front: DataFromFront):
        self.data_from_front = data_front
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

            self.AUDIENCE_LIST = AlgorithmSettings.__get_audience_list(data_front.audiencesJSON.valueDF)
            self.AUDIENCE_PARAMS = AlgorithmSettings.__gen_audience_params(data_front.audiencesJSON.valueDF,
                                                                           self.AUDIENCE_LIST)

            # call generate main data struct
            self.__gen_main_data_and_validate(data_front)
        except Exception as e:
            raise e

    @staticmethod
    def __gen_group_list_from_df(df: pd.DataFrame) -> list:
        return [tuple([row["number"], RUSSIAN_ALPHABET[count]])
                for index, row in df.iterrows()
                for count in range(row["count"])]

    @staticmethod
    def __gen_pedagogs_list_from_df(df: pd.DataFrame) -> list:
        return df["ped_name"].unique()

    @staticmethod
    def __gen_all_disciplines(df: pd.DataFrame) -> list:
        return df["discipline"].unique()

    @staticmethod
    def __gen_disciplines_with_pairs(df: pd.DataFrame) -> list:
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
    def __get_audience_list(audiencesDF: pd.DataFrame) -> list:
        return audiencesDF["number_audience"].unique()

    @staticmethod
    def __gen_audience_params(audiencesDF: pd.DataFrame, all_audiences: list) -> dict:
        return {audience: audiencesDF[audiencesDF["number_audience"] == audience]["params"].tolist()[0]
                for audience in all_audiences}
        # for audience in all_audiences:
        #     if audience[1] > 0
        #
        # pass

    def getAudienceForGeneration(self):
        df = self.data_from_front.audiencesJSON.valueDF
        # check value of link_flag if != 0 ret tuple
        # return list(map(lambda x: x[0] if x[1] == 0 else tuple(x),
        #                 df[["number_audience", "link_flags"]].drop_duplicates().values.tolist()))
        return list(map(lambda x: tuple(x),
                        df[["number_audience", "link_flags"]].drop_duplicates().values.tolist()))

    @staticmethod
    def __validateMainData(main_data: dict) -> None:
        for key, value in main_data.items():
            for disc, val in value.items():
                if val["load"] is None:
                    raise ValueError(
                        f'This discipline {disc} probably not implemented in pedagog model'
                        f'Group is - {key}'
                    )

    @staticmethod
    def __fill_main_data_load_for_group(main_data: dict, keys: tuple, discipline: str,
                                        load: int, pedagogs_load: dict, OTHER_DATA: dict):
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
        main_data[keys][discipline]["type_discipline"] = TYPE_DISCIPLINES.get(discipline)
        main_data[keys][discipline]["weight"] = WEIGHT_DISCIPLINES.get(keys[0], 11).get(discipline, 1)
        pedagogs_load[ped_name] = pedagogs_load.get(ped_name, 0) + load
        OTHER_DATA["whole_time"] = load + OTHER_DATA.get("whole_time", 0)

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
                                                                   self.__pedagogs_load, self.OTHER_DATA)
                 for row in zip(groupDF['discipline'], groupDF['load'])]
            AlgorithmSettings.__validateMainData(self.main_data)
        except Exception as e:
            raise e

    def getPedagogName(self, group: tuple, discipline: str):
        if group not in self.GROUPS_LIST:
            return None
        ret = self.main_data.get(group).get(discipline)
        return None if ret is None else ret["pedagog"]

    def getPedagogLoad(self, group: tuple, discipline: str):
        if group not in self.GROUPS_LIST:
            return None
        ret = self.main_data.get(group).get(discipline)
        return None if ret is None else ret["load"]

    def getPedagogNameAndLoad(self, group: tuple, discipline: str):
        """
        if main_data have needed group and discipline:
        ret == tuple[2] ==> ret[0] == dep_name, ret[1] == load value
        group found in self.GROUPS_LIST !
        else return None
        """

        if group not in self.GROUPS_LIST:
            return None
        ret = self.main_data.get(group).get(discipline)
        return None if ret is None else ret["pedagog"], ret["load"]

    def getGroupData(self, group: tuple):
        ret = self.main_data.get(group)
        return self.main_data.get(group)
