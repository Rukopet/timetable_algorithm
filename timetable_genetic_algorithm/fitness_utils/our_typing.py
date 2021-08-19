from typing import Type

from timetable_genetic_algorithm.fitness_utils.module_for_fitness_function_base import ModuleForFitnessFunctionBase

Rule = str
ModuleName = Type[ModuleForFitnessFunctionBase] or str
