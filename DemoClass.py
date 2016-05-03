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
            self.agent_function.last_state = self.agent_function.state

            (observation, reward) = self.architecture.interact(action)
            actions = self.architecture.get_actions()  # a set of possible actions (vectors)
            # TODO: define reward here from the observation?
            # reward = observation['objective']  # where objective is the name of the attribute to maximize

            self.agent_function.improve(reward)
            action = self.agent_function.evaluate(observation, actions)

        return self.agent_function


env = WoodCutterEnvironment()
arch = WoodCutter(env)
agent = RLAgent(env, arch)

agent.train(GreedyPolicy(), TDLearn(0.9, 0.1), 10)
