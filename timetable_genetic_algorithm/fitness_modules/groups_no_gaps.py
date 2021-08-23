from typing import Optional

from timetable_genetic_algorithm.fitness_modules import constants_weight
from timetable_genetic_algorithm.fitness_modules.constants_weight import WINDOWS_GROUP
from timetable_genetic_algorithm.fitness_utils import module_register, ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.utils.settings_generations import AMOUNT_TIMELINES_IN_DAY


@module_register
class GroupsNoGaps(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = constants_weight.WINDOWS_GROUP

    def get_fitness_penalty(self) -> int:
        """
        Groups fitness function for check of no windows in each Group schedule

        :return: int
        """
        day = self.shared_data.current_timeline // AMOUNT_TIMELINES_IN_DAY
        time = self.shared_data.current_timeline % AMOUNT_TIMELINES_IN_DAY
        ret = 0
        if self.shared_data.current_lesson:
            if day in self.shared_data.dict_count_group_windows.keys():
                if self.shared_data.current_lesson[0] in self.shared_data.dict_count_group_windows[day].keys():
                    if time > self.shared_data.dict_count_group_windows[day][self.shared_data.current_lesson[0]]:
                        ret += (time - self.shared_data.dict_count_group_windows[day][self.shared_data.current_lesson[0]] - 1) \
                               * self.PENALTY_WEIGHT
                        self.shared_data.dict_count_group_windows[day][self.shared_data.current_lesson[0]] = time
                else:
                    self.shared_data.dict_count_group_windows[day][self.shared_data.current_lesson[0]] = time
            else:
                self.shared_data.dict_count_group_windows[day] = {self.shared_data.current_lesson[0]: time}
        return ret

    def get_module_description(self):
        pass

    def get_module_naming(self) -> str:
        return "Отсутстиве окон у групп"

    def change_shared_data(self):
        pass
