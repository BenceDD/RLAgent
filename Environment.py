import random


class Forest:

    def __init__(self):
        self.money = 100  # just for fun (debug)
        self.tree_age = 0

    def wait_one_more_year(self):
        if random.randint(0, 20) is 2:
            self.tree_age = 0
            self.money -= 50
            return -50
        else:
            self.tree_age += 1
            return 0

    def cut_down_trees(self):
        income = self.tree_age * 10 - 50
        self.money += income
        self.tree_age = 0
        return income


class Maze:

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
        self._avatar = {'x': 9, 'y': 1}

    def _get_area(self, x, y):
        try:
            return self._map[x][y]
        except IndexError:
            return 0

    def _look_around(self):
        return {'up': self._get_area(self._avatar['x'] - 1, self._avatar['y']),
                'down': self._get_area(self._avatar['x'] + 1, self._avatar['y']),
                'left': self._get_area(self._avatar['x'], self._avatar['y'] - 1),
                'right': self._get_area(self._avatar['x'], self._avatar['y'] + 1)}

    def step(self, direction):
        view = self._look_around()

        if direction is 'up' and view['up'] is 1:
            self._avatar['x'] -= 1
        elif direction is 'down' and view['down'] is 1:
            self._avatar['x'] += 1
        elif direction is 'left' and view['left'] is 1:
            self._avatar['y'] -= 1
        elif direction is 'right' and view['right'] is 1:
            self._avatar['y'] += 1

        return self._avatar, self._look_around()

    def reset(self):
        self._avatar = {'x': 9, 'y': 1}
