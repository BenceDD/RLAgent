from TrainingFunction import Table


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
    """ This policy choose the best from the available actions for the LAST state """

    def __init__(self):
        self.U = Table()

    def evaluate(self, observation, action):
        # get all actions which can be performed in a state
        actions = self.U.data[observation]
        # get the key(s) of the maximal value(s)
        max_values = [k for k in actions if actions[k] is max(actions.values())]
        if action in max_values:
            return 1 / len(max_values)  # determine the number of maximal values
        else:
            return 0

    def improve(self, training, last_observation, observation, reward):
        training.improve(self.U, last_observation, observation, reward)


class AgentFunction:

    def __init__(self):
        """
        The training policy and the learning method for this policy (for a session) which currently
        belongs to the implementation of the policy
        """
        self.policy = None  # RLAgent set it!
        self.training_method = None  # RLAgent set it!
        self._last_observation = None

    def improve(self, observation, action, reward):
        self.policy.improve(self.training_method, self._last_observation, observation, reward)

    def evaluate(self, observation, actions):
        self._last_observation = observation  # assume that we call evaluate first!
        for action in actions:
            if self.policy.evaluate(observation, action) is not 0:
                return action

