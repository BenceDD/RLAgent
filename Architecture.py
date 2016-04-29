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
        """
        Get the action for the execution by index/id.
        :param action_name: Action index/id
        :return: The action with the given name
        """
        return self._action_table[action_name]

    def set_action_handler(self, action_name, action_handler):
        """
        Set action for an action ID.
        :param action_name: Index on the action
        :param action_handler: A function which has to be executed for the given action ID/index
        :return: None
        """
        self._action_table[action_name] = action_handler

    def get_interpretation_interval(self):
        """
        Returns all the possible action ID's.
        :return: List of possible keys
        """
        return self._action_table.keys()


class ContinuousActionHandler:
    def __init__(self, name, resolution):
        """
        Makes a new manipulator with continuous interpretation range
        :param name: name of the manipulator, should be unique for the architecture instance
        :param resolution: sampling resolution of the function
        """
        self.name = name
        self.resolution = resolution
        self._action_table = defaultdict(lambda: lambda: print("Unimplemented action!"))

    def sample(self, sample_point):
        for points in self.get_interpretation_interval():
            (begin, end) = points
            if begin < sample_point < end:
                return self._action_table[points]

    def set_action_handler(self, interval, action_handler):
        """
        Set action for an interval.
        :param interval: tuple of integers
        :param action_handler: a function
        :return:
        """
        (begin, end) = interval
        if end < begin:
            raise Exception("Starting point of interval must be lower than ending point!")

        for i in self._action_table:
            (i_begin, i_end) = i
            if i_begin <= interval.end or interval.begin <= i_end:
                raise Exception("Intervals shouldn't overlap each other!")

        self._action_table[interval] = action_handler

    def get_interpretation_interval(self):
        for begin, end in self._action_table:
            for


handler = ContinuousActionHandler("szintszabalyozo", 0.5)
handler.set_action_handler((2, 6), lambda: print('say hello'))

print(handler.get_interpretation_interval())
