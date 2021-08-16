from copy import copy

from timetable_Genetic_Algorithm.utils import AlgorithmSettings


class Fitness:
    """a class of functions for checking all the necessary conditions of an individual"""

    def __init__(self, settings: AlgorithmSettings, individ: dict):
        self.settings = settings
        self.individ = individ
        self.lst_group = []
        self.dict_group = {}

# TODO what is faster: copy dict or create dict? + decorator property

    """
    in individ =>
    { tuple: int }
    
    time - prev
    
    {
        {
            
        }
    }
    
    
    """
    def get_one_group(self):
        for group in self.settings.GROUPS_LIST:
            for ktime, vtime in self.individ.items():
                for kaud, vaud in vtime.items():
                    if vaud != None and vaud[0] == group:
                        self.lst_group.append(vaud)
                self.dict_group[ktime] = copy(self.lst_group)
                self.lst_group.clear()

