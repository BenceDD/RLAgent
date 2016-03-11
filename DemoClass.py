class Environment:
    pass


class Policy:
    pass


class EnvironmentImplementation(Environment):

    def __init__(self):
        # sample data...
        self._internal_state = 4
        self._description = ['partially observable', 'deterministic', 'episodic', 'static', 'discrete']
        self._actions = ['left', 'right', 'up', 'down']

    def get_environment_description(self):
        return self._description

    def observe(self):
        # a list describe the internal state, a reward for the last experiment, and the actions for next
        return self._internal_state/2,  1, self._actions

    def apply_action(self, action):
        self._internal_state += action


class PolicyImplementation(Policy):

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


class TDAgent:

    def __init__(self):
        self._improvement_policy_state = True

    @staticmethod
    def _choose_policy(environment_description):
        # determine which policy should be used depending on what we know about the environment
        if 'discrete' in environment_description:
            return PolicyImplementation()

    def _improvement_policy(self):
        return self._improvement_policy_state

    def create_policy(self, environment, until):
        # get the details of the environment
        description = environment.get_environment_description()

        # initialize policy
        policy = TDAgent._choose_policy(description)

        # improve the policy, until is't become enough good...
        for i in range(0, until):
            # observe the environment: it contains all the observable data, and the reward for the last experiment
            # in the available_actions the environment should pass that what actions can be applied in a situation
            observation, reward, available_actions = environment.observe()
            action = policy.evaluate(observation)

            if self._improvement_policy():  # how often should we improve?
                policy.improve(reward, available_actions)

            if action is not None:  # if we don't know what to do, maybe later
                environment.apply_action(action)

        return policy


agent = TDAgent()
e = EnvironmentImplementation()
p = agent.create_policy(e, 1)
