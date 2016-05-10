from collections import defaultdict
from itertools import product


class Architecture:
    def __init__(self):
        self._manipulators = {}

    def get_actions(self):
        """
        Gives the Descartes product of all the possible values of all manipulators
        :return: list of possible actions as a dict
        """
        interpretation_intervals = {k: self._manipulators[k].get_interpretation_interval() for k in self._manipulators}
        return [dict(zip(interpretation_intervals, v)) for v in product(*interpretation_intervals.values())]

    def interact(self, action_vector):
        """
        Apply the action on the environment represented by the action vector.
        :param action_vector: a dict with a legal value for each manipulator of the Architecture
        :return: an (observation, reward) tuple, where the observation is always None, and the reward (at this point
            rather than result than reward) is a dict with the manipulator names.
        """
    #    if len(action_vector) != len(self._manipulators):
    #        raise ValueError
        try:
            m = self._manipulators
            return None, {name: m[name].get_action_handler(action_vector[name])() for name in m}
        except (KeyError, ValueError):
            print('Action vector does not fit for the manipulators!')
            raise


class WoodCutter(Architecture):

    def __init__(self, forest_environment):
        super().__init__()

        # save the environment for later... (it might be not necessary)
        self.forest = forest_environment

        # add a manipulators
        gardener = DiscreteActionHandler()
        gardener.set_action_handler('wait', forest_environment.wait_one_more_year)
        gardener.set_action_handler('cut_and_plant', forest_environment.cut_down_trees)
        self._manipulators['gardener'] = gardener

    def interact(self, action_vector):
        """
        Observes the environment after executes the action in the parameter.
        :param action_vector: tuple of action indexes indexed by manipulator ID's, which a "composite" action.
        :return: observation of the environment, and the reward
        """
        _, result = super().interact(action_vector)
        return self.forest.tree_age, result['gardener']  # tree age is the observation

    def initial_state(self):
        return self.forest.tree_age


class MazeMan(Architecture):
    # TODO: implement MazeMan architecture!

    def __init__(self, maze):

        super().__init__()
        self.maze = maze

    def interact(self, action_vector):
        # interact with the environment
        _, result = super().interact(action_vector)

        # get the results
        position, view = result['walk']

        # update manipulator
        walker = DiscreteActionHandler()
        if view['up'] is 1:
            walker.set_action_handler('up', lambda: self.maze.step('up'))
        if view['down'] is 1:
            walker.set_action_handler('down', lambda: self.maze.step('down'))
        if view['left'] is 1:
            walker.set_action_handler('left', lambda: self.maze.step('left'))
        if view['right'] is 1:
            walker.set_action_handler('right', lambda: self.maze.step('right'))
        self._manipulators['walk'] = walker

        # calculate reward
        reward = 0
        if position['x'] == 1 and position['y'] == 9:  # are we in the finish?
            reward = 10

        return position, reward

    def get_actions(self):

        return super().get_actions()

    def initial_state(self):

        position, _ = self.maze.step(None)
        return position


class DiscreteActionHandler:
    def __init__(self):
        self._action_table = defaultdict(lambda: lambda: print("Unimplemented action!"))

    def get_action_handler(self, action_name):
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


