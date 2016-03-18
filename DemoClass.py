from Policy import *
from Environment import EnvironmentImplementation


class TDAgent:

    def __init__(self):
        self._improvement_policy = ImprovementPolicy();

    @staticmethod
    def _choose_policy(environment_description):
        # determine which policy should be used depending on what we know about the environment
        if 'discrete' in environment_description:
            return PolicyImplementation()

    def train_policy(self, environment, until):
        # get the details of the environment
        description = environment.get_environment_description()

        # initialize policy
        trainee = TDAgent._choose_policy(description)

        # improve the policy, until is't become enough good...
        for i in range(0, until):
            # observe the environment: it contains all the observable data, and the reward for the last experiment
            # in the available_actions the environment should pass that what actions can be applied in a situation
            observation = environment.observe()
            action = trainee.evaluate(observation)

            if self._improvement_policy.evaluate() is True:  # how often should we improve?
                trainee.improve(observation['reward'], available_actions)

            if action is not None:  # if we don't know what to do, maybe later
                environment.apply_action(action)

        return trainee


agent = TDAgent()
e = EnvironmentImplementation()
p = agent.train_policy(e, 1)
