import gymnasium as gym
import numpy as npy
import random
import ale_py
# from ale_py import ALEInterface, roms

# 'state' is a 2D array, 160 x 210, length 160 pixels, width 210 pixels, 
#  state[y][x]
# state[all y][0-8x] is black
'''
Y (0 top; 209 bottom)
0-3 black [0, 0, 0]
4-13 dark grey [142, 142, 142]
14 black [0, 0, 0]
15-22 light grey [170, 170, 170]
23 black [0, 0, 0] FINISH
39 white [214, 214, 214] LANE 11
55 white [214, 214, 214] LANE 10
71 white [214, 214, 214] LANE 9
87 white [214, 214, 214] LANE 8
102 yellow [252, 252, 84] LANE 7
103 dark grey [142, 142, 142] LANE 6 HALFWAY POINT
104 yellow [252, 252, 84]
119 white [214, 214, 214] LANE 5
135 white [214, 214, 214] LANE 4
151 white [214, 214, 214] LANE 3
167 white [214, 214, 214] LANE 2
185 black [0, 0, 0] START/LANE 1
186-194 light grey [170, 170, 170]
195-209 black [0, 0, 0] and 'Activision' label
'''

### WHERE'S THE CHICKEN; WHERE'S SCORE; WHERE'S CHICKEN POSITION; HOW MUCH IS EACH STEP; HOW TO TELL IF BEEN HIT; WHY THE SECOND CHICKEN
### WHAT'S 'dict' type

gym.register_envs(ale_py)
env = gym.make("ALE/Freeway-v5", render_mode = "human")
state, info = env.reset()

'''
for i in range(10):
    for i in range(3):
        env.step(0)
    env.step(1)
    print(state[2])
'''

for i in range(10):
   env.step(1)

#print(state[10])
'''
print(len(info))
print(info)
print(type(info))
'''

### info --- {'lives': 0, 'episode_frame_number': 0, 'frame_number': 0}

#print(state[104]) # 0-8 black; 9-12 grey; 13-16 yellow; 17-20 grey; 21-24 yellow; 25-28 grey; alternate grey yellow, each 4 pixels along x direction
#print(state)


for y in range(100, 210):
    for x in range(160):
        if int(state[y][x][1]) > int(state[y][x][2]) and int(state[y][x][0]) > int(state[y][x][2]) and y != 102 and y != 104:
            print(str(y) + ", " + str(x) + str(state[y][x]))

for y in range(170, 180):
    for x in range(155, 160):
        if list(state[172][x]) == [210, 210, 64]:
            print(str(y) + ", " + str(x) + str(state[y][x]))
#print(state[172])

print(len(state))
print(len(state[100]))

'''
for i in range(210):
    if state[i][14][0] != 170 and state[i][14][0] != 142:
        print("index: " + str(i))
        print("colour: " + str(state[i][14]))
'''

'''
running = True
while running:
    action = env.action_space.sample() #policy(obs)  # to implement - use `env.action_space.sample()` for a random policy
    new_state, reward, terminated, truncated, info = env.step(action)
    #print("state" + state)

    episode_over = terminated or truncated
env.close()
'''

# 0 - stay still; 1 - hop forwards; 2 - hop backwards
ACTIONS = [0, 1, 2] 

# Discretize state variables' values for the correct index in q table
def discretizeRed(r):
    index = r//1
    return(index) 

def discretizeGreen(g):
    index = g//1
    return(index) 

def discretizeBlue(b):
    index = b//1
    return(index) 

def discretizePixelXPosition(x):
    index = x//1
    return(index) 

def discretizePixelYPosition(y):
    index = y//1
    return(index) 


'''

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
        if i > 300: wins += 10
        if i > 500: wins += 15
        if i > 700: wins += 20
        if i > 900: wins += 20
        if i > 1100: wins += 25
        if i > 1300: wins += 30
        if i > 1500: wins += 35
        mode = "human"
    else:
        mode = "none"
    env = gym.make("Acrobot-v1", render_mode = mode)
    wins += runEpisode(q_table) # Run episode and also add 1 to the number of wins if won in that episode
env.close



'''