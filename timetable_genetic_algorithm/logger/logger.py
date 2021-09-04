import logging
from dataclasses import dataclass, field
from typing import Dict, Any, Union


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
    penalty: Dict[Union[int, str], Union[Dict[str, int], int]] = field(default_factory=dict)
    best_individ: Dict[str, Any] = field(default_factory=dict)

    def penalty_for_individ(self, id_individ: int):
        ind = self.penalty.get(id_individ)
        if ind is None:
            logging.debug("incorrect id in |LoggerUtils|.|penalty_for_individ|")
        return ind.get("sum", float('inf'))

    def set_best_individ_if_best(self, current_individ):
        penalty = self.penalty_for_individ(current_individ.id_individ)
        if self.best_individ.get("penalty", float('inf')) > penalty:
            self.best_individ = self.penalty.get(current_individ.id_individ)

    def drop_sum_all_individs(self):
        self.penalty["sum_all_individs"] = 0

    def get_mean(self, population_len: int) -> int:
        mean = int(self.penalty.get("sum_all_individs") / population_len)
        return mean
