from Policy import *
from Environment import *
from Memory import *


class TDAgent:

    def __init__(self):
        self._memory = Memory()

    def train_policy(self, environment, until):

        trainee = TraineePolicy()

        state = None
        actions = None

        for i in range(0, until):
            # it must return null if can't do anything
            action = trainee.evaluate(self._memory, state, actions)
            environment.apply_action(action)
            state_before = state
            state, actions, reward = environment.observe()
            self._memory.store((state_before, action, state, reward))
            trainee.improve(self._memory)
        return trainee


agent = TDAgent()
e = WoodCutterEnvironment()
agent.train_policy(e, 10)
