import gymnasium as gym
import numpy as np
import random

env = gym.make("CliffWalking-v0", render_mode = "human")
ACTIONS = [1, 2, 0, 3]

def getMaxFutureValue(q_table, state):
    bestAction = -100
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
    elif new_state >= 25 and new_state <= 34:
        q_table[action][state] = -100                        
    else:
        maximumFutureReward,_ = getMaxFutureValue(q_table, new_state)
        currentQvalue = q_table[action][state]
        newQvalue = currentQvalue + learningRate * (reward + discountFactor*maximumFutureReward - currentQvalue)
        q_table[action][state] = newQvalue


def runEpisode(q_table):
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

episodes = 10
q_table = initQtable()

env = gym.make("CliffWalking-v0", render_mode = "none")

for i in range(episodes):
    print(q_table)
    print("epi", i)
    if i % 100 == 0 and i != 0:
        env.close()
        env = gym.make("CliffWalking-v0", render_mode = "human")
    runEpisode(q_table)

env.close()

