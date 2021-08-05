from abc import abstractmethod, ABCMeta
import pandas as pd


class OurJsonClass:
    """ Use this only for JSON !! We can adding other types transformations with JSON """

    def __init__(self, value):
        self.__valueJSON__ = value
        self.valueDF = None

    def intoDataFrame(self):
        """ change, when data format changes """
        if self.valueDF:
            return self.valueDF

    def setValueDF(self, valueDF):
        self.valueDF = valueDF
    #
    # def intoDict(self):
    #     pass


class IDataFromFront:
    """ interface for our base classes (DataFronts) """
    __metaclass__ = ABCMeta

    @abstractmethod
    def setGroupsJSON(self, JSON):
        pass

    @abstractmethod
    def setDisciplinesJSON(self, JSON):
        pass

    @abstractmethod
    def setLoadPlanJSON(self, JSON):
        pass

    @abstractmethod
    def setPedagogsJSON(self, JSON):
        pass

    @abstractmethod
    def setAudiencesJSON(self, JSON):
        pass


class DataFromFront(IDataFromFront):
    """ This class collect data, and parsing into needed shape """

    def __init__(self, groupsJSON=None, disciplinesJSON=None, loadPlanJSON=None, pedagogsJSON=None, audiencesJSON=None):
        self.groupsJSON = OurJsonClass(groupsJSON)
        self.disciplinesJSON = OurJsonClass(disciplinesJSON)
        self.loadPlanJSON = OurJsonClass(loadPlanJSON)
        self.pedagogsJSON = OurJsonClass(pedagogsJSON)
        self.audiencesJSON = OurJsonClass(audiencesJSON)

    def setGroupsJSON(self, groupsJSON):
        self.groupsJSON = OurJsonClass(groupsJSON)
        df = pd.json_normalize(groupsJSON, record_path=['groups'],
                               meta=['second_shift',
                                     'max_days'])
        self.groupsJSON.setValueDF(df)

    def setDisciplinesJSON(self, disciplinesJSON):
        self.disciplinesJSON = OurJsonClass(disciplinesJSON)
        df = pd.DataFrame(data=disciplinesJSON)
        self.disciplinesJSON.setValueDF(df)

    def setLoadPlanJSON(self, loadPlanJSON):
        self.loadPlanJSON = OurJsonClass(loadPlanJSON)
        df = pd.json_normalize(loadPlanJSON, record_path=['discipline'],
                               meta=['num',
                                     'letter'])
        self.loadPlanJSON.setValueDF(df)

    def setPedagogsJSON(self, pedagogsJSON):
        self.pedagogsJSON = OurJsonClass(pedagogsJSON)
        df = pd.json_normalize(pedagogsJSON, record_path=['disciplines'],
                               meta=["ped_name"])
        self.pedagogsJSON.setValueDF(df)

    def setAudiencesJSON(self, audiencesJSON):
        self.audiencesJSON = OurJsonClass(audiencesJSON)
        df = pd.json_normalize(audiencesJSON, record_path=['params'],
                               meta=["number_audience",
                                     "link_flags"])
        self.audiencesJSON.setValueDF(df)
