from typing import Tuple, List, Any

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
Population = List[Any]
"""
    
    alias for list tuples

"""