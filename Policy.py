class Policy:

    def evaluate(self, state):
        raise Exception("Evaluation is not implemented yet!")

    def improve(self, action, result):
        raise Exception("Improvement is not implemented yet!")


class GreedyPolicy(Policy):
    """ This policy choose the best from the available actions for the LAST state """
    # TODO: Implement Greedy!
    def evaluate(self, observation):
        # get the latest state, and choose the action from the possibilities which has the greatest expected value
        pass


class EpsilonGreedyPolicy(Policy):
    """ This policy policy use the GreedyPolicy according to a certain distribution """
    # TODO: Implement EpsilonGreedyPolicy!
    def __int__(self, probability):
        self._epsilon = probability
        self._greedy = GreedyPolicy()

    def evaluate(self, observation):
        # get a random number from {1 ... 1/epsilon} to choose if follow the GreedyPolicy or not.
        # then get an other for choose the action
        pass


class AgentFunction(Policy):
    def improve(self, last_action, reward):
        pass

    def evaluate(self, observation):
        return observation

