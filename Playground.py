from Environment import *
from Architecture import *
import Policy
import TrainingFunction
import random

mm = MazeMan(Maze())


d = {'a': 0.2, 'b': 0, 'c': 0.4, 'd': 0.4}

gr = Policy.EpsilonGreedy(epsilon=0.2, regression=0.5)

table = TrainingFunction.Table()

af = Policy.AgentFunction(table)
af.policy = gr

#dd = {{'a': 4, 'b': 3}: 34, {'a': 4, 'd': 3}: 31}
#print(dd[{'a': 4, 'b': 3}])


#tuple(sorted(someDictionary .items())

actions = [{'fek': 'be', 'gaz': 'be'},
           {'fek': 'ki', 'gaz': 'be'},
           {'fek': 'be', 'gaz': 'ki'},
           {'fek': 'ki', 'gaz': 'ki'}]


actions2 = [{'fek': 'fully', 'gaz': 'be'},
           {'fek': 'halfly', 'gaz': 'be'}, ]
