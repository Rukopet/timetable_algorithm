from timetable_genetic_algorithm.fitness_modules import constants_weight
from timetable_genetic_algorithm.fitness_utils import module_register, ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.utils.settings_generations import AMOUNT_TIMELINES_IN_DAY


@module_register
class GroupsUniqueness(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = constants_weight.NO_SINGLE_GROUP

    def get_fitness_penalty(self) -> int:
        ret = 0
        if self.shared_data.current_lesson:
            if self.shared_data.current_timeline in self.shared_data.dict_count_group_nosingle:
                if self.shared_data.current_lesson[0] in \
                        self.shared_data.dict_count_group_nosingle[self.shared_data.current_timeline]:
                    self.shared_data.dict_count_group_nosingle[self.shared_data.current_timeline]\
                        [self.shared_data.current_lesson[0]] += 1
                    if self.shared_data.current_lesson[1] not in self.settings.DISCIPLINES_LIST_WITH_PAIR or \
                            self.shared_data.current_lesson[1] in self.settings.DISCIPLINES_LIST_WITH_PAIR and \
                            self.shared_data.dict_count_group_nosingle[self.shared_data.current_timeline]\
                                    [self.shared_data.current_lesson[0]] > 2:
                        ret += self.PENALTY_WEIGHT
                    if self.shared_data.current_lesson[1] in self.settings.DISCIPLINES_LIST_WITH_PAIR and \
                            self.shared_data.dict_count_group_nosingle[self.shared_data.current_timeline]\
                                    [self.shared_data.current_lesson[0]] == 2 and \
                            self.shared_data.dict_count_disc_name[self.shared_data.current_timeline \
                                // AMOUNT_TIMELINES_IN_DAY][self.shared_data.current_lesson[0]] in \
                            self.settings.DISCIPLINE_DICT_WITH_LIST_PAIR:
                        ret -= self.PENALTY_WEIGHT
                else:
                    self.shared_data.dict_count_group_nosingle[self.shared_data.current_timeline]\
                        [self.shared_data.current_lesson[0]] = 1
                    if self.shared_data.current_lesson[1] in self.settings.DISCIPLINES_LIST_WITH_PAIR:
                        ret += self.PENALTY_WEIGHT
            else:
                self.shared_data.dict_count_group_nosingle[self.shared_data.current_timeline] \
                    = {self.shared_data.current_lesson[0]: 1}
        return ret

    def get_module_description(self) -> str:
        pass

    def get_module_naming(self) -> str:
        return "Один урок - одна группа"

    def change_shared_data(self) -> None:
        pass

