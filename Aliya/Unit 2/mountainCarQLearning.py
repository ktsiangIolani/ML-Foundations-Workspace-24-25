import gymnasium as gym
import numpy as np
import random

# -------------- PART 1: Implement Mountain Car --------------

# 0 - acclerate left; 1 - don't accelerate; 2 - accelerate right
ACTIONS = [0, 1, 2]



# -------------- PART 2: Q LEARNING HELPER FUNCTIONS --------------

# Matches a position on the mountain car hill to the correct index for our q table
def discretizePosition(position):
    position += 1.2
    index = position//0.1
    return(index)   

# Matches a velocity on the mountain car hill to the correct index for our q table
def discretizeVelocity(velocity):
    velocity += 0.07
    index = velocity//0.01
    return(index)


# Returns the best action to take given a state and q table
def getMaxFutureValue(q_table, position, velocity):
    max = -100
    x = int(discretizePosition(position))
    v = int(discretizeVelocity(velocity))
    for action in ACTIONS:
        if q_table[action][x][v] > max:
            max = q_table[action][x][v]
            bestAction = action
    return max, bestAction

def initializeQTable():
    return np.zeros((3, 19, 15))

def updateQTable(q_table, state, reward, action, new_state):
    #CHECK
    learningRate = 0.1
    discountFactor = 0.4

    # get the position and velocity from state, and discretize for their indexes
    position = state[0]
    velocity = state[1]
    pInd = int(discretizePosition(position))
    vInd = int(discretizeVelocity(velocity))
    # same for new state
    newPos = new_state[0]
    newVel = new_state[1]
    maxQ, _ = getMaxFutureValue(q_table, newPos, newVel)
    
    # current Q value variable in equation; given current position, velocity, and specified action
    currentQValue = q_table[action][pInd][vInd]
    # max future reward variable in equation; after the action performed on current state, move to new state, 
    # get the maximum q value, the best action, for the max future reward variable in equation
    maxFutureReward = maxQ

    # reward if we reach the top 
    if newPos > 0.5:
        # update q table with reward 100
        q_table[action][pInd][vInd] = 100
        print("GOAL REACHED YAY!!!")
    else:
        # update q table with q learning formula
        newQValue = currentQValue + learningRate*(reward + (discountFactor * maxFutureReward) - currentQValue)
        q_table[action][pInd][vInd] = newQValue



# -------------- PART 3: CONDUCT Q LEARNING ON MOUNTAIN CAR --------------
def runEpisode(q_table):
    state, _ = env.reset()
    running = True
    while running:
        _, bestAction = getMaxFutureValue(q_table, state[0], state[1])
        new_state, reward, terminated, truncated, _ = env.step(bestAction) # move the car one step
        updateQTable(q_table, state, reward, bestAction, new_state)
        if terminated or truncated:
            running = False
        state = new_state

# run our q learning
q_table = initializeQTable()
episodes = 1000
for i in range(episodes):
    print("episode: ", i)
    if i % 100 == 0:
        mode = "human"
    else:
        mode = "none"
    env = gym.make("MountainCar-v0", render_mode = mode)
    runEpisode(q_table)
env.close