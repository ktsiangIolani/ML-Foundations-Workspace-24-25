import gymnasium as gym
import numpy as np
import random

# 0 is accelerate left, 1 is dont accelerate, and 2 is accelerate right
ACTIONS = [0, 1, 2]

# Matches a position on the mountain car hill to the correct index for our q table
# For example, -1.2 should match to 0, -1.1 should match to 1 ... 0.5 should match to 17, and 0.6 should match to 18
# Hint: Use the // operator to find the integer division of a number
def discretizePosition(position):
    index = position + 1.2
    index = index//.1
    return int(index)

# Matches a velocity on the mountain car hill to the correct index for our q table
# For example, -0.07 should match to 0, -0.06 should match to 1 ... 0.06 should match to 13, and 0.07 should match to 14
# Hint: Use the // operator to find the integer division of a number
def discretizeVelocity(velocity):
    index = velocity + .07
    index = index//.01
    return int(index)


# Returns the best action to take given a state and q table
# Find this by comparing all possible actions for a given state in the q table and returning the action with the highest value
# Hint 1: Use the discretizePosition and discretizeVelocity functions to find the correct index in the q table for the given position and velocity
# Hint 2: Use a for loop to iterate through all possible actions (0, 1, 2) and compare the q values for each action
def getMaxFutureValue(q_table, position, velocity):
    # loop through all the possible actions for a given position and velocity
    positionIndex = discretizePosition(position)
    velocityIndex = discretizeVelocity(velocity)
    ACTIONS = [0,1,2]

    bestAction = -100
    bestActionNumber = 0 # 0, 1,or 2 based on the ebst action we find
    for action in ACTIONS:
       if q_table[action][positionIndex][velocityIndex] > bestAction:
            bestAction = q_table[action][positionIndex][velocityIndex]
            bestActionNumber = action
    return bestAction, bestActionNumber # returns a qValue (bestAction) and a number 0, 1 ,or 2 (bestActionNumber)

def initQtable():
    return np.zeros((3, 18, 14))

def updateQTable(q_table, state, reward, action, new_state):
    position = state[0]
    velocity = state[1]
    newPosition = new_state[0]
    newVelocity = new_state[1]
    positionIndex = discretizePosition(position)
    velocityIndex = discretizeVelocity(velocity)
    # reward if we reach the top

    #variables for equation
    learningRate = 0.1
    discountFactor = .8

    if (newPosition >= .5):
        # update q table with reward 100
        q_table[action][positionIndex][velocityIndex] = 100
        print("GOAL REACHED YAY!!")
    else:
        maximumFutureReward,_ = getMaxFutureValue(q_table, newPosition, newVelocity)
        currentQvalue = q_table[action][positionIndex][velocityIndex]
        newQvalue = currentQvalue + learningRate * (reward + discountFactor*maximumFutureReward - currentQvalue)
        q_table[action][positionIndex][velocityIndex] = newQvalue
    
def runEpisode(q_table):
    state, _ = env.reset()
    running = True
    while running:
        # choose the best future action
        _, actionNumber = getMaxFutureValue(q_table, state[0], state[1])
        new_state, reward, terminated, truncated, _ = env.step(actionNumber) #move the car one step
        updateQTable(q_table, state, reward, actionNumber, new_state)
        if terminated or truncated:
            running = False
        state = new_state

#initialize the mountain car environment from gymnasium

# run our q learning
episodes = 1000
q_table = initQtable()
for i in range(episodes):
    print("epi", i)
    if i % 100 == 0:
        mode =  "human"
    else:
        mode = "none"
    env = gym.make("MountainCar-v0", render_mode = mode)
    runEpisode(q_table)
env.close()