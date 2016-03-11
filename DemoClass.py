class Environment:
    """ This class represents the environment, which about we can get info, or apply actions on. """
    def get_info(self):
        # this is NOT a complete state because of the partially observable environment.
        return "A"

    def apply_action(self, action):
        return


class DiscreteModel:
    """ The model represents the knowledge about the world. It has to have an initial state.
        Knowledge is the states and it's reward value (empirical)
    """

    def __init__(self, state):
        # States will contain all the states with its utility
        self._states = {state: 0}

        # Status indicates the current , which MUST be a key in the states array!
        self._state = state

    def _evaluate(self, info):
        """ This function "converts" info to state """
        return "State"

    def update(self, info, reward):
        # assume witch state we are in
        state = self._evaluate(info)

        # add the state and the reward (it store the last reward, is it ok??)
        self._states[state] = reward

        # Set current state
        self._state = info

    def get_available_actions(self):
        # Assumed that an state change possibility means that it is declared in the dictionary
        return self._pm[self._state]


class MatrixUtilityImplementation:
    def __index__(self):
        # PM (probability matrix) represents a graph, which currently has only one point, without any edge
        self._pm = {}

    def get_utility(self, state):
        return "4"


class EpsilonGreedyPolicy:

    def __init__(self, utility):
        # braveness factor
        self._epsilon = 1

        # implementation of a storage for utilities
        self._utility = utility

        self._model = DiscreteModel(environment.get_state())

    def evaluate(self, info):

        # depend on the rule, update the model, 

         # update the model based on the information about the last experiment
        self._model.update(info)

         # get the available actions from the model
        action_list = self._model.get_available_actions()


        # TODO: implement epsilon greedy rule! This method call should improve the policy!
        return max(states, key=lambda x: states[x])

    def _improve(self):
        return


class Agent:
    """ An agent in the environment:
        - at first it needs to get informed about the surrounding world, and make a strategy from it
        - after that it should be manipulate the world (apply actions)
    """
    def __init__(self, environment, policy):
        self._environment = environment
        self._policy = policy

    def start(self):
        # a stop condition should be here...
        while():
            # gathering information from the world (part of state, reward)
            info = self._environment.get_info()

            # figure out what to do :)
            action = self._policy.evaluate(info)

            # do it
            self._environment.apply_action(action)
        return

