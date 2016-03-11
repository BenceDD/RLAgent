class Environment:
    pass


class Policy:
    pass


class EnvironmentImplementation:

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


class PolicyImplementation:

    def __init__(self):
        self._action_table = {}
        self._action_list = set()
        self._current_state = None
        self._last_action = None

    @staticmethod
    def _evaluate_state(observation):
        # figure out the state from the observation
        return observation

    def _update_action_list(self, actions):
        self._action_list.add(actions)

    def improve(self, reward, actions):
        if (self._current_state or self._last_action) is None:
            return  # because we are not able to learn...

        # check if we are new possibilities to do (somehow...)
        self._update_action_list(actions)

        # update the policy
        self._action_table[(self._current_state, self._last_action)] = reward  # ???

        # clean up
        self._last_action = None  # we already learned from this!

    def evaluate(self, observation):
        # get state from observation
        self._current_state = self._evaluate_state(observation)

        # list the possible actions
        possible_actions = self._action_table[self._current_state]

        # choose the best - or not always the best...
        action = max(possible_actions, key=lambda x: possible_actions[x])

        # save action for future improvement
        self._last_action = action

        return action


class TDAgent:

    @staticmethod
    def _choose_policy(environment_description):
        # determine which policy should be used depending on what we know about the environment
        if 'discrete' in environment_description:
            return PolicyImplementation()

    @staticmethod
    def create_policy(environment):
        # get the details of the environment
        description = environment.get_environment_description()

        # initialize policy
        policy = TDAgent._choose_policy(description)

        # improve the policy, until is't become enough good...
        for i in range(0, 100):
            # observe the environment: it contains all the observable data, and the reward for the last experiment
            # in the available_actions the environment should pass that what actions can be applied in a situation
            observation, reward, available_actions = environment.observe()
            policy.improve(reward, available_actions)
            action = policy.evaluate(observation)
            environment.apply_action(action)

        return policy


agent = TDAgent()
e = EnvironmentImplementation()
p = agent.create_policy(e)
