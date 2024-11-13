import gymnasium as gym
import numpy as np
import random

ACTIONS = [1, 2, 0, 3]

def getMaxFutureValue(q_table, state):
    ACTIONS = [1, 2, 0, 3]
    bestAction = 0
    bestActionNumber = random.choice(ACTIONS)
    for action in ACTIONS:
        if q_table[action][state] > bestAction:
            bestAction = q_table[action][state]
            bestActionNumber = action
    return bestAction, bestActionNumber

def initQtable():
    return np.zeros((4, 48))

def updateQTable(q_table, state, reward, action, new_state): 
    learningRate = .1
    discountFactor = .8

    if (new_state == 47):
        q_table[action][state] = 100
        print("Goal REACHED YAY!!")
    elif (new_state >= 25) and (new_state <= 34):
        q_table[action][state] = -100                        
    else:
        maximumFutureReward,_ = getMaxFutureValue(q_table, new_state)
        currentQvalue = q_table[action][state]
        newQvalue = currentQvalue + learningRate * (reward + discountFactor*maximumFutureReward - currentQvalue)
        q_table[action][state] = newQvalue


def runEpisode(q_table, env):
    state, _ = env.reset()
    running = True
    while running:
        #print ("qtable", q_table)
        _, actionNumber = getMaxFutureValue(q_table, state)
        new_state, reward, terminated, truncated, _ = env.step(actionNumber)
        updateQTable(q_table, state, reward, actionNumber, new_state)
        if terminated or truncated:
            running = False
        state = new_state

episodes = 10000
q_table = initQtable()
env = gym.make("CliffWalking-v0")

for i in range(episodes):
    print(q_table)
    print("epi", i)
    if i % 100 == 0:
        mode = "human"
    else:
        mode = "none"
    state, _ = env.reset() 
    runEpisode(q_table, env)
env.close()