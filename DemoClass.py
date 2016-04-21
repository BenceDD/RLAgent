from Policy import *
from Architecture import *
from Environment import *
from FunctionArchitecture import TablePolicyFunction


class RLAgent:

    def __init__(self, environment, architecture):
        self.environment = environment
        self.architecture = architecture
        self.agent_function = AgentFunction()

    def train(self, policy, learning_function, iteration_limit):
        action = None
        self.agent_function.set_improvement_properties(policy, learning_function)

        for i in range(0, iteration_limit):

            observation, reward = self.architecture.interact(self.environment, action)
            self.agent_function.improve(action, reward)

            action = self.agent_function.evaluate(observation)

        return self.agent_function

    @staticmethod
    def td_train():
        pass

"""
env = WoodCutterEnvironment()
arch = WoodCutter()
agent = RLAgent(env, arch)

agent.train(None, None, 10)
"""
tfi = TablePolicyFunction()
tfi.define('a', 'b', 34)
print(tfi.eval('a', 'b'))
print(tfi.eval('a', 'c'))
print(tfi.eval('d', 'b'))

