# import time
#
# a = [1, 2]
# b = (1, 2)
#
# start_time = time.time()
# for _ in range(1000000):
#     if tuple(a) == b:
#         pass
# print("--- %s seconds ---" % (time.time() - start_time))
#
# start_time = time.time()
# for _ in range(1000000):
#     if a == list(b):
#         pass
# print("--- %s seconds ---" % (time.time() - start_time))
from timetable_Genetic_Algorithm.fitness_func.ModuleRegistrationDecorator import ModuleRegistrationDecorator


@ModuleRegistrationDecorator
class One:
    pass


class Two:
    pass


ModuleRegistrationDecorator.get_list_names()