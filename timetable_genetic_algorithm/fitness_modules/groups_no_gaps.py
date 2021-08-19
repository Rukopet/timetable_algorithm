from timetable_genetic_algorithm.fitness_utils import ModuleForFitnessFunctionBase, module_register


@module_register
class GroupsNoGaps(ModuleForFitnessFunctionBase):
    def get_fitness_penalty(self):
        """
         Groups fitness function for check of no windows in each Group schedule

        :param lesson: tuple
        :param timeline: int
        :return: None
        """
        day = timeline // AMOUNT_TIMELINES_IN_DAY
        time = timeline % AMOUNT_TIMELINES_IN_DAY

        if lesson:
            if day in self.dict_count_group_windows.keys():
                if lesson[0] in self.dict_count_group_windows[day].keys():
                    if time > self.dict_count_group_windows[day][lesson[0]] \
                            [len(self.dict_count_group_windows[day][lesson[0]]) - 1]:
                        self.count_group_error_window += (time - self.dict_count_group_windows[day][lesson[0]] \
                            [len(self.dict_count_group_windows[day][lesson[0]]) - 1] - 1) * WINDOWS_GROUP
                        self.dict_count_group_windows[day][lesson[0]].append(time)
                else:
                    self.dict_count_group_windows[day][lesson[0]] = [time]
            else:
                self.dict_count_group_windows[day] = {lesson[0]: [time]}

    def get_module_description(self):
        pass

    def get_module_naming(self):
        pass
