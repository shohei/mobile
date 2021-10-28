NONE = 0
SUCCESS = 10

def advance_state(s,a):
    # todo: Calculate reward from the given state and action
    if a==0: # Press button 1
        s2 = 1-s # Toggle bulb state
        reward = NONE 
    else: # Press button 2
        if s==1: # Bulb is ON
            s2 = s # Bulb maintains current state 
            reward= SUCCESS # Cheese gained
        else:
            s2 = s # Bulb maintains current state 
            reward = NONE # No cheese because power is OFF 
    return reward, s2

if __name__=="__main__":
    s_a_s2s = [(0,0,0),(1,0,0),(0,1,0),(1,1,0)] # s_{t}, a_{t}, s_{t+1} 
    for s_a_s2 in s_a_s2s:
        s = s_a_s2[0] # s_{t}
        a = s_a_s2[1] # a_{t}
        s2 = s_a_s2[2] # s_{t+1}
        reward, s2 = advance_state(s,a)
        print(f"s={s},s2={s2},a={a},reward={reward}")

# Expected result
# s=0,s2=1,a=0,reward=0
# s=1,s2=0,a=0,reward=0
# s=0,s2=0,a=1,reward=0
# s=1,s2=1,a=1,reward=10