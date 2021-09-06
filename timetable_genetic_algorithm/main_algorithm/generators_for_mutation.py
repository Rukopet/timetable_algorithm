from timetable_genetic_algorithm.utils import AlgorithmSettings
from random import choice
from typing import Generator, NoReturn

try:
    from typing import Final
except ImportError:
    from typing_extensions import Final


class GeneratorsForMutation:
    def __init__(self, table_settings: AlgorithmSettings, audience_tuple: tuple):
        self.__settings = table_settings
        self.__aud_tuple: Final = audience_tuple
        self.__lst_tmp: Final = list(range(table_settings.MAX_DAYS_FROM_JSON * table_settings.AMOUNT_TIMELINES_IN_DAY))
        self.next_random_timeline = self._generator_for_random_timeline()
        self.next_random_cell = self._generator_for_random_cell()

    def _generator_for_random_timeline(self) -> Generator[int, int, NoReturn]:
        while True:
            yield choice(self.__lst_tmp)

    def _generator_for_random_cell(self) -> Generator[tuple, tuple, NoReturn]:
        while True:
            yield choice(self.__aud_tuple)
