from abc import abstractmethod, ABCMeta
import pandas as pd
import json


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


class AllPossibleSetsInDF:
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

    def getAllPossibleSetsInDFClass(self):
        """ Wrap calling this method into try/except! """

        try:
            # if list(self.__dict__.values()).count(None) == 0:
            if True:
                ret = AllPossibleSetsInDF(self.groupsJSON, self.disciplinesJSON,
                                          self.pedagogsJSON, self.audiencesJSON,
                                          self.loadPlanJSON)
                return ret
            else:
                err_msg = ""
                for key, value in self.__dict__.items():
                    if value is None:
                        err_msg += key + " "

                raise ValueError("Need set all JSON values before convert: " + err_msg)
        except Exception as e:
            raise e


def main():
    wow = DataFromFront()
    with open("../data_for_test/disciplines_model.json") as disciplines_json:
        wow.setDisciplinesJSON(json.load(disciplines_json))
    with open("../data_for_test/group_model.json") as groups_json:
        wow.setGroupsJSON(json.load(groups_json))
        # print(wow.groupsJSON.valueDF)
    with open("../data_for_test/load_plan.json") as load_plan_json:
        wow.setLoadPlanJSON(json.load(load_plan_json))
    with open("../data_for_test/pedagogs_model.json") as pedagogs_json:
        wow.setPedagogsJSON(json.load(pedagogs_json))
        wow.pedagogsJSON.valueDF.
        # print(wow.pedagogsJSON.valueDF)

    # DFS = wow.getAllPossibleSetsInDFClass()
    # print(DFS.groupsDF)


if __name__ == "__main__":
    main()
