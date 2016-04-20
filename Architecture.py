class Architecture:
    def observe(self, environment):
        """
        With the given sensors get and return with data from the environment
        :param environment: for observation
        :return:
        """
        pass

    def execute(self, environment, action):
        """
        Executes the given action in the environment
        :param environment: here will executed the action
        :param action: it will executed in the environment
        :return:
        """
        pass


class WoodCutter(Architecture):
    def observe(self, forest_environment):
        return forest_environment.tree_age

    def execute(self, forest_environment, action):
        if action is 0:
            return forest_environment.wait_one_more_year()
        if action is 1:
            return forest_environment.cut_down_trees()
