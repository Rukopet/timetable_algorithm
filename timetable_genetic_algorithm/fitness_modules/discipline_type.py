from timetable_genetic_algorithm.fitness_modules import constants_weight
from timetable_genetic_algorithm.fitness_utils import module_register, ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.utils import TYPE_DISCIPLINES
from timetable_genetic_algorithm.utils.settings_generations import AMOUNT_TIMELINES_IN_DAY


@module_register
class DisciplineType(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = constants_weight.DISCIPLINES_TYPE

    def get_fitness_penalty(self) -> int:
        time = self.shared_data.current_timeline % AMOUNT_TIMELINES_IN_DAY
        day = self.shared_data.current_timeline // AMOUNT_TIMELINES_IN_DAY
        ret = 0
        if self.shared_data.current_lesson:
            group = self.shared_data.current_lesson[0]
            discipline = self.shared_data.current_lesson[1]
            first_lesson = self.shared_data.current_lesson[4]
            if day not in self.shared_data.dict_count_disc_type:
                self.shared_data.dict_count_disc_type[day] = {}
            if time == first_lesson or group not in self.shared_data.dict_count_disc_type[day]:
                self.shared_data.dict_count_disc_type[day][group] = TYPE_DISCIPLINES.get(discipline, None)
            else:
                if discipline in TYPE_DISCIPLINES and \
                        self.shared_data.dict_count_disc_type[day][group] == TYPE_DISCIPLINES[discipline]:
                    ret += self.PENALTY_WEIGHT
                else:
                    self.shared_data.dict_count_disc_type[day][group] = TYPE_DISCIPLINES.get(discipline, None)
        return ret

    def get_module_description(self) -> str:
        pass

    def get_module_naming(self) -> str:
        return "Чередование уроков по типу"

    def change_shared_data(self) -> None:
        pass
