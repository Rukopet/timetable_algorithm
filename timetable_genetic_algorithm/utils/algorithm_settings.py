from typing import Dict, Tuple, Union, List, Any

import pandas as pd

from timetable_genetic_algorithm.fitness_utils.our_typing import Discipline
from timetable_genetic_algorithm.utils.constants import RUSSIAN_ALPHABET, TYPE_DISCIPLINES, WEIGHT_DISCIPLINES
from timetable_genetic_algorithm.utils.custom_settings import DataFromFront
from timetable_genetic_algorithm.utils import settings_generations
from timetable_genetic_algorithm.utils.our_typing import Audience, Group
try:
    from typing import Final
except ImportError:
    from typing_extensions import Final


def from_list_of_dicts_to_list_values(list_dicts: List[Dict], column: str) -> List[str]:
    return [
        d.get(column, 'Unknown')
        for d in list_dicts
    ]


def get_appended_default_list(dict_with_list, key: Any, appended_val: Any) -> List[Any]:
    tmp_val = dict_with_list.get(key, [])
    tmp_val.append(appended_val)
    dict_with_list[key] = tmp_val
    return tmp_val


class AlgorithmSettings:
    """ settings for whole project """
    DEBUG = 0

    GROUPS_RANGE = {"min": 1, "max": 11}

    """
    GROUPS_LIST = ("num", "letter") ==> (1, "А")
    """

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
        num_audience: int --> params
    """
    AUDIENCE_PARAMS = {}

    IS_GROUP_STUDY_SATURDAY = {}
    IS_GROUP_STUDY_IN_SECOND_SHIFT = {}
    bool_SCHOOL_STUDY_SATURDAY = True
    bool_SCHOOL_SECOND_SHIFT = False

    GROUPS_AUDIENCE_LINK: Dict[Group, Audience] = {}
    DISCIPLINES_AUDIENCE_LINK: Dict[Discipline, Audience] = {}
    DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK: Dict[Union[Group, Discipline], Audience] = {}
    DISCIPLINE_DICT_WITH_LIST_PAIR: Dict[Discipline, List[Discipline]] = {}

    TOTAL_POPULATION = settings_generations.TOTAL_POPULATION
    P_CROSSOVER = settings_generations.P_CROSSOVER
    P_MUTATION = settings_generations.P_MUTATION
    AMOUNT_TIMELINES_IN_DAY = settings_generations.AMOUNT_TIMELINES_IN_DAY
    TIME_FIRST_LESSON_SECOND_SHIFT = settings_generations.TIME_FIRST_LESSON_SECOND_SHIFT
    COUNT_GENERATIONS = settings_generations.COUNT_GENERATIONS
    PRE_GENERATED_LIST_RANGE_POPULATION: Final = list(range(settings_generations.TOTAL_POPULATION))
    PRE_GENERATED_LIST_TIMELINES = []
    NUMBER_CELLS_FOR_SWAP_MUTATION = 0
    MAX_DAYS_FROM_JSON = 5

    def __init__(self, data_front: DataFromFront):
        self.data_from_front = data_front
        self._validation_set_main_data(data_front)

    def _validation_set_main_data(self, data_front: DataFromFront):
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
            self.MAX_DAYS_FROM_JSON = self.data_from_front.groupsJSON.__valueJSON__.get("max_days", 5)
            if self.MAX_DAYS_FROM_JSON == 6:
                self.IS_GROUP_STUDY_SATURDAY = self.__gen_is_group_study_saturday()
            else:
                self.bool_SCHOOL_STUDY_SATURDAY = False

            if self.data_from_front.groupsJSON.__valueJSON__.get("second_shift", False):
                self.bool_SCHOOL_SECOND_SHIFT = True
                self.IS_GROUP_STUDY_IN_SECOND_SHIFT = self.__gen_is_group_study_in_second_shift()

            self.GROUPS_AUDIENCE_LINK, self.DISCIPLINES_AUDIENCE_LINK = self.__gen_groups_audience_disciplines_link(
                data_front.audiencesJSON.valueDF
            )
            self.DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK = self.__gen_disciplines_groups_for_audience_link(
                data_front.audiencesJSON.valueDF
            )
            self.DISCIPLINE_DICT_WITH_LIST_PAIR = self.__gen_disciplines_list_with_pair(
                data_front.disciplinesJSON.valueDF
            )
            self.NUMBER_CELLS_FOR_SWAP_MUTATION = self.__get_number_cells_for_swap_mutation()

        except Exception as e:
            raise e

    def __get_number_cells_for_swap_mutation(self) -> int:
        return int(self.OTHER_DATA["whole_time"] / 10)

    @staticmethod
    def __gen_groups_audience_disciplines_link(df: pd.DataFrame) -> Tuple[Dict[Group, Audience],
                                                                          Dict[Discipline, Audience]]:
        tmp_df = df[(df["link_flags"] == 1) | (df["link_flags"] == 2)]
        #print(tmp_df)
        discipline_audience, group_audience = {}, {}
        for link_flag, audience, list_groups_or_disc in zip(tmp_df["link_flags"],
                                                            tmp_df["number_audience"],
                                                            tmp_df["params"]):
            for discipline_or_group in list_groups_or_disc:
                if link_flag == 1:
                    disc = discipline_or_group.get('discipline')
                    get_appended_default_list(discipline_audience, disc, audience)
                elif link_flag == 2:
                    group = tuple(discipline_or_group.values())
                    get_appended_default_list(group_audience, group, audience)
        return group_audience, discipline_audience

    @staticmethod
    def __gen_disciplines_groups_for_audience_link(df: pd.DataFrame) -> Dict[Union[Group, Discipline], Audience]:
        tmp_df = df[df["link_flags"] == 3]
        return {
            group.get('discipline', tuple([group.get('num'), group.get('letter')])): audience
            for list_groups, audience in zip(tmp_df["params"], tmp_df["number_audience"])
            for group in list_groups
        }

    @staticmethod
    def __gen_disciplines_list_with_pair(df: pd.DataFrame) -> Dict[Discipline, List[Discipline]]:
        tmp_df = df.dropna(subset=["pair"], inplace=False)
        ret = {}
        for discipline, pair_list in zip(tmp_df["discipline"], tmp_df["pair"]):
            for pair in from_list_of_dicts_to_list_values(pair_list, 'discipline'):
                val = ret.get(discipline, [])
                val.append(pair)
                ret[discipline] = val
        return ret

    @staticmethod
    def __gen_group_list_from_df(df: pd.DataFrame) -> list:
        return [tuple([row["number"], RUSSIAN_ALPHABET[count]])
                for index, row in df.iterrows()
                for count in range(row["count"])]

    @staticmethod
    def __gen_pedagogs_list_from_df(df: pd.DataFrame) -> list:
        return df["ped_name"].unique()

    def __gen_is_group_study_saturday(self) -> dict:
        df = self.data_from_front.groupsJSON.valueDF
        p = df.loc[(df["number"] == 1)]["saturday_not_study"].values[0]
        return {group: True if df.loc[(df["number"] == group[0])]["saturday_not_study"].values[0] else False
                for group in self.GROUPS_LIST}

    def __gen_is_group_study_in_second_shift(self) -> dict:
        df = self.data_from_front.groupsJSON.valueDF
        return {group: df[(df["number"] == group[0])]["second_shift"].values[0]
                for group in self.GROUPS_LIST}

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

    def get_audience_for_generation(self):
        df = self.data_from_front.audiencesJSON.valueDF
        return list(map(lambda x: tuple(x),
                        df[["number_audience", "link_flags"]].drop_duplicates().values.tolist()))

    @staticmethod
    def __validate_main_data(main_data: dict) -> None:
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
            AlgorithmSettings.__validate_main_data(self.main_data)
        except Exception as e:
            raise e

    def get_pedagog_name(self, group: tuple, discipline: str):
        if group not in self.GROUPS_LIST:
            return None
        ret = self.main_data.get(group).get(discipline)
        return None if ret is None else ret["pedagog"]

    def get_pedagog_load(self, group: tuple, discipline: str):
        if group not in self.GROUPS_LIST:
            return None
        ret = self.main_data.get(group).get(discipline)
        return None if ret is None else ret["load"]

    def get_pedagog_name_and_load(self, group: tuple, discipline: str):
        """
        if main_data have needed group and discipline:
        ret == tuple[2] ==> ret[0] == dep_name, ret[1] == load value
        group found in self.GROUPS_LIST !
        else return None
        """

        if group not in self.GROUPS_LIST:
            return None
        ret = self.main_data.get(group, {}).get(discipline)
        return None if ret is None else ret["pedagog"], ret["load"]

    def get_group_data(self, group: tuple):
        return self.main_data.get(group)
