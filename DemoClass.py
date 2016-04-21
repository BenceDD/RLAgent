from Policy import *
from Architecture import *
from Environment import *


class RLAgent:

    def __init__(self, environment, architecture):
        self.environment = environment
        self.architecture = architecture
        self.agent_function = AgentFunction()

    def train(self, policy, learning_function, iteration_limit):
        self.agent_function.set_improvement_properties(policy, learning_function)

        action = None
        for i in range(0, iteration_limit):

            observation, reward = self.architecture.interact(self.environment, action)
            self.agent_function.improve(action, reward)

            action = self.agent_function.evaluate(observation)

        return self.agent_function

    @staticmethod
    def td_train(q_table, action, reward):
        pass


env = WoodCutterEnvironment()
arch = WoodCutter()
agent = RLAgent(env, arch)
agent.train(GreedyPolicy(), RLAgent.td_train, 10)
