import gymnasium as gym
import numpy as np
import random

ACTIONS = [0, 1, 2, 3]  # the actions we can take

def discretizePositions(xposition, yposition):
    Yindex = (yposition + 2.5) // 0.25 # scale Y position
    Xindex = (xposition + 2.5) // 0.25 # scale X position
    return int(Xindex), int(Yindex)

def discretizeVelocity(Xvelocity, Yvelocity):
    Xvelocityindex = (Xvelocity + 10) // 1
    Yvelocityindex = (Yvelocity + 10) // 1
    Xvelocityindex = min(19, max(0, int(Xvelocityindex))) # keep it between 0 and 19
    Yvelocityindex = min(19, max(0, int(Yvelocityindex))) # keep it between 0 and 19
    return Xvelocityindex, Yvelocityindex

def discretizeAngles(angle):
    angleIndex = (angle + np.pi) // (2 * np.pi / 18) #scales the angle into indexes or buckets
    angleIndex = min(17, max(0, int(angleIndex)))# keep it between 0 and 17
    return angleIndex

def discretizeAngularVelocity(angularVelocity):
    angVIndex = (angularVelocity + 10) // 1
    angVIndex = min(19, max(0, int(angVIndex)))
    return angVIndex
#initializes the Qtable with all 0s at first
def initQTable():
    return np.zeros((4, 20, 20, 20, 20, 18, 20, 2, 2))

def getMaxFutureValue(q_table, xposition, yposition, Xvelocity, Yvelocity, angle, angularVelocity, left_leg, right_leg):
    Xpos, Ypos = discretizePositions(xposition, yposition) # turn all the state values into numbers we can use
    Xvel, Yvel = discretizeVelocity(Xvelocity, Yvelocity)
    angleDiscrete = discretizeAngles(angle)
    angVDiscrete = discretizeAngularVelocity(angularVelocity)
    left_leg_int = int(left_leg)
    right_leg_int = int(right_leg)
    
    bestActionValue = -100 ## start with a low value to compare
    for action in ACTIONS: # check all possible actions
        q_value = q_table[action][Xpos][Ypos][Xvel][Yvel][angleDiscrete][angVDiscrete][left_leg_int][right_leg_int]
        bestActionValue = max(bestActionValue, q_value) #find all best possible action values
    
    return bestActionValue

def updateQTable(q_table, state, reward, action, new_state):
    learningRate = 0.1
    discountFactor = 0.6
    
    x, y, xV, yV, angle, angVel, left_leg, right_leg = new_state
    Xpos, Ypos = discretizePositions(x, y)
    Xvel, Yvel = discretizeVelocity(xV, yV)
    angleDiscrete = discretizeAngles(angle)
    angVDiscrete = discretizeAngularVelocity(angVel)
    
    left_leg_int = int(left_leg)
    right_leg_int = int(right_leg)
    #this is the old q value
    oldQValue = q_table[action][Xpos][Ypos][Xvel][Yvel][angleDiscrete][angVDiscrete][left_leg_int][right_leg_int]
    #finds the future and max future vallue
    maxFutureValue = getMaxFutureValue(q_table, x, y, xV, yV, angle, angVel, left_leg, right_leg)
    #updates the Qvalue
    q_table[action][Xpos][Ypos][Xvel][Yvel][angleDiscrete][angVDiscrete][left_leg_int][right_leg_int] = oldQValue + learningRate * (reward + discountFactor * maxFutureValue - oldQValue)

def runEpisode(q_table, render=False):
    state, _ = env.reset() 
    running = True
    while running:
        action = random.choice(ACTIONS)
        new_state, reward, terminated, truncated, info = env.step(action)
        
        x, y, xV, yV, angle, angVel, left_leg, right_leg = new_state
        Xpos, Ypos = discretizePositions(x, y)
        Xvel, Yvel = discretizeVelocity(xV, yV)
        angleDiscrete = discretizeAngles(angle)
        angVDiscrete = discretizeAngularVelocity(angVel)
        
        left_leg_int = int(left_leg)
        right_leg_int = int(right_leg)
# if the agent reaches the goal, give a big reward
        if -0.5 < x < 0.5 and y < 0.1 and y > -0.1 and abs(xV) < 0.5 and abs(yV) < 0.5:
            reward = 400
            print("GOAL REACHED YAY!!")
        elif terminated:
            reward = -100 #if the game ends it will give it a big penalty
        
        oldQValue = q_table[action][Xpos][Ypos][Xvel][Yvel][angleDiscrete][angVDiscrete][left_leg_int][right_leg_int]
        
        maxFutureValue = getMaxFutureValue(q_table, x, y, xV, yV, angle, angVel, left_leg, right_leg)
        # update the Q-table based on what just happened
        q_table[action][Xpos][Ypos][Xvel][Yvel][angleDiscrete][angVDiscrete][left_leg_int][right_leg_int] = oldQValue + 0.1 * (reward + 0.6 * maxFutureValue - oldQValue)
        
        if render:
            env.render() 
        
        if terminated or truncated:
            running = False
        
        state = new_state
#setting up of the lunar lander game
env = gym.make("LunarLander-v3", render_mode="human", continuous=False, gravity=-10.0, enable_wind=False, wind_power=15.0, turbulence_power=1.5)
q_table = initQTable()
episodes = 5000 #number of episodes it will run

for i in range(episodes):
    print(f"Episode {i + 1}")
    env.reset()
    
    render = (i % 10 == 0) #this means that it will render every 100th episode
    
    runEpisode(q_table, render)

env.close()
