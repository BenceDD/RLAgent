from Policy import *
from Architecture import *
from Environment import *


class RLAgent:

    def __init__(self, environment, architecture):
        self.environment = environment
        self.architecture = architecture
        self.agent_function = AgentFunction()

    def train(self, learning_algorithm, exploration_function, iteration_limit):
        last_action = None

        for i in range(0, iteration_limit):
            observation, reward = self.architecture.observe(self.environment)
            self.agent_function.improve(learning_algorithm, last_action, reward)

            best_action = self.agent_function.evaluate(observation)
            next_action = exploration_function.evaluate(best_action)

            self.architecture.execute(self.environment, next_action)
            last_action = next_action

        return self.agent_function


env = WoodCutterEnvironment()
arch = WoodCutter()
agent = RLAgent(env, arch)

agent.train(None, None, 10)
