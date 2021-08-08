from random import choice


class RandomizerGeneration:
    """ Simple randomizer for generate populations """

    def __init__(self, len_main_tuple: int, len_audience_tuple: int):
        self.excluded_list_main_tuple = []
        self.excluded_list_audiences_tuple = []
        self.len_main_tuple = len_main_tuple
        self.len_audience_tuple = len_audience_tuple

    def getNumExcludeRandomForMainTuple(self) -> int:
        ret = choice([i for i in range(0, self.len_main_tuple) if i not in self.excluded_list_main_tuple])
        self.excluded_list_main_tuple.append(ret)
        return ret

    def getNumExcludeRandomForAudienceTuple(self) -> int:
        ret = choice([i for i in range(0, self.len_audience_tuple)
                      if i not in self.excluded_list_audiences_tuple])
        self.excluded_list_audiences_tuple.append(ret)
        return ret

    def getTupleExcludeRandomForMainTuple(self, main_tuple: list) -> tuple:
        ret = choice([i for i in range(0, self.len_main_tuple) if i not in self.excluded_list_main_tuple])
        self.excluded_list_main_tuple.append(ret)
        return main_tuple[ret]

    def getTupleExcludeRandomForAudienceTuple(self, audience_tuple: list) -> tuple:
        ret = choice([i for i in range(0, self.len_audience_tuple)
                      if i not in self.excluded_list_audiences_tuple])
        self.excluded_list_audiences_tuple.append(ret)
        return audience_tuple[ret]
