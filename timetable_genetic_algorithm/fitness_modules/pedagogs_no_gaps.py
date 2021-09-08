from timetable_genetic_algorithm.fitness_utils import ModuleForFitnessFunctionBase, module_register
from timetable_genetic_algorithm.fitness_modules import constants_weight
from timetable_genetic_algorithm.utils.settings_generations import AMOUNT_TIMELINES_IN_DAY


@module_register
class PedagogsNoGaps(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = constants_weight.WINDOWS_PEDAGOG

    def get_fitness_penalty(self) -> int:
        day = self.shared_data.current_timeline // AMOUNT_TIMELINES_IN_DAY
        time = self.shared_data.current_timeline % AMOUNT_TIMELINES_IN_DAY
        ret = 0
        if self.shared_data.current_lesson:
            ped_name = self.shared_data.current_lesson[2]
            if day in self.shared_data.dict_count_pedago_windows.keys():
                if ped_name in self.shared_data.dict_count_pedago_windows[day].keys():
                    if time > self.shared_data.dict_count_pedago_windows[day][ped_name]:
                        ret += (time - self.shared_data.dict_count_pedago_windows[day][ped_name] - 1) \
                               * self.PENALTY_WEIGHT
                        self.shared_data.dict_count_pedago_windows[day][ped_name] = time
                else:
                    self.shared_data.dict_count_pedago_windows[day][ped_name] = time
            else:
                self.shared_data.dict_count_pedago_windows[day] = {ped_name: time}
        return ret

    def get_module_description(self):
        pass

    def get_module_naming(self) -> str:
        return "Отсутствие окон у педагога"

    def change_shared_data(self):
        pass
