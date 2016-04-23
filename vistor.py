class FunctionImplementation:
    def improve_by(self, imp_func):
        imp_func.improve(self)


class Table(FunctionImplementation):
    def improve_by_td(self, imp_func):
        print("A table improved by TDLearn")

    def improve_by_q(self, imp_func):
        print("A table improved by QLearn")

    def improve_by_sarsa(self, imp_func):
        print("A table improved by SARSA")


class NeuralNetwork(FunctionImplementation):
    def improve_by_td(self, imp_func):
        print("A neural network improved by TDLearn")

    def improve_by_q(self, imp_func):
        print("A neural network improved by QLearn")

    def improve_by_sarsa(self, imp_func):
        print("A neural network improved by SARSA")


class CalculusExpression(FunctionImplementation):
    def improve_by_td(self, imp_func):
        print("A calculus expression improved by TDLearn")

    def improve_by_q(self, imp_func):
        print("A calculus expression improved by QLearn")

    def improve_by_sarsa(self, imp_func):
        print("A calculus expression improved by SARSA")


class TDLearn:
    def improve(self, func_impl):
        func_impl.improve_by_td(self)


class QLearn:
    def improve(self, func_impl):
        func_impl.improve_by_q(self)


class SARSA:
    def improve(self, func_impl):
        func_impl.improve_by_sarsa(self)


table = Table()
td_learn = TDLearn()

table.improve_by(td_learn)
