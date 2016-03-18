class AbstractPolicy:

    def evaluate(self):
        return self.evaluate(None, None)

    def evaluate(self, observation_list):
        return self.evaluate(observation_list, None)

    def evaluate(self, observation_list, state_function):
        """
        Choose an action from the given set of possibilities.
        :param observation_list: A list of experiences, which helps to choose.
        :param state_function: It "converts" an observation to a state
        :return: An action if it can be evaluated, or None if not.
        """
        raise "Evaluation not implemented yet!"

    def improve(self, state1, action, state2, reward):
        """
        Improve the policy by the given parameters.
        :param state1: The state before the action
        :param action: Action which fired in state represented by the first parameter.
        :param state2: State after the action fired.
        :param reward: This is the reward (feedback) from the environment.
        :return: None
        """
        raise "This policy can not improved!"


class ImprovementPolicy(AbstractPolicy):

    def evaluate(self, observation_list, state_function):
        return True


class GreedyPolicy(AbstractPolicy):
    # TODO: Implement Greedy!
    def evaluate(self, observation_list, state_function):
        return super().evaluate(observation_list, state_function)


class EpsilonGreedyPolicy(GreedyPolicy):

    def evaluate(self, observation_list, state_function):
        return super().evaluate(observation_list, state_function)


class PolicyImplementation:

    def __init__(self):
        self._action_table = {}
        self._current_state = None
        self._action = None
        self._last_action = None

    @staticmethod
    def _evaluate_state(observation):
        # figure out the state from the observation
        return int(observation)

    def evaluate(self, observation):
        # get state from observation
        self._current_state = self._evaluate_state(observation)

        # save state
        self._last_action = self._action

        # list the possible actions
        if self._current_state in self._action_table:
            possible_actions = self._action_table[self._current_state]
        else:  # we can't to anything
            self._action = None
            return None

        # choose the best - or not always the best...
        self._action = max(possible_actions, key=lambda x: possible_actions[x])

        return self._action

    def improve(self, reward, actions):
        # if has not been in the _current_state before, than we add possible actions with 0.5 probability and return
        if self._current_state not in self._action_table:
            self._action_table[self._current_state] = {}
            for action in actions:
                self._action_table[self._current_state][action] = 0.5

        # update the policy IF we done something
        if self._action is not None:
            self._action_table[self._current_state][self._last_action] = reward  # ???
