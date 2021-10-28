import numpy as np
TRIAL_MAX = 100
num_a = 2
num_s = 2
epsilon = 0.1
alpha = 0.5
gamma = 0.9

from rl1_ans import advance_state 
from rl2_ans import max_Qval
from rl4_ans import epsilon_greedy

if __name__=="__main__":
    Qtable = np.zeros((num_s,num_a))
    s = 0
    s2 = 0
    for _ in range(TRIAL_MAX):
        while True:
            a = epsilon_greedy(epsilon, s, num_a, Qtable)
            reward, s2 = advance_state(s,a)
            Q_max = max_Qval(s2, Qtable)
            Qtable[s][a] = (1-alpha)*Qtable[s][a] + alpha*(reward+gamma*Q_max)
            s = s2
            if reward>0:
                break
    print(Qtable)
