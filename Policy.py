class Policy:

    def evaluate(self, memory, state, actions):
        """
        Choose an action from the given set of possibilities.
        :param memory: This represent the knowledge (context)
        :param state: The state where we are in.
        :param actions: The possibilities.
        :return: An action if it can be evaluated, or None if not.
        """
        raise Exception("Evaluation is not implemented yet!")


class StatefulPolicy(Policy):

    def improve(self, memory):
        """
        Improve the policy by the memory
        :param memory: Stores all we already know.
        :return: None
        """
        raise Exception("Improvement is not implemented yet!")


class GreedyPolicy(Policy):
    """ This policy choose the best from the available actions for the LAST state """
    # TODO: Implement Greedy!
    def evaluate(self, memory, state, actions):
        # get the latest state, and choose the action from the possibilities which has the greatest expected value
        pass


class EpsilonGreedyPolicy(Policy):
    """ This policy policy use the GreedyPolicy according to a certain distribution """
    # TODO: Implement EpsilonGreedyPolicy!
    def __int__(self, probability):
        self._epsilon = probability
        self._greedy = GreedyPolicy()

    def evaluate(self, memory, state, actions):
        # get a random number from {1 ... 1/epsilon} to choose if follow the GreedyPolicy or not.
        # then get an other for choose the action
        pass


class TraineePolicy(StatefulPolicy):
    """ This is the policy for training """
    # TODO: Figure out how it's work!
    def __init__(self):
        self._evaluationPolicy = EpsilonGreedyPolicy()
        self._actionTable = {}

    def evaluate(self, memory, state, actions):
        if state is None or actions is None:
            return None
        # add all possible state-action pairs to actiontable with def value (add new if needed)
        # select all value with state
        # return _evaluationPolicy(None, state, selected_from_actiontable)

    def improve(self, memory):
        # update the actiontable following the state-action-rewards
        pass
