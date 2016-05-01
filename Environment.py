import random


class WoodCutterEnvironment:

    def __init__(self):
        self.money = 100
        self.tree_age = 0

    def wait_one_more_year(self):
        if random.randint(0, 7) is 2:
            self.tree_age = 0
            self.money -= 50
            return -50
        return 0

    def cut_down_trees(self):
        income = self.tree_age * 10
        self.money += (income - 50)
        return income
