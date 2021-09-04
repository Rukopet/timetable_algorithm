from random import shuffle
from typing import List

from timetable_genetic_algorithm.main_algorithm.generators_for_mutation import GeneratorsForMutation
from timetable_genetic_algorithm.utils import AlgorithmSettings


def get_shuffled_list_for_mutation(list_for_shuffle: List[int]) -> List[int]:
    shuffle(list_for_shuffle)
    return list_for_shuffle


def get_range_for_mutation(population_len: int, mutation_probability: float) -> int:
    return int(population_len * mutation_probability)


def swap_for_mutations(individ, table_settings: AlgorithmSettings, mut_gen: GeneratorsForMutation):
    for _ in range(table_settings.NUMBER_CELLS_FOR_SWAP_MUTATION):
        first_timeline, second_timeline = next(mut_gen.next_random_timeline), next(mut_gen.next_random_timeline)
        first_audience, second_audience = next(mut_gen.next_random_cell), next(mut_gen.next_random_cell)
        first = individ.dict_individ[first_timeline][first_audience]
        second = individ.dict_individ[second_timeline][second_audience]
        individ.dict_individ[first_timeline][first_audience] = second
        individ.dict_individ[second_timeline][second_audience] = first
        p = 1
