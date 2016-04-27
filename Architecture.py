from collections import defaultdict


class WoodCutter():

    def __init__(self, forest_environment):
        self.manipulators = {}
        plant_action = DiscreteActionHandler('Plant')
        plant_action.set_action_handler(0, forest_environment.wait_one_more_year)
        plant_action.set_action_handler(1, forest_environment.cut_down_trees)
        self.manipulators['plant'] = plant_action

    def interact(self, forest_environment, action):
        for part_action in action:
            
            reward = self.manipulators[action]

        return forest_environment.tree_age, reward


class DiscreteActionHandler:
    def __init__(self, name):
        self.name = name
        self._action_table = defaultdict(lambda: lambda: print("Unimplemented action!"))

    def sample(self, action_name):
        return self._action_table[action_name]

    def set_action_handler(self, action_name, action_handler):
        self._action_table[action_name] = action_handler

    def get_interpretation_interval(self):
        return self._action_table.keys()


class ContinuousActionHandler:
    def __init__(self, name, resolution):
        self.name = name
        self.resolution = resolution
        self._action_table = defaultdict(lambda: lambda: print("Unimplemented action!"))

    def sample(self, sample_point):
        for points in self.get_interpretation_interval():
            (begin, end) = points
            if begin < sample_point < end:
                return self._action_table[points]

    def set_action_handler(self, interval, action_handler):
        # interval is a tuple
        (begin, end) = interval
        if end < begin:
            raise Exception("Starting point of interval must be lower than ending point!")

        for i in self._action_table:
            if i.begin <= interval.end or interval.begin <= i.end:
                raise Exception("Intervals shouldn't overlap each other!")

        self._action_table[interval] = action_handler

    def get_interpretation_interval(self):
        return {range(i[0], i[1], self.resolution) for i in self._action_table}


handler = ContinuousActionHandler("szintszabalyozo", 0.5)
handler.set_action_handler((2, 6), lambda: print('say hello'))

print(handler.get_interpretation_interval())
