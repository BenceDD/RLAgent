from FunctionArchitecture import TablePolicyFunction


class Policy:
    """ A probability over the actions """

    def evaluate(self, state):
        raise Exception("Evaluation is not implemented yet!")

    def improve(self, action, result):
        raise Exception("Improvement is not implemented yet!")


class GreedyPolicy(Policy):
    """ This policy choose the best from the available actions for the LAST state """

    def __init__(self):
        self.Q = TablePolicyFunction()

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


class AgentFunction:

    def __init__(self):
        self.policy = None
        self.training_method = None

    def set_improvement_properties(self, policy, training_method):
        self.policy = policy
        self.training_method = training_method

    def improve(self, action, reward):
        pass

    def evaluate(self, observation):
        return observation

