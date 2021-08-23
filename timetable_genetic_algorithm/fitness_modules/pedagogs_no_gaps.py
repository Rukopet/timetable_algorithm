from timetable_genetic_algorithm.fitness_utils import ModuleForFitnessFunctionBase, module_register
from timetable_genetic_algorithm.fitness_modules import constants_weight


@module_register
class PedagogsNoGaps(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = constants_weight.WINDOWS_PEDAGOG

    def get_fitness_penalty(self) -> int:
        return 123

    def get_module_description(self):
        pass

    def get_module_naming(self) -> str:
        return "Отсутствие окон у педагога"

    def change_shared_data(self):
        pass
