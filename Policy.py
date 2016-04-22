from collections import defaultdict


class Policy:
    @staticmethod
    def table_policy_function():
        """ Returns a table for a 2 dim -> 1 dim (Q) function """
        return defaultdict(lambda: defaultdict(lambda: 0))

    @staticmethod
    def tensor_flow_neural_network():
        """ Returns a TF neural network """
        return None

    def evaluate(self, observation, action):
        """
        Get the probability of an action in the given state represented by the related observation
        :param observation: represents the state
        :param action: this action's probability will be returned
        :return: the probability of the action in the observed state
        """
        raise Exception('Evaluation not implemented yet!')

    def improve(self, training_method, action, reward):
        """
        Modifies the distribution of the preferred actions
        :param training_method: the distribution modification based on this function
        :param action: target for modification
        :param reward: change the distribution by this value
        :return:
        """
        raise Exception('Improvement not implemented yet!')


class GreedyPolicy(Policy):
    """ This policy choose the best from the available actions for the LAST state """

    def __init__(self):
        self.Q = self.table_policy_function()

    def evaluate(self, observation, action):
        # get all actions which can be performed in a state
        actions = self.Q[observation]
        # get the key(s) of the maximal value(s)
        max_values = [k for k in actions if actions[k] is max(actions.values())]
        if action in max_values:
            return 1 / len(max_values)  # determine the number of maximal values
        else:
            return 0

    def improve(self, training_method, action, reward):
        training_method(self.Q, action, reward)


class AgentFunction:

    def __init__(self):
        """
        The training policy and the learning method for this policy (for a session) which currently
        belongs to the implementation of the policy
        """
        self.policy = None
        self.training_method = None

    def improve(self, action, reward):
        self.policy.improve(self.training_method, action, reward)

    def evaluate(self, observation):
        # TODO: how to iterate on the all actions?
        actions = self.policy.Q[observation]
        for action in actions:
            if self.policy.evaluate(observation, action) is not 0:
                return action

