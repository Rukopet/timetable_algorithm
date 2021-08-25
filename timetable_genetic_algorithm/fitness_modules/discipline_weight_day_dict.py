from timetable_genetic_algorithm.fitness_utils import ModuleForFitnessFunctionBase, module_register
from timetable_genetic_algorithm.utils import WEIGHT_DISCIPLINES
from timetable_genetic_algorithm.utils.settings_generations import AMOUNT_TIMELINES_IN_DAY


@module_register
class DisciplineWeightDayDict(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = 0

    def get_fitness_penalty(self) -> int:
        day = self.shared_data.current_timeline // AMOUNT_TIMELINES_IN_DAY
        if self.shared_data.current_lesson:
            group = self.shared_data.current_lesson[0]
            discipline = self.shared_data.current_lesson[1]
            if day not in self.shared_data.dict_count_disc_weight_day:
                self.shared_data.dict_count_disc_weight_day[day] = {}
            if group not in self.shared_data.dict_count_disc_weight_day[day]:
                if group[0] in WEIGHT_DISCIPLINES and discipline in WEIGHT_DISCIPLINES[group[0]]:
                    self.shared_data.dict_count_disc_weight_day[day][group] = [WEIGHT_DISCIPLINES[group[0]][discipline]]
                else:
                    self.shared_data.dict_count_disc_weight_day[day][group] = [1]
            else:
                if group[0] in WEIGHT_DISCIPLINES and discipline in WEIGHT_DISCIPLINES[group[0]]:
                    self.shared_data.dict_count_disc_weight_day[day][group].\
                        append(WEIGHT_DISCIPLINES[group[0]][discipline])
                else:
                    self.shared_data.dict_count_disc_weight_day[day][group].append(1)
        return 0

    def get_module_description(self) -> str:
        pass

    def get_module_naming(self) -> str:
        return "Создание словаря весов предметов"

    def change_shared_data(self) -> None:
        pass
