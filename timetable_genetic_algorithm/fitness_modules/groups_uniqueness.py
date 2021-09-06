from timetable_genetic_algorithm.fitness_modules import constants_weight
from timetable_genetic_algorithm.fitness_utils import module_register, ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.utils.settings_generations import AMOUNT_TIMELINES_IN_DAY


@module_register
class GroupsUniqueness(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = constants_weight.NO_SINGLE_GROUP

    def get_fitness_penalty(self) -> int:
        ret = 0
        if self.shared_data.current_lesson:
            time = self.shared_data.current_timeline
            group = self.shared_data.current_lesson[0]
            discipline = self.shared_data.current_lesson[1]
            if time in self.shared_data.dict_count_group_nosingle:
                if group in self.shared_data.dict_count_group_nosingle[time]:
                    self.shared_data.dict_count_group_nosingle[time][group] += 1
                    if discipline not in self.settings.DISCIPLINES_LIST_WITH_PAIR or \
                            discipline in self.settings.DISCIPLINES_LIST_WITH_PAIR and \
                            self.shared_data.dict_count_group_nosingle[time][group] > 2:
                        ret += self.PENALTY_WEIGHT
                    if discipline in self.settings.DISCIPLINES_LIST_WITH_PAIR and \
                            self.shared_data.dict_count_group_nosingle[time][group] == 2 and \
                            self.shared_data.dict_count_disc_name[time // AMOUNT_TIMELINES_IN_DAY][group] in \
                            self.settings.DISCIPLINE_DICT_WITH_LIST_PAIR:
                        ret -= self.PENALTY_WEIGHT
                else:
                    self.shared_data.dict_count_group_nosingle[time][group] = 1
                    if discipline in self.settings.DISCIPLINES_LIST_WITH_PAIR:
                        ret += self.PENALTY_WEIGHT
            else:
                self.shared_data.dict_count_group_nosingle[time] = {group: 1}
        return ret

    def get_module_description(self) -> str:
        pass

    def get_module_naming(self) -> str:
        return "Один урок - одна группа"

    def change_shared_data(self) -> None:
        pass

