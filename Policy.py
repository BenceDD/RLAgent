from TrainingFunction import Table
import random


class Policy:
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


class GreedyPolicy:  # should it inherit from policy??
    """ This policy choose the best from the available actions from the given context"""

    @staticmethod
    def probability(action, best_actions):
        if action in best_actions:
            return 1 / len(best_actions)  # determine the number of maximal values
        else:
            return 0

    @staticmethod
    def evaluate(actions):
        """
        :param actions: array of actions
        :return: the distribution of the given actions by the policy
        """
        # get the key(s) of the maximal value(s)
        best_actions = [k for k in actions if actions[k] is max(actions.values())]
        # calculate the distribution
        return {(a, GreedyPolicy.probability(a, best_actions)) for a in actions}


class EpsilonGreedy:

    def __init__(self, epsilon):
        self.epsilon = epsilon

    def evaluate(self, actions):
        if random.random() < self.epsilon:
            return GreedyPolicy.evaluate(actions)  # TODO: it should modify the result of the GreedyPolicy
        else:
            return GreedyPolicy.evaluate(actions)


class AgentFunction:

    def __init__(self):

        self.knowledge = Table()       # TODO: this should come from TLAgent. And not a common name...
        self.policy = None              # RLAgent set it!
        self.training_method = None     # RLAgent set it!

        # TODO: infinite history!
        # represents the local history
        self.state = None
        self.action = None
        self.last_state = None
        self.last_action = None

        self.history = []

    def improve_dummy(self, states, actions):
        for s in states:
            for a in actions:
                self.knowledge.data[s][a] = random.random()

    def improve(self, reward):
        self.history[-1]['r'] = reward

        if self.action is None:  # TODO: is it necessary?
            print("[AgentFunction] Action is none, return...")
            return

        self.training_method.improve(self.knowledge, self.history)

    def evaluate(self, state, actions):  # this is called second!
        # create history
        if len(self.history) != 0:  # if this is the first time, there is no previous
            self.history[-1]['s_new'] = state
        self.history.append({'s': state, 'a': actions})

        for p in self.policy(self.knowledge.data[state]):
            # TODO: make a random choice depending on the (Epsilon)Greedy distribution
            action = p  # calculate...

            # before return (after added a new line, -1. element is the new one)
            self.history[-1]['a'] = None
            return action

