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

        observation = self.architecture.initial_state()
        for i in range(0, iteration_limit):

            print(str(i) + ". round begin!")
            actions = self.architecture.get_actions()  # a set of possible actions (vectors)

            print("[RLAgent] Getting the next action...")
            action = self.agent_function.evaluate(observation, actions)
            print("[RLAgent] We got the next action, which is: " + str(action))

            (observation, reward) = self.architecture.interact(action)
            print("[RLAgent] The observation is: " + str(observation))
            print("[RLAgent] The reward is: " + str(reward))

            print("[RLAgent] Improvement the agent function...")
            self.agent_function.improve(reward)
            print("[RLAgent] Improvement finished")

            print("----------------------------------------")

        return self.agent_function


env = WoodCutterEnvironment()
arch = WoodCutter(env)
agent = RLAgent(env, arch)

agent.train(GreedyPolicy, QLearn(0.1, 0.9), 1000)
