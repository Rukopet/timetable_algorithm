from abc import abstractmethod, ABCMeta
import pandas as pd


class OurJsonClass:
    """ Use this only for JSON !! We can adding other types transformations with JSON """

    def __init__(self, value):
        self.__valueJSON__ = value

    def intoDataFrame(self):
        """ change, when data format changes """
        if self.__valueJSON__:
            return pd.json_normalize(self.__valueJSON__)

    def intoDict(self):
        pass


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


class AllPossibleSets:
    """ contain main sets in DF format. no validate data!! """
    def __init__(self, groupsJSON: OurJsonClass, disciplinesJSON: OurJsonClass,
                 loadPlanJSON: OurJsonClass, pedagogsJSON: OurJsonClass, audiencesJSON: OurJsonClass):
        self.groupsDF = groupsJSON.intoDataFrame()
        self.disciplinesDF = disciplinesJSON.intoDataFrame()
        self.loadPlanDF = loadPlanJSON.intoDataFrame()
        self.pedagogsDF = pedagogsJSON.intoDataFrame()
        self.audiencesDF = audiencesJSON.intoDataFrame()


class DataFromFront(IDataFromFront):
    """ This class collect data, and parsing into needed shape """

    def __init__(self, groupsJSON=None, disciplinesJSON=None, loadPlanJSON=None, pedagogsJSON=None, audiencesJSON=None):
        self._groupsJSON = OurJsonClass(groupsJSON)
        self._disciplinesJSON = OurJsonClass(disciplinesJSON)
        self._loadPlanJSON = OurJsonClass(loadPlanJSON)
        self._pedagogsJSON = OurJsonClass(pedagogsJSON)
        self._audiencesJSON = OurJsonClass(audiencesJSON)

    def setGroupsJSON(self, groupsJSON):
        self._groupsJSON = OurJsonClass(groupsJSON)

    def setDisciplinesJSON(self, disciplinesJSON):
        self._disciplinesJSON = OurJsonClass(disciplinesJSON)

    def setLoadPlanJSON(self, loadPlanJSON):
        self._loadPlanJSON = OurJsonClass(loadPlanJSON)

    def setPedagogsJSON(self, pedagogsJSON):
        self._pedagogsJSON = OurJsonClass(pedagogsJSON)

    def setAudiencesJSON(self, audiencesJSON):
        self._audiencesJSON = OurJsonClass(audiencesJSON)

    def getAllPossibleSetsClass(self):
        """ Wrap calling this method into try/except! """
        if list(self.__dict__.values()).count(None) == 0:
            return AllPossibleSets(self._groupsJSON, self._disciplinesJSON,
                                   self._pedagogsJSON, self._audiencesJSON,
                                   self._loadPlanJSON)
        else:
            err_msg = ""
            for key, value in self.__dict__.items():
                if value is None:
                    err_msg += key + " "

            raise ValueError("Need set all JSON values before convert: " + err_msg)

a = DataFromFront()
# a.setAudiencesJSON("asd")
print(a.getAllPossibleSetsClass().__doc__)