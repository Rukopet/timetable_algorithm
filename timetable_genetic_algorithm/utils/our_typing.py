from typing import Tuple, List

from timetable_genetic_algorithm.utils.Individ import Individ

"""

    alias for Tuple with [0] == class(groups) number; [1] == letter
    examples:
        (1, "А")
        (11, "Г")
        ...
        
    Groups this same like group, but many in list
    
"""
Group = Tuple[int, str]
Groups = List[Group]

Audience = Tuple[int, int]
Audiences = List[Audience]

# Individ = dict
Population = List[Individ]
"""
    
    alias for list tuples

"""