from Policy import *
from Architecture import *
from Environment import *
from TrainingFunction import *


class RLAgent:

    def __init__(self, environment, architecture, knowledge):  # reward?
        self.environment = environment
        self.architecture = architecture
        self.agent_function = AgentFunction(knowledge)

    def train(self, policy, learning_function, iteration_limit):
        # these can be set for a single training session
        self.agent_function.policy = policy
        self.agent_function.training_method = learning_function

        observation = self.architecture.initial_state()

        lap_start = 0
        quality_target = 0

        for i in range(0, iteration_limit):
            # this is a list of dicts
            actions = self.architecture.get_actions()  # a set of possible actions (vectors)
            action = self.agent_function.evaluate(observation, actions)

            (observation, reward) = self.architecture.interact(action)

            if reward > 0:
                lap_time = i - lap_start
                print("[" + str(i) + "] Round Finished: " + str(lap_time))
                lap_start = i + 1
                if lap_time < 50:
                    quality_target += 1
                if quality_target > 5:
                    print("Quality target was hit in " + str(quality_target) + " times.")
                    break

            self.agent_function.improve(reward)

        print("Quality target was hit in " + str(quality_target) + " times.")

        return self.agent_function

env = Maze()
arch = MazeMan(env)
agent = RLAgent(env, arch, Table())

agent.train(EpsilonGreedy(epsilon=0.1, regression=0.5), QLearn(learning_rate=0.2, discount_factor=0.95), 3000000)
