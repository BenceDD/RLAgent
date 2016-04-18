from Policy import *
from Architecture import *
from Environment import *


class TDTrainer:

    @staticmethod
    def train(environment, architecture, iteration_limit):

        agent_function = AgentFunction()
        last_action = None
        problem_generator = EpsilonGreedyPolicy()

        for i in range(0, iteration_limit):
            observation, reward = architecture.observe(environment)
            agent_function.improve(last_action, reward)

            best_action = agent_function.evaluate(observation)
            next_action = problem_generator.evaluate(best_action)

            architecture.execute(environment, next_action)
            last_action = next_action

        return agent_function


trainer = TDTrainer()
arch = WoodCutter()
env = WoodCutterEnvironment()
trainer.train(env, arch, 10)
