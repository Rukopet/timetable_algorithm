from timetable_genetic_algorithm.fitness_modules import constants_weight
from timetable_genetic_algorithm.fitness_utils import module_register, ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.utils.settings_generations import AMOUNT_TIMELINES_IN_DAY


@module_register
class DisciplineName(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = constants_weight.DISCIPLINES_NAME

    def get_fitness_penalty(self) -> int:
        time = self.shared_data.current_timeline % AMOUNT_TIMELINES_IN_DAY
        day = self.shared_data.current_timeline // AMOUNT_TIMELINES_IN_DAY
        ret = 0
        if self.shared_data.current_lesson:
            group = self.shared_data.current_lesson[0]
            discipline = self.shared_data.current_lesson[1]
            first_lesson = self.shared_data.current_lesson[4]
            if day not in self.shared_data.dict_count_disc_name:
                self.shared_data.dict_count_disc_name[day] = {}
            if time == first_lesson or group not in self.shared_data.dict_count_disc_name[day]:
                self.shared_data.dict_count_disc_name[day][group] = discipline
            else:
                if self.shared_data.dict_count_disc_name[day][group] == discipline:
                    ret += self.PENALTY_WEIGHT
                else:
                    self.shared_data.dict_count_disc_name[day][group] = discipline
        return ret

    def get_module_description(self) -> str:
        pass

    def get_module_naming(self) -> str:
        return "Чередование уроков по названию"

    def change_shared_data(self) -> None:
        pass


