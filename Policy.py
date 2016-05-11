from TrainingFunction import Table
import random


class Policy:
    def evaluate(self, actions):
        self.evaluate(actions, None)

    def evaluate(self, actions, history):
        """
        Calculate the probability of the actions got.
        :param actions: represents the known distribution of the actions
        :param history: this is all we already know, this can be used for the evaluation
        :return: the modified distribution
        """
        raise Exception('Evaluation not implemented yet!')


class GreedyPolicy(Policy):
    """ This policy choose the best from the available actions from the given context"""

    @staticmethod
    def probability(action, best_actions):
        if action in best_actions:
            return 1 / len(best_actions)  # determine the number of maximal values
        else:
            return 0

    def evaluate(self, actions):
        # get the key(s) of the maximal value(s)
        best_actions = [k for k in actions if actions[k] is max(actions.values())]
        # calculate the distribution
        return {a: GreedyPolicy.probability(a, best_actions) for a in actions}


class EpsilonGreedy(Policy):

    def __init__(self, epsilon, regression):
        """
        :param epsilon: probability of not following the Greedy Policy
        :param regression: this is added to each probability before normalization
        """
        self.epsilon = epsilon
        self.regression = regression
        self.greedy = GreedyPolicy()

    def evaluate(self, actions):

        if random.random() < self.epsilon:
            # add epsilon to each probability
            actions = {x: actions[x] + self.epsilon for x in actions}
            # calculate the length for the normalization
            s = sum(actions.values())
            # normalize and return
            return {x: actions[x] / s for x in actions}

        else:  # normal way by the Greedy
            return self.greedy.evaluate(actions)


class AgentFunction:

    def __init__(self, knowledge_representation):

        self.policy = None              # RLAgent set it!
        self.training_method = None     # RLAgent set it!
        self.history = Table()
        self.knowledge = None

    @staticmethod
    def choose(actions):
        tmp = 0
        r = random.random()
        for k in actions:
            if tmp + actions[k] > r:
                return k
            else:
                tmp += actions[k]

    def improve(self, reward):
        self.history.add(-1, {'r': reward})

        if self.action is None:  # TODO: is it necessary to return with none?
            print("[AgentFunction] Action is none, return...")
            return

        self.training_method.improve(self.history)

    def evaluate(self, state, actions):
        # update history
        if self.history.length() != 0:  # if this is the first time, there is no previous
            self.history.add(-1, {'s_new': state})
        self.history.push({'s': state})

        # modify the distribution by the policies
        actions = self.policy.evaluate(actions)
        # choose (draw) next action
        action = AgentFunction.choose(actions)
        # before return (after added a new line, -1. element is the new one)
        self.history.add(-1, {'a': action})
        return action

