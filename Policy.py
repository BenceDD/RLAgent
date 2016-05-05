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
    def evaluate(context, action):
        """
        :param context: an array where the policy choose the best from
        :param action: the action of the (state)context which has to be evaluated
        :return: the probability of the given action by the policy
        """
        # get the key(s) of the maximal value(s)
        max_values = [k for k in context if context[k] is max(context.values())]

        print("[GreedyPolicy] The context and values are:")
        for item in context:
            print(context[item])
        print("[GreedyPolicy] context end.")

        if action in max_values:
            return 1 / len(max_values)  # determine the number of maximal values
        else:
            return 0


class EpsilonGreedy:

    def __init__(self, epsilon):
        self.epsilon = epsilon

    def evaluate(self, context, action):
        if random.random() < self.epsilon:
            return random.choice(context)
        else:
            return GreedyPolicy.evaluate(context, action)


class AgentFunction:

    def __init__(self):

        self._knowledge = Table()       # TODO: this is implied by the training method! And not a common name...
        self.policy = None              # RLAgent set it!
        self.training_method = None     # RLAgent set it!

        # represents the local history
        self.state = None
        self.action = None
        self.last_state = None
        self.last_action = None

    def improve_dummy(self, actions):
        for i in range(0, 10):
            for a in actions:
                self._knowledge.data[i][a] = random.random()

    def improve(self, reward):
        # add the local history to the improvement as an additional information
        if self.action is None:
            print("[AgentFunction] Action is none, return...")
            return

        # TODO: this is a piece of shit!
        self.training_method.improve_table(self._knowledge,
                                           (self.last_state, self.last_action, reward, self.state, self.action))

    def evaluate(self, state, actions):  # this is called second!
        # back up the state...
        self.last_state = self.state
        self.last_action = self.action
        self.state = state

        state_knowledge = self._knowledge.data[state]

        # TODO: Epsilon Greedy: should not be here!
        if len(actions) != 0 and random.random() < 0.1:
            action = random.choice(actions)
            if action not in state_knowledge:
                state_knowledge[action] = random.random()
            return action

        for action in actions:  # evaluate the policy to choose an action

            if action not in state_knowledge:
                state_knowledge[action] = random.random()

            print("[AgentFunction] Evaluate action: " + str(action))

            if self.policy.evaluate(state_knowledge, action) is not 0:

                print("[AgentFunction] Action selected!")
                self.action = action
                return self.action

        print("[AgentFunction] There is no action selected!! Error!!")
