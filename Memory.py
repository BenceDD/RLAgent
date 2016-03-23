class Memory:
    def __init__(self):
        self._storage = []

    def store(self, observation):
        self._storage.append(observation)

    def recall(self, state):
        return [(s1, a, s2, r) for s1, a, s2, r in self._storage if state == s1]

    def recall_last(self, n=1):
        return self._storage[len(self._storage) - n: len(self._storage)]
