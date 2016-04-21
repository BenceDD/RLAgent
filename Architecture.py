class WoodCutter:

    def interact(self, forest_environment, action):
        reward = None
        if action is 0:
            reward = forest_environment.wait_one_more_year()
        if action is 1:
            reward = forest_environment.cut_down_trees()

        return forest_environment.tree_age, reward
