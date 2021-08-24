from timetable_genetic_algorithm.fitness_modules import constants_weight
from timetable_genetic_algorithm.fitness_utils import module_register, ModuleForFitnessFunctionBase
from timetable_genetic_algorithm.utils import MAX_LESSONS_IN_DAY
from timetable_genetic_algorithm.utils.settings_generations import AMOUNT_TIMELINES_IN_DAY


@module_register
class GroupsNumLesson(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = constants_weight.FIRST_LESSON_GROUP

    def get_fitness_penalty(self) -> int:
        timeline = self.shared_data.current_timeline % AMOUNT_TIMELINES_IN_DAY
        ret = 0
        if self.shared_data.current_lesson:
            if self.shared_data.current_lesson[4] > timeline or timeline > self.shared_data.current_lesson[4] \
                    + MAX_LESSONS_IN_DAY[self.shared_data.current_lesson[0][0]]:
                ret += self.PENALTY_WEIGHT
        return ret

    def get_module_description(self) -> str:
        pass

    def get_module_naming(self) -> str:
        return "Проверка номера первого урока и общего количества уроков в день"

    def change_shared_data(self) -> None:
        pass

