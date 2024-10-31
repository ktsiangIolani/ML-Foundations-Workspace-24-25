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
for y in range

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


