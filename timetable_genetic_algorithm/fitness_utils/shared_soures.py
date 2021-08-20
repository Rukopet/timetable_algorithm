from dataclasses import dataclass
from typing import List, Dict

from timetable_genetic_algorithm.fitness_utils.our_typing import Rule, ModuleName, Timeline, Pedagog, AmountMentions, \
    NumberLessons, DayOfWeek, Discipline, TypeDiscipline
from timetable_genetic_algorithm.utils.our_typing import Group


@dataclass
class SharedData:
    """
    Dataclass that will be in all other modules classes

    """

    # Rule = str
    all_rules: List[Rule]
    # global_rules_matrix: Dict[Rule, bool]
    # current_rules_matrix: Dict[Rule, bool]

    dict_count_pedago_nosingle: Dict[Timeline, Dict[Pedagog, AmountMentions]]
    # dict_count_group_nosingle: Dict[Timeline, Dict[Group, AmountMentions]]
    # dict_count_pedago_windows: Dict[DayOfWeek, Dict[Pedagog, NumberLessons]]
    # dict_count_group_windows: Dict[DayOfWeek, Dict[Group, NumberLessons]]
    # dict_count_disc_name: Dict[DayOfWeek, Dict[Group, Discipline]]
    # dict_count_disc_type: Dict[DayOfWeek, Dict[Group, TypeDiscipline]]

    def is_current_module_need_check(self, module: ModuleName) -> bool:
        """
        Check need or not add penalty in current timeline.
        NOT CHECKED INPUT VALUE!

        :param module: any child class of IModuleForFitnessFunction or name module
        :return: True/False
        :raise: TypeError
        """

        if type(module) == str:
            rule_name = module
        else:
            rule_name = module.__name__

        if rule_name not in self.all_rules:
            err_msg = f'This class {rule_name}, not registered, in modules decorator'
            raise TypeError(err_msg)
        return self.current_rules_matrix[rule_name]
