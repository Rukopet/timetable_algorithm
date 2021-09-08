from timetable_genetic_algorithm.fitness_modules import constants_weight
from timetable_genetic_algorithm.fitness_utils import ModuleForFitnessFunctionBase, module_register


@module_register
class AudienceHardLink(ModuleForFitnessFunctionBase):
    PENALTY_WEIGHT = constants_weight.AUDIENCE_HARD_LINK

    def get_fitness_penalty(self) -> int:
        ret = 0
        audience = self.shared_data.current_audience
        if self.shared_data.current_lesson:
            group = self.shared_data.current_lesson[0]
            discipline = self.shared_data.current_lesson[1]
            if audience and audience[1] == 3:
                if discipline not in self.settings.DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK or \
                        group not in self.settings.DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK or \
                        discipline in self.settings.DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK and \
                        self.settings.DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK[discipline] != audience[0] or \
                        group in self.settings.DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK and \
                        self.settings.DISCIPLINES_GROUPS_FOR_AUDIENCE_LINK[group] != audience[0]:
                    ret += self.PENALTY_WEIGHT
            elif group in self.settings.GROUPS_AUDIENCE_LINK:
                if audience[0] not in self.settings.GROUPS_AUDIENCE_LINK[group]:
                    ret += self.PENALTY_WEIGHT
            elif discipline in self.settings.DISCIPLINES_AUDIENCE_LINK:
                if audience[0] not in self.settings.DISCIPLINES_AUDIENCE_LINK[discipline]:
                    ret += self.PENALTY_WEIGHT
        return ret

    def get_module_description(self) -> str:
        pass

    def get_module_naming(self) -> str:
        return "Проверка жесткой связи аудитории с группами и дисциплинами"

    def change_shared_data(self) -> None:
        pass
