from timetable_genetic_algorithm.fitness_modules import constants_weight
from timetable_genetic_algorithm.fitness_utils import ModuleForFitnessFunctionBase, module_register


@module_register
class PedagogsUniqueness(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = constants_weight.NO_SINGLE_PEDAGOG

    def get_fitness_penalty(self) -> int:
        ret = 0
        if self.shared_data.current_lesson:
            if self.shared_data.current_timeline in self.shared_data.dict_count_pedago_nosingle:
                if self.shared_data.current_lesson[2] in \
                        self.shared_data.dict_count_pedago_nosingle[self.shared_data.current_timeline]:
                    self.shared_data.dict_count_pedago_nosingle[self.shared_data.current_timeline]\
                        [self.shared_data.current_lesson[2]] += 1
                    ret += self.PENALTY_WEIGHT
                else:
                    self.shared_data.dict_count_pedago_nosingle[self.shared_data.current_timeline]\
                        [self.shared_data.current_lesson[2]] = 1
            else:
                self.shared_data.dict_count_pedago_nosingle[self.shared_data.current_timeline] \
                    = {self.shared_data.current_lesson[2]: 1}
        return ret

    def get_module_description(self) -> str:
        pass

    def get_module_naming(self) -> str:
        return "Один урок - один педагог"

    def change_shared_data(self) -> None:
        pass
