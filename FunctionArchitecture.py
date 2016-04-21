from collections import defaultdict


class ImprovableFunction:
    pass


class TablePolicyFunction(ImprovableFunction):

    def __init__(self):
        self._table = defaultdict(lambda: defaultdict(lambda: 0))

    def define(self, state, action, value):
        self._table[state][action] = value

    def eval(self, state, action):
        return self._table[state][action]


class TensorFlowNeuralNetwork(ImprovableFunction):
    """
    Use the TF implementation with the policy interface
    """
    pass
