import random


class WoodCutterEnvironment:
    """
    Calculate reward, always return with it.
    """

    def __init__(self):
        self.money = 100
        self.tree_age = 0

    def wait_one_more_year(self):
        if random.randint(0, 13) is 2:
            self.tree_age = 0
            self.money -= 50
            return -50
        else:
            self.tree_age += 1
            return 0

    def cut_down_trees(self):
        income = self.tree_age * 10
        self.money += (income - 50)
        self.tree_age = 0
        return income


class MazeEnvironment:
    # TODO: implement Maze environment
    def __init__(self):
        self._map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
            [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def get_area(self, x, y):
        try:
            return self._map[x][y]
        except IndexError:
            return 0

    # http://mnemstudio.org/path-finding-q-learning-tutorial.htm
    # http://artint.info/html/ArtInt_265.html
