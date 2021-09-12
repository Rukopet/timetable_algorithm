import random
from copy import copy
from typing import List, Dict

from timetable_genetic_algorithm.fitness_func.main_function import fitness_function
from timetable_genetic_algorithm.logger.logger import LoggerUtils
from timetable_genetic_algorithm.main_algorithm.generators_for_mutation import GeneratorsForMutation
from timetable_genetic_algorithm.utils.Individ import Individ
from timetable_genetic_algorithm.utils.algorithm_settings import AlgorithmSettings

PopulationType = List[Individ]


def generate_dict_for_logger(population: PopulationType) -> Dict[int, Dict[str, int]]:
    ret = {
        ind.id_individ: {"instance": ind}
        for ind in population
    }
    ret["sum_all_individs"] = 0
    return ret


def tournament_selection(table_settings: AlgorithmSettings,
                         population: List[Individ],
                         log: LoggerUtils) -> PopulationType:
    offspring = []
    END_OF_WHILE = 5

    # p_len = table_settings.TOTAL_POPULATION
    p_len = len(population)
    for n in range(p_len):
        i1 = i2 = i3 = 0
        flag = 0
        while (i1 == i2 or i1 == i3 or i2 == i3) and flag < END_OF_WHILE:
            i1, i2, i3 = random.randint(0, p_len - 1), random.randint(0, p_len - 1), random.randint(0, p_len - 1)
            flag += 1
        take_three = {
            i1: log.penalty[i1]["sum"],
            i2: log.penalty[i2]["sum"],
            i3: log.penalty[i3]["sum"]
        }
        best_individ = min(take_three, key=take_three.get)
        if population[best_individ] not in offspring:
            offspring.append(population[best_individ])
    return offspring


def copy_offspring(population: PopulationType, table_settings: AlgorithmSettings) -> PopulationType:
    ret_offspring: PopulationType = [
        Individ(population[new_id_individ].dict_individ.copy(), table_settings, new_id_individ)
        for new_id_individ in range(len(population))
    ]
    return ret_offspring


def parent_crossover(general_parent: Individ, second_parent: Individ) -> Individ:
    child = copy(general_parent)
    count = random.randint(0, child.settings.MAX_DAYS_FROM_JSON * child.settings.AMOUNT_TIMELINES_IN_DAY)
    for _ in range(count):
        timeline = random.randint(0, child.settings.MAX_DAYS_FROM_JSON * child.settings.AMOUNT_TIMELINES_IN_DAY - 1)
        audience = random.choice(child.settings.get_audience_for_generation())
        while child.dict_individ[timeline][audience] is None:
            timeline = random.randint(0, child.settings.MAX_DAYS_FROM_JSON * child.settings.AMOUNT_TIMELINES_IN_DAY - 1)
            audience = random.choice(child.settings.get_audience_for_generation())
        time_list = [i for i in range(0, child.settings.MAX_DAYS_FROM_JSON * child.settings.AMOUNT_TIMELINES_IN_DAY)]
        random.shuffle(time_list)
        for time in time_list:
            if child.dict_individ[timeline][audience] in second_parent.dict_individ[time].values():
                break
        for aud in second_parent.dict_individ[time].keys():
            if second_parent.dict_individ[time][aud] == child.dict_individ[timeline][audience]:
                break
        tmp = child.dict_individ[timeline][audience]
        child.dict_individ[timeline][audience] = child.dict_individ[time][aud]
        child.dict_individ[time][aud] = tmp
    return child


def childbirth(mom: Individ, dad: Individ, table_setting: AlgorithmSettings, log, id_child: int) -> Individ:
    i = random.randint(0, 1)
    if i == 0:
        child = parent_crossover(mom, dad)
    else:
        child = parent_crossover(dad, mom)
    child.id_individ = id_child
    log.penalty[id_child] = {}
    fitness_function(table_setting, child, log)
    return child


def crossover(table_settings: AlgorithmSettings, current_population: PopulationType, log):
    if len(current_population) < 2:
        raise ValueError(f"Too small population")
    while len(current_population) < table_settings.TOTAL_POPULATION:
        p_len = len(current_population)
        i1 = i2 = 0
        while i1 == i2:
            i1, i2 = random.randint(0, p_len - 1), random.randint(0, p_len - 1)
        mom_individ = current_population[i1]
        dad_individ = current_population[i2]
        new_individ = childbirth(mom_individ, dad_individ, table_settings, log, p_len)
        current_population.append(new_individ)


def mutation(table_settings: AlgorithmSettings,
             current_population: PopulationType,
             mut_gen: GeneratorsForMutation):
    """

    :param current_population:
    :param table_settings:
    :type mut_gen: object
    """
    from timetable_genetic_algorithm.main_algorithm.mutation_utils import get_shuffled_list_for_mutation, \
        get_range_for_mutation, swap_for_mutations
    shuffled_list = get_shuffled_list_for_mutation(table_settings.PRE_GENERATED_LIST_RANGE_POPULATION.copy())
    number_of_mutations = get_range_for_mutation(table_settings.TOTAL_POPULATION, table_settings.P_MUTATION)
    for number_ind in range(number_of_mutations):
        current_individ = current_population[shuffled_list[number_ind]]
        current_individ.into_excel_file(file_name="1.xls")
        swap_for_mutations(current_individ, table_settings, mut_gen)
        current_individ.into_excel_file(file_name="2.xls")


def main_loop(table_settings: AlgorithmSettings, population: PopulationType, audience_tuple: tuple) -> Individ:
    from timetable_genetic_algorithm.utils.plot_drawer import PlotDrawer

    best_individ = None
    draw = PlotDrawer()
    mutation_generators = GeneratorsForMutation(table_settings, audience_tuple)

    for generation in range(table_settings.COUNT_GENERATIONS):
        log = LoggerUtils()
        log.penalty = generate_dict_for_logger(population)

        for individ in population:
            fitness_function(table_settings, individ, log)
        best_individ = log.best_individ
        if best_individ.get("sum") <= table_settings.EXIT_OF_ALGORITHM:
            break
        offspring = tournament_selection(table_settings, population, log)
        offspring = copy_offspring(offspring, table_settings)

        print(generation)
        print(best_individ.get("sum"))
        crossover(table_settings, offspring, log)
        mutation(table_settings, offspring, mutation_generators)

        population = offspring

        best = best_individ.get("sum")
        draw.max_append(best)
        draw.mean_append(log.get_mean(table_settings.TOTAL_POPULATION))
        del log

    if table_settings.DEBUG == 1:
        draw.show_plot()
    return best_individ.get("instance")
