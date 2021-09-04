import logging
from dataclasses import dataclass, field
from typing import Dict, Any


class LoggerPenalty:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return ""

    def __repr__(self) -> str:
        return ""


def is_dict_empty(current_dict: dict) -> bool:
    if len(current_dict) == 0:
        return True
    return False


# TODO LoggerUtils for Loggerpenalty in loop in dict Dict[timeline: LoggerUtils instance]
@dataclass
class LoggerUtils:
    penalty: Dict[int, Dict[str, int]] = field(default_factory=dict)
    best_individ: Dict[str, Any] = field(default_factory=dict)

    def penalty_for_individ(self, id_individ: int):
        ind = self.penalty.get(id_individ)
        if ind is None:
            logging.debug("incorrect id in |LoggerUtils|.|penalty_for_individ|")
        return ind.get("penalty", float('inf'))

    def set_best_individ_if_best(self, current_individ):
        penalty = self.penalty_for_individ(current_individ.id_individ)
        if self.best_individ.get("penalty", float('inf')) > penalty:
            self.best_individ["instance"] = current_individ
            self.best_individ["penalty"] = penalty
