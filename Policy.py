import copy
import random


class Policy:

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

    def evaluate(self, actions, history):
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

    def evaluate(self, actions, history):

        if random.random() < self.epsilon:
            # add epsilon to each probability
            actions = {x: actions[x] + self.epsilon for x in actions}
            # calculate the length for the normalization
            s = sum(actions.values())
            # normalize and return
            return {x: actions[x] / s for x in actions}

        else:  # normal way by the Greedy
            return self.greedy.evaluate(actions, None)


class AgentFunction:

    def __init__(self, knowledge_representation):

        self.policy = None              # RLAgent set it!
        self.training_method = None     # RLAgent set it!
        self.history = []
        self.knowledge = knowledge_representation

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
        # add reward to the history
        self.history[-1]['r'] = copy.deepcopy(reward)
        self.training_method.improve(self.knowledge, self.history)

    def evaluate(self, state, new_actions):
        # update history
        if len(self.history) != 0:  # if this is the first time, there is no previous
            self.history[-1]['s_new'] = copy.deepcopy(state)
        else:
            self.history.append({'s_new': copy.deepcopy(state)})
        self.history.append({'s': copy.deepcopy(state)})

        # add the new actions for the knowledge base
        actions = self.knowledge.update_actions(state, new_actions)
        # modify the distribution by the policies
        actions = self.policy.evaluate(actions, None)
        # choose (draw) next action
        action = AgentFunction.choose(actions)

        action = dict(action)  # TODO: this is not nice..
        # before return (after added a new line, -1. element is the new one)
        self.history[-1]['a'] = copy.deepcopy(action)
        return action
