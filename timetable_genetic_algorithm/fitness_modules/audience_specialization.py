from timetable_genetic_algorithm.fitness_modules import constants_weight
from timetable_genetic_algorithm.fitness_utils import ModuleForFitnessFunctionBase, module_register


@module_register
class AudienceSpecialization(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = constants_weight.AUDIENCE_SPECIALIZATION

    def get_fitness_penalty(self) -> int:
        ret = 0
        audience = self.shared_data.current_audience
        if self.shared_data.current_lesson and audience and audience[0] in self.settings.AUDIENCE_PARAMS and \
                self.settings.AUDIENCE_PARAMS[audience[0]] is not None:
            dict_disc = {'discipline': self.shared_data.current_lesson[1]}
            dict_group = {'num': self.shared_data.current_lesson[0][0], 'letter': self.shared_data.current_lesson[0][1]}
            if audience[1] != 2:
                if dict_disc not in self.settings.AUDIENCE_PARAMS[audience[0]]:
                    ret += self.PENALTY_WEIGHT
            if audience[1] > 1:
                if dict_group not in self.settings.AUDIENCE_PARAMS[audience[0]]:
                    ret += self.PENALTY_WEIGHT
        return ret

    def get_module_description(self) -> str:
        pass

    def get_module_naming(self) -> str:
        return "Проверка специализации аудитории"

    def change_shared_data(self) -> None:
        pass
