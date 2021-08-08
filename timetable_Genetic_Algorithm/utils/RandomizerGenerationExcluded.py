from random import choice


class RandomizerGenerationExcluded:
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

    def dropExcludedMainTuple(self):
        self.excluded_list_main_tuple.clear()

    def dropExcludedAudienceTuple(self):
        self.excluded_list_audiences_tuple.clear()


class RandomizerGenerationIncluded:
    """ Simple randomizer for generate populations """

    def __init__(self, len_main_tuple: int, len_audience_tuple: int, timeline: int):
        self.included_list_main_tuple = list(range(0, len_main_tuple))
        self.included_list_audiences_tuple = list(range(0, len_audience_tuple))
        self.len_main_tuple = len_main_tuple
        self.len_audience_tuple = len_audience_tuple
        self.timeline = timeline

    def getNumIncludedRandomForMainTuple(self) -> int:
        ret = choice(self.included_list_main_tuple)
        self.included_list_main_tuple.remove(ret)
        return ret

    def getNumIncludedRandomForAudienceTuple(self) -> int:
        ret = choice(self.included_list_audiences_tuple)
        self.included_list_audiences_tuple.remove(ret)
        return ret

    def getTupleIncludedRandomForMainTuple(self, main_tuple: list) -> tuple:
        ret = choice(self.included_list_main_tuple)
        self.included_list_main_tuple.remove(ret)
        return main_tuple[ret]

    def getTupleIncludedRandomForAudienceTuple(self, audience_tuple: list) -> tuple:
        ret = choice(self.included_list_audiences_tuple)
        self.included_list_audiences_tuple.remove(ret)
        return audience_tuple[ret]

    def dropIncludedMainTuple(self) -> None:
        self.included_list_main_tuple = list(range(0, self.len_main_tuple))

    def dropIncludedAudienceTuple(self) -> None:
        self.included_list_audiences_tuple = list(range(0, self.len_audience_tuple))
