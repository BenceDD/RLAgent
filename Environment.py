class Environment:
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
