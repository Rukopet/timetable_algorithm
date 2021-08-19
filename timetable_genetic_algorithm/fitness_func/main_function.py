from typing import Type

from timetable_genetic_algorithm.utils.Individ import Individ


def fitness_function(individ: Individ):

    for timeline in individ.dict_individ.keys():
        for auditory, lesson in individ.dict_individ[timeline].items():
            pass
