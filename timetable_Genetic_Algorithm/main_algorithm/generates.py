from abc import abstractmethod, ABCMeta


class AlgorithmSettings:
    """ settings for whole project """
    DEBUG = 0

    GROUPS_RANGE = {"min": 1, "max": 11}
    # dict with min and max num of groups

    groups_list_DF = []
    # all groups struct [{"number": int, "letter": 'str'}]

    pedagogs_list = []
    """
    all pedagogs struct:
    [
        {
            "name": str,
            "disciplines": [
                                {
                                    "disc": str,
                                    "groups": [
                                                *groups_list
                                              ]
                                }
                            ]
        }
    ]
    """

    disciplines_list = []
    """
    
    """

    def setListGroups(self, groups: list):
        pass

    def setPedagogsDisciplinesLists(self, pedagogs: list, disciplines: list):
        pass


class IFirstGeneration:
    """ Interface for FirstGeneration Class """
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def generate(size_population: int, settings: AlgorithmSettings):
        pass