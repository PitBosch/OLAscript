from Environment import Environment
import numpy as np
class Non_Stationary_Environment(Environment):
    def __init __(self,n_arms,probabilities,horizon):
        super().__ init_(n_arms,probabilities)
        self.t=0
        n_phases=len(self.probabilities)
        self.phases_size=horizon/n_phases
    def round(self,pulled_arm):
        current_phase=int(self.t/self.phase_size)
        p=self.probabilities[current_phase][pulled_arm]
        reward=np.random.binomial(1,p)
        self.t+=1
        return reward
