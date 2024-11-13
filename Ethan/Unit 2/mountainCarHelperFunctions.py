# ML Foundations 24-25 
# Mountain Car RL Helper Functions - Ms. Tsiang

#Name: Ethan Mashimo

import numpy as np
# Matches a position on the mountain car hill to the correct index for our q table
# For example, -1.2 should match to 0, -1.1 should match to 1 ... 0.5 should match to 17, and 0.6 should match to 18
# Hint: Use the // operator to find the integer division of a number
def discretizePosition(position):
    index = position + 1.2
    index = index//0.1 
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
    # q_table[action][position][velocity]
    # loop through all the possible actions for a given posiion and velocity 
    # find the largest one
    positionIndex = discretizePosition(position)
    velocityIndex = discretizeVelocity(velocity)
    ACTIONS = [0, 1, 2]
    bestAction = -100

    for action in ACTIONS:
        if q_table[action][positionIndex][velocityIndex] > bestAction:
            bestAction = q_table[action][positionIndex][velocityIndex]
    return bestAction
        
        



        
        
        



# Test cases
if __name__ == "__main__":

    print("Testing discretizePosition")
    assert(discretizePosition(-1.2) == 0)
    assert(discretizePosition(-1.09999) == 1)
    assert(discretizePosition(0.5321) == 17)
    assert(discretizePosition(0.6145) == 18)
    print("All tests passed for discretizePosition")

    print("Testing discretizeVelocity")
    assert(discretizeVelocity(-0.07) == 0)
    assert(discretizeVelocity(-0.0599) == 1)
    assert(discretizeVelocity(0.06) == 13)
    assert(discretizeVelocity(0.07) == 14)
    print("All tests passed for discretizeVelocity")

    print("Testing getMaxFutureValue")
    # 3 x 18 x 14 q table
    q_table = np.zeros((3, 19, 15))
    q_table[0][0][0] = 1
    q_table[2][17][14] = 2
    q_table[1][17][14] = 1
    q_table[0][18][13] = 2
    q_table[2][18][13] = 3
    assert(getMaxFutureValue(q_table, -1.2, -0.07) == 1)
    assert(getMaxFutureValue(q_table, 0.51, 0.07) == 2)
    assert(getMaxFutureValue(q_table, 0.61, 0.061) == 3)
    print("All tests passed for getMaxFutureValue")