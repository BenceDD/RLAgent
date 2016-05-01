from collections import defaultdict


class TrainingFunction:
    def improve(self, function_representation):
        function_representation.improve(self)


class TDLearn(TrainingFunction):

    def __init__(self, braveness_factor, discount_factor):
        self._braveness = braveness_factor
        self._discount = discount_factor
        self._N = {}

    def improve_table(self, table_representation, last_state, state, reward):
        utility = table_representation.data
        if state not in utility:
            utility[state] = reward
        if last_state is not None:
            self._N[last_state] += 1
            utility[last_state] += self._braveness * self._N[last_state] * (
                reward + self._discount * utility[state] - utility[last_state])


class QLearn(TrainingFunction):
    def improve_table(self, func):
        print("A table improved by QLearn")

    def improve_network(self, func):
        print("A network improved by QLearn")


class Table:
    def __init__(self):
        self.data = defaultdict(lambda: defaultdict(lambda: 0))

    def improve(self, func_impl):
        func_impl.improve_table(self)


class NeuralNetwork:
    def improve(self, func_impl):
        func_impl.improve_network(self)

"""
table = NeuralNetwork()
td_learn = TDLearn()

td_learn.improve(table)
"""