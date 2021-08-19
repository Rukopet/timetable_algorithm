from dataclasses import dataclass
from typing import List, Dict

from timetable_genetic_algorithm.fitness_utils.our_typing import Rule, ModuleName


@dataclass
class SharedData:
    """
    Dataclass that will be in all other modules classes

    """

    # Rule = str
    all_rules: List[Rule]
    global_rules_matrix: Dict[Rule, bool]
    current_rules_matrix: Dict[Rule, bool]

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


# TODO remove debug code =>>
# dell = ["asd", "zxc"]
#
#
# class asd(ModuleForFitnessFunctionBase):
#     pass
#
#
# a = SharedData(dell, {i: True for i in dell}, {i: True for i in dell})
# print(a.is_current_module_need_check(asd))
# print(a)
