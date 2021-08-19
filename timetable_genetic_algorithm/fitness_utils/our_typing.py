from typing import Type, List

from timetable_genetic_algorithm.fitness_utils.module_for_fitness_function_base import ModuleForFitnessFunctionBase

Timeline = int
DayOfWeek = int
AmountMentions = int
NumberLessons = List[int]
Discipline = str
TypeDiscipline = str
Pedagog = str
Rule = str
ModuleName = Type[ModuleForFitnessFunctionBase] or str
