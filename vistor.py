class FunctionRepresentation(object):
    def improve_by(self, training_function):
        training_function.visit(self)
    # itt kell majd felsorolni mind a 9 esetet
    def pollinate(self, pollinator):
        print(self, "pollinated by", pollinator)
    def eat(self, eater):
        print(self, "eaten by", eater)
    def __str__(self):
        return self.__class__.__name__


class Table(FunctionRepresentation):
    def improve_by(self, training_function):
        training_function.train_table(self)

class CalculusExpression(FunctionRepresentation): pass
class NeuralNetwork(FunctionRepresentation): pass

class TrainingFunction:

    def train_table(self): pass

    def __str__(self):
        return self.__class__.__name__

class TableLearner(TrainingFunction): pass
class NetworkLearner(TrainingFunction): pass
#class CalculusLearner(TrainingFunction): pass

# Add the ability to do "Bee" activities:
class TDLearn(TableLearner):
    def visit(self, flower):
        flower.pollinate(self)

    def train_table(self, func_repl):
        func_repl.td_train_table(self)

# Add the ability to do "Fly" activities:
class QLearn(TableLearner):
    def visit(self, flower):
        flower.pollinate(self)

# Add the ability to do "Worm" activities:
class SARSA(NetworkLearner):
    def visit(self, flower):
        flower.eat(self)


# It's almost as if I had a method to Perform
# various "Bug" operations on all Flowers:
tdlearn = TDLearn()
qlearn = QLearn()
sarsa = SARSA()

table = Table()
calc = CalculusExpression()
network = NeuralNetwork()

table.improve_by(sarsa)
