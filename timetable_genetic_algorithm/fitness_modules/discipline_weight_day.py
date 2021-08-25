from timetable_genetic_algorithm.fitness_modules import constants_weight
from timetable_genetic_algorithm.fitness_utils import ModuleForFitnessFunctionBase, module_register


@module_register
class DisciplineWeightDay(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = constants_weight.DISCIPLINES_WEIGHT_DAY

    def get_fitness_penalty(self) -> int:
        return 0

    def get_module_description(self) -> str:
        pass

    def get_module_naming(self) -> str:
        return "Распределение сложности дисциплин в день"

    def change_shared_data(self) -> None:
        pass

    def final_action(self) -> int:
        ret = 0
        for day, dict_group in self.shared_data.dict_count_disc_weight_day.items():
            for group, list_weight in dict_group.items():
                length = len(list_weight)
                if group not in self.shared_data.dict_count_disc_weight_week:
                    self.shared_data.dict_count_disc_weight_week[group] = [sum(list_weight)]
                else:
                    self.shared_data.dict_count_disc_weight_week[group].append(sum(list_weight))
                if length == 4:
                    if list_weight[0] > list_weight[1]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[0] > list_weight[2]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[3] > list_weight[1]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[3] > list_weight[2]:
                        ret += self.PENALTY_WEIGHT
                if length == 5:
                    if list_weight[0] > list_weight[1]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[0] > list_weight[2]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[0] > list_weight[3]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[4] > list_weight[1]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[4] > list_weight[2]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[4] > list_weight[3]:
                        ret += self.PENALTY_WEIGHT
                if length == 6:
                    if list_weight[0] > list_weight[1]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[0] > list_weight[2]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[0] > list_weight[3]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[0] > list_weight[4]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[5] > list_weight[1]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[5] > list_weight[2]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[5] > list_weight[3]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[5] > list_weight[4]:
                        ret += self.PENALTY_WEIGHT
                if length == 7:
                    if list_weight[0] > list_weight[1]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[0] > list_weight[2]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[0] > list_weight[3]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[0] > list_weight[4]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[5] > list_weight[1]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[5] > list_weight[2]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[5] > list_weight[3]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[5] > list_weight[4]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[6] > list_weight[1]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[6] > list_weight[2]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[6] > list_weight[3]:
                        ret += self.PENALTY_WEIGHT
                    if list_weight[6] > list_weight[4]:
                        ret += self.PENALTY_WEIGHT
        return ret
