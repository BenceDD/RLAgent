import random


class Environment:

    def observe(self):
        pass

    def apply_action(self, action):
        pass


class WoodCutterEnvironment(Environment):

    def __init__(self):
        self._money = 100
        self._tree_age = -1
        self._storm_happened = False  # this is just for printing
        self._actions = ['plant tree', 'cut out tree', 'wait']

    def observe(self):
        if self._storm_happened is True:
            print('Your trees destroyed!! :(')

        if self._tree_age == -1 or self._storm_happened is True:
            print('You have no trees.')
        else:
            print('Your trees ' + str(self._tree_age) + ' years old.')

        print('Your money is: ' + str(self._money))

        if self._tree_age == -1 or self._storm_happened is True:
            actions = ['plant tree', 'wait']
        else:
            actions = ['cut out tree', 'wait']

        return self._tree_age, actions, self._money

    def apply_action(self, action):

        if self._storm_happened is True:
            self._storm_happened = False

        if action == 'plant tree' and self._tree_age == -1 and self._money >= 50:
            self._money -= 50
            self._tree_age = 0
            print('Trees planted!')
        if action == 'cut out tree' and self._tree_age != -1:
            self._money += (self._tree_age * 20)
            print('Trees has cut down. You earned: ' + str(self._tree_age * 20))
            self._tree_age = -1
        if action == 'wait':
            self._tree_age += 1
            print('Waiting for one year...')

        if random.randint(0, 7) is 2:
            self._tree_age = -1
            self._storm_happened = True
