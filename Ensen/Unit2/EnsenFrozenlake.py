import gymnasium as gym
import numpy as np
import random
ACTIONS = [1, 0,2,3]

#returns the best action in a given
# state that will be used to calculte the q table value
def getMaxFutureValue(q_table, state):
    #loops through all possible actions for a given state and give it it's respective reward
    ACTIONS = [1, 0, 2, 3]
    bestAction = 0
    bestActionNumber = random.choice(ACTIONS)# 0, 1, 2, 3 is the best action based on what we find
    for action in ACTIONS:
        if q_table[action][state] > bestAction:
            bestAction = q_table[action][state]
            bestActionNumber = action
    return bestAction, bestActionNumber

def initQTable():
    #defines the 2D table
    return np.zeros((4,16))

def updateQTable(q_table, state, reward, action, new_state):
    learningRate = .7
    discountFactor = .6
    if new_state == 15:
        #this is the location of the chest/the goal of the character
        q_table[action][state] = 100
        print("Goal Reached Yay!!")
    elif new_state == 5:
        q_table[action][state] = -1000
    elif new_state == 7:
        q_table[action][state] = -1000
    elif new_state == 11:
        q_table[action][state] = -1000
    elif new_state == 12:
        q_table[action][state] = -1000

    else:
        #formula for q learning
        maximumFutureReward, _ = getMaxFutureValue(q_table, new_state)
        currentQValue = q_table[action][state]
        newQValue = currentQValue + learningRate*(reward + discountFactor*maximumFutureReward - currentQValue)
        q_table[action][state] = newQValue
        #print(q_table)


def runEpisode(q_table):
    state, _ = env.reset()
    running = True
    while running:
        action = random.choice(ACTIONS)
        _, action = getMaxFutureValue(q_table, state)
        new_state, reward, terminated, truncated, _ = env.step(action)
        updateQTable(q_table, state, reward, action, new_state)
        if terminated or truncated:
            running = False
        state = new_state

q_table = initQTable()
episodes = 1000
for i in range(episodes):
    print("episode: ", i)
    if i % 1000 == 0:
        mode = "human"
    else:
        mode = "none"
    env = gym.make("FrozenLake-v1", render_mode = mode)
    runEpisode(q_table)
env.close()
