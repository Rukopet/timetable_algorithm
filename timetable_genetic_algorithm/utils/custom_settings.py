from abc import abstractmethod, ABCMeta
import pandas as pd


class OurJsonClass:
    """ Use this only for JSON !! We can adding other types transformations with JSON """

    def __init__(self, value):
        self.__valueJSON__ = value
        self.valueDF = None

    def into_data_frame(self):
        """ change, when data format changes """
        if self.valueDF:
            return self.valueDF

    def set_value_df(self, valueDF):
        self.valueDF = valueDF
    #
    # def intoDict(self):
    #     pass


class IDataFromFront:
    """ interface for our base classes (DataFronts) """
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_groups_json(self, JSON):
        pass

    @abstractmethod
    def set_disciplines_json(self, JSON):
        pass

    @abstractmethod
    def set_load_plan_json(self, JSON):
        pass

    @abstractmethod
    def set_pedagogs_json(self, JSON):
        pass

    @abstractmethod
    def set_audiences_json(self, JSON):
        pass


class DataFromFront(IDataFromFront):
    """ This class collect data, and parsing into needed shape """

    def __init__(self, groupsJSON=None, disciplinesJSON=None, loadPlanJSON=None, pedagogsJSON=None, audiencesJSON=None):
        self.groupsJSON = OurJsonClass(groupsJSON)
        self.disciplinesJSON = OurJsonClass(disciplinesJSON)
        self.loadPlanJSON = OurJsonClass(loadPlanJSON)
        self.pedagogsJSON = OurJsonClass(pedagogsJSON)
        self.audiencesJSON = OurJsonClass(audiencesJSON)

    def set_groups_json(self, groupsJSON):
        self.groupsJSON = OurJsonClass(groupsJSON)
        df = pd.json_normalize(groupsJSON, record_path=['groups'],
                               meta=['second_shift',
                                     'max_days'])
        self.groupsJSON.set_value_df(df)

    def set_disciplines_json(self, disciplinesJSON):
        self.disciplinesJSON = OurJsonClass(disciplinesJSON)
        df = pd.DataFrame(data=disciplinesJSON)
        self.disciplinesJSON.set_value_df(df)

    def set_load_plan_json(self, loadPlanJSON):
        self.loadPlanJSON = OurJsonClass(loadPlanJSON)
        df = pd.json_normalize(loadPlanJSON, record_path=['discipline'],
                               meta=['num',
                                     'letter'])
        self.loadPlanJSON.set_value_df(df)

    def set_pedagogs_json(self, pedagogsJSON):
        self.pedagogsJSON = OurJsonClass(pedagogsJSON)
        df = pd.json_normalize(pedagogsJSON, record_path=['disciplines'],
                               meta=["ped_name"])
        self.pedagogsJSON.set_value_df(df)

    def set_audiences_json(self, audiencesJSON):
        self.audiencesJSON = OurJsonClass(audiencesJSON)
        # df = pd.json_normalize(audiencesJSON, record_path=['params'],
        #                        meta=["number_audience",
        #                              "link_flags"])
        df = pd.DataFrame(data=audiencesJSON)
        self.audiencesJSON.set_value_df(df)

