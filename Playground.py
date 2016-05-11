from Environment import *
from Architecture import *
import Policy
import TrainingFunction
import random

mm = MazeMan(Maze())


d = {'a': 0.2, 'b': 0, 'c': 0.4, 'd': 0.4}

gr = Policy.EpsilonGreedy(epsilon=0.2, regression=0.5)

af = Policy.AgentFunction(TrainingFunction.Table())
af.policy = gr

for i in range(0, 20):
    print(af.evaluate('state1', d))
