from random import shuffle
from typing import List


def get_shuffled_list_for_mutation(list_for_shuffle: List[int]) -> List[int]:
    shuffle(list_for_shuffle)
    return list_for_shuffle


def get_range_for_mutation(population_len: int, mutation_probability: float) -> int:
    return int(population_len * mutation_probability)


def swap_for_mutations(individ, mutation_probability: float):
    ...
