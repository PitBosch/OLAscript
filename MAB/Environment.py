import numpy as np
class Environment():
    def __init__(self, n_arms, probabilities):
        self.n_arms=n_arms
        self.probabilities=probabilities

    def round(self, puleld_arm):
        reward=np.random.binomial(1, self.probabilities[pulled_arm])
        return reward
    