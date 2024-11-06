import gymnasium as gym
import numpy as np
import random

ACTIONS = [0, 1, 2]

# Functions to discretize the values of each state variable for their corresponding indexes-- DONE
def discretizeAngles(x): # Used for cosTheta1, sinTheta1, cosTheta2, sinTheta2
    x += 1
    index = x//0.04
    return index

def discretizeAngVelTheta1(angVelTheta1):
    angVelTheta1 += 158
    index = angVelTheta1//1
    return index

def discretizeAngVelTheta2(angVelTheta2):
    angVelTheta2 += 800
    index = angVelTheta2//1
    return index

# Get the best action and max future reward given a q table and state -- DONE
def getMaxFutureValue(q_table, cosTheta1, sinTheta1, cosTheta2, sinTheta2, angVelTheta1, angVelTheta2):
    max = -100
    cosTheta1Ind = int(discretizeAngles(cosTheta1))
    sinTheta1Ind = int(discretizeAngles(sinTheta1))
    cosTheta2Ind = int(discretizeAngles(cosTheta2))
    sinTheta2Ind = int(discretizeAngles(sinTheta2))
    angVelTheta1Ind = int(discretizeAngVelTheta1(angVelTheta1))
    angVelTheta2Ind = int(discretizeAngVelTheta2(angVelTheta2))
    for action in ACTIONS:
        if q_table[action][cosTheta1Ind][sinTheta1Ind][cosTheta2Ind][sinTheta2Ind][angVelTheta1Ind][angVelTheta2Ind] > max:
            max = q_table[action][cosTheta1Ind][sinTheta1Ind][cosTheta2Ind][sinTheta2Ind][angVelTheta1Ind][angVelTheta2Ind]
            bestAction = action
    return max, bestAction

# Initialize empty q table -- DONE
def initializeQTable():
    return np.zeros((3, 51, 51, 51, 51, 317, 1601))

# Update q table -- DONE
def updateQTable(q_table, state, reward, action, new_state):
    learningRate = 0.8
    discountFactor = 0.3

    # get the variable values from state, and discretize for their indexes
    cosTheta1 = state[0]
    sinTheta1 = state[1]
    cosTheta2 = state[2]
    sinTheta2 = state[3]
    angVelTheta1 = state[4]
    angVelTheta2 = state[5]

    cosTheta1Ind = int(discretizeAngles(cosTheta1))
    sinTheta1Ind = int(discretizeAngles(sinTheta1))
    cosTheta2Ind = int(discretizeAngles(cosTheta2))
    sinTheta2Ind = int(discretizeAngles(sinTheta2))
    angVelTheta1Ind = int(discretizeAngVelTheta1(angVelTheta1))
    angVelTheta2Ind = int(discretizeAngVelTheta2(angVelTheta2))

    # current Q value variable in equation; given current state variables' values and specified action
    currentQValue = q_table[action][cosTheta1Ind][sinTheta1Ind][cosTheta2Ind][sinTheta2Ind][angVelTheta1Ind][angVelTheta2Ind]

    # max future reward variable in equation; after the action performed on current state, move to new state, 
    # get the maximum q value possible from the q table
    maxFutureReward, _ = getMaxFutureValue(q_table, new_state[0], new_state[1], new_state[2], new_state[3], new_state[4], new_state[5])

    # reward if we reach the target height
    if (0-new_state[0] - (new_state[0]*new_state[2] - new_state[1]*new_state[3])) > 1.0:
        # update q table with reward 100
        q_table[action][cosTheta1Ind][sinTheta1Ind][cosTheta2Ind][sinTheta2Ind][angVelTheta1Ind][angVelTheta2Ind] = 100
        print("GOAL REACHED!")
    else:
        # update q table with q learning formula
        newQValue = currentQValue + learningRate*(reward + (discountFactor * maxFutureReward) - currentQValue)
        q_table[action][cosTheta1Ind][sinTheta1Ind][cosTheta2Ind][sinTheta2Ind][angVelTheta1Ind][angVelTheta2Ind] = newQValue


def runEpisode(q_table):
    state, _ = env.reset()
    running = True
    won = 0
    while running:
        _, bestAction = getMaxFutureValue(q_table, state[0], state[1], state[2], state[3], state[4], state[5])
        if random.randint(1,10) % 10 == 0: # Picks a random action 10% of the time to explore new paths other than the ones that have already been rewarded
            action = random.choice(ACTIONS)
        else: # 90% of the time will perform the best action from the q table
            action = bestAction
        new_state, reward, terminated, truncated, _ = env.step(action) # move the acrobot one step
        updateQTable(q_table, state, reward, action, new_state)
        if terminated: # Will return 1 if won within time frame
            won = 1
        if terminated or truncated:
            running = False
        state = new_state
    return won # Used to calculate win rate

# run our q learning
q_table = initializeQTable()
episodes = 5000
wins = 0
for i in range(1, episodes):
    print("episode: ", i)
    win_rate = wins/i # Calculates the win rate
    if i % 200 == 0 and i != 1: # Prints the win rate and displays the episode every 200 episodes
        print("Current win_rate:", win_rate, "(", wins, "won /", i, "episodes )")
        mode = "human"
    else:
        mode = "none"
    env = gym.make("Acrobot-v1", render_mode = mode)
    wins += runEpisode(q_table) # Run episode and also add 1 to the number of wins if won in that episode
env.close

