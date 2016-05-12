from collections import defaultdict
import random


class TrainingFunction:
    def improve(self, function_representation, additional_information):
        function_representation.improve(self, additional_information)

    @staticmethod
    def random_distribution(length):
        result = [random.random() for _ in range(0, length)]
        s = sum(result)
        return [result[i] / s for i in range(0, length)]


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

    def improve_table(self, table, additional_information):
        # TODO: history will be the parameter!
        if len(additional_information) < 3:
            return

        s = Table.to_key(additional_information[-2]['s'])
        a = Table.to_key(additional_information[-2]['a'])
        r = additional_information[-2]['r']
        s_new = Table.to_key(additional_information[-2]['s_new'])

        q = table.data
        q[s][a] = (1 - self.lr) * q[s][a] + self.lr * (r + self.discount * q[s_new][max(q[s_new])])

    def improve_network(self, func):
        print("A network improved by QLearn")


class Table:
    def __init__(self):
        self.data = {}

    def improve(self, training_function, additional_information):
        training_function.improve_table(self, additional_information)

    @staticmethod
    def to_key(key_candidate):
        return tuple(sorted(key_candidate.items()))

    def update_actions(self, state, actions):
        state = Table.to_key(state)
        if state not in self.data:
            # get random distribution for the new actions
            distribution = TrainingFunction.random_distribution(len(actions))
            self.data[state] = {Table.to_key(actions[i]): distribution[i] for i in range(0, len(actions))}
        else:
            # calculate the difference, and set 0 probability for each
            difference = {}
            for i in range(0, len(actions)):
                key = Table.to_key(actions[i])
                if key not in self.data:
                    difference[key] = 0.0
            # merge the new actions
            self.data[state] = {**self.data[state], **difference}
        return self.data[state]


class NeuralNetwork:
    def improve(self, training_function, additional_information):
        training_function.improve_network(self, additional_information)

    def update_actions(self, state, actions):
        pass

