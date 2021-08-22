import logging
from dataclasses import dataclass
from typing import Dict


class LoggerPenalty:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return ""

    def __repr__(self) -> str:
        return ""


# TODO LoggerUtils for Loggerpenalty in loop in dict Dict[timeline: LoggerUtils instance]
@dataclass
class LoggerUtils:
    penalty: Dict[int, Dict[str, int]]

    def penalty_for_individ(self, id_individ: int):
        whole_penalties = self.penalty.get(id_individ)
        if whole_penalties is None:
            msg = f'id={id_individ} not in dict penalty'
            logging.debug(msg)
            raise ValueError
        return sum(whole_penalties.values())
