from Policy import *
from Architecture import *
from Environment import *
from TrainingFunction import *


class RLAgent:

    def __init__(self, environment, architecture):  # reward?
        self.environment = environment
        self.architecture = architecture
        self.agent_function = AgentFunction()

    def train(self, policy, learning_function, iteration_limit):
        # these can be set for a single training session
        self.agent_function.policy = policy
        self.agent_function.training_method = learning_function

        action = None
        for i in range(0, iteration_limit):
            # TODO: define reward here from the observation?
            observation, reward = self.architecture.interact(self.environment, action)
            # reward = observation['objective']  # where objective is the name of the attribute to maximize

            self.agent_function.improve(action, reward)
            action = self.agent_function.evaluate(observation)

        return self.agent_function

    @staticmethod
    def td_train(q_table, action, reward):
        pass


env = WoodCutterEnvironment()
arch = WoodCutter(env)
agent = RLAgent(env, arch)
training = TDLearn(0.9, 0.1)

agent.train(GreedyPolicy(), RLAgent.td_train, 10)
