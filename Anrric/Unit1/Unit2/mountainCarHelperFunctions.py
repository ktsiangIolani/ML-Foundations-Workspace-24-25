import gymnasium as gym
# ML Foundations 24-25



import numpy as np
import random
ACTIONS = [0, 1, 2]
# Matches a position on the mountain car hill to the correct index for our q table
# For example, -1.2 should match to 0, -1.1 should match to 1 ... 0.5 should match to 17, and 0.6 should match to 18
# Hint: Use the // operator to find the integer division of a number
def discretizePosition(position):
    index = position + 1.2
    index=index//0.1
    return int(index)


# Matches a velocity on the mountain car hill to the correct index for our q table
# For example, -0.07 should match to 0, -0.06 should match to 1 ... 0.06 should match to 13, and 0.07 should match to 14
# Hint: Use the // operator to find the integer division of a number
def discretizeVelocity(velocity):
    index = velocity + 0.07
    index = index//0.01
    return int(index)


# Returns the best action to take given a state and q table
# Find this by comparing all possible actions for a given state in the q table and returning the action with the highest value
# Hint 1: Use the discretizePosition and discretizeVelocity functions to find the correct index in the q table for the given position and velocity
# Hint 2: Use a for loop to iterate through all possible actions (0, 1, 2) and compare the q values for each action
def getMaxFutureValue(q_table, position, velocity):
    #q_table[action][position][velocity]
    #loop through all the possible actions for a given position and velocity
    #find the largest one
    positionIndex = discretizePosition(position)
    velocityIndex = discretizeVelocity(velocity)




    bestAction = -100
    for action in ACTIONS:
        if q_table[action][positionIndex][velocityIndex] > bestAction:
            bestAction = q_table[action][positionIndex][velocityIndex]
    return bestAction


def initQTable():
    return np.zeros((3, 18, 14))


def updateQTable(q_table, state, reward, action, new_state):
    position = state[0]
    velocity = state[1]
    positionIndex = discretizePosition(position)
    velocityIndex = discretizeVelocity(velocity)
    learningRate = 0.1
    discountFactor = 0.6


    #reward if we reach the top
    if position > 0.5:
        #update qtable with reward 100
        q_table[action][positionIndex][velocityIndex] = 100
        print("GOAL REACHED YAY!!")
    else:
        new_state = q_table[action][positionIndex][velocityIndex] + learningRate(reward+discountFactor )
        pass #update q table with the q learning formula FOR HOMEWORK




def runEpisode(q_table):
    state, _ = env.reset()
    running = True
    while running:
        action = random.choice(ACTIONS)
        new_state, reward, terminated,truncated, _ = env.step(action) # move the car one step
        updateQTable(q_table, state, reward, action, new_state)
        if terminated or truncated:
            running = False
        state = new_state


#----------------------- PART 1 IMPLEMENT MOUNTAIN CAR ENV---------------------
#run our q learning
q_table = initQTable()
episodes = 100
for i in range(episodes):
    print("episode: ", i)
    if i % 100 == 0:
        mode = "human"
    else:
        mode = "none"
    env = gym.make("MountainCar-v0", render_mode=mode)
    runEpisode(q_table)
env.close()








