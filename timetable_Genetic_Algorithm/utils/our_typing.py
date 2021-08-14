from typing import Tuple

"""

    alias for Tuple with [0] == class(groups) number; [1] == letter
    examples:
        (1, "А")
        (11, "Г")
        ...
    
"""
Group = Tuple[int, str]
