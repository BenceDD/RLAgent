from collections import defaultdict


class Policy:
    @staticmethod
    def table_policy_function():
        return defaultdict(lambda: defaultdict(lambda: 0))

    @staticmethod
    def tensor_flow_neural_network():
        pass

    def evaluate(self, observation, action):
        raise Exception('Evaluation not implemented yet!')

    def improve(self, training_method, action, reward):
        raise Exception('Improvement not implemented yet!')


class GreedyPolicy(Policy):
    """ This policy choose the best from the available actions for the LAST state """

    def __init__(self):
        self.Q = self.table_policy_function()

    def evaluate(self, observation, action):
        actions = self.Q[observation]
        max_values = [k for k in actions if actions[k] is max(actions.values())]
        if action in max_values:
            return 1 / len(max_values)
        else:
            return 0

    def improve(self, training_method, action, reward):
        training_method(self.Q, action, reward)


class AgentFunction:

    def __init__(self):
        self.policy = None
        self.training_method = None

    def set_improvement_properties(self, policy, training_method):
        self.policy = policy
        self.training_method = training_method

    def improve(self, action, reward):
        self.policy.improve(self.training_method, action, reward)

    def evaluate(self, observation):
        # TODO: how to iterate on the all actions?
        return observation

