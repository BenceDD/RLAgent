from collections import defaultdict


class TrainingFunction:
    def improve(self, function_representation, additional_information):
        function_representation.improve(self, additional_information)


class TDLearn(TrainingFunction):

    def __init__(self, braveness_factor, discount_factor):
        self._braveness = braveness_factor
        self._discount = discount_factor
        self._N = {}

    def improve_table(self, table_representation, additional_information):
        # TODO: history will be the parameter!
        utility = table_representation.data
        (last_state, last_action, reward, state, action) = additional_information

        if state not in utility:
            utility[state] = reward
        if last_state is not None:
            self._N[last_state] += 1
            utility[last_state] += self._braveness * self._N[last_state] * (
                reward + self._discount * utility[state] - utility[last_state])


class QLearn(TrainingFunction):

    def __init__(self, learning_rate, discount_factor):
        self.lr = learning_rate
        self.discount = discount_factor

    def improve_table(self, table_representation, additional_information):
        # TODO: history will be the parameter!
        (s, a, r, s_new, a_new) = additional_information
        q = table_representation.data
        print("Before improvement: " + str(q[s][a]))
        q[s][a] = (1 - self.lr) * q[s][a] + self.lr * (r + self.discount * q[s_new][max(q[s_new])])
        print("After improvement: " + str(q[s][a]))

    def improve_network(self, func):
        print("A network improved by QLearn")


class Table:
    def __init__(self):
        self.data = []

    def improve(self, training_function, additional_information):
        training_function.improve_table(self, additional_information)

    def add(self, place, item):
        if isinstance(item, dict) is False:
            raise ValueError
        self.data[place] = {**self.data[place], **item}

    def get(self, place):
        return self.data[place]

    def push(self, item):
        if isinstance(item, dict) is False:
            raise ValueError
        self.data.append(item)

    def length(self):
        return len(self.data)


class NeuralNetwork:
    def improve(self, training_function, additional_information):
        training_function.improve_network(self, additional_information)

