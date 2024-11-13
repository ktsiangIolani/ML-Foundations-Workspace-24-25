import gymnasium as gym
import numpy as np
import random


def discretizePosition(position): # discretize 4 data points
    index = position + 4.8
    index = index //0.1 
    #print("position: ", position, " ", index)
    return int(index)

def discretizeVelocity(velocity):
    index = velocity + 4.8
    index = index //0.1 
    #print("velocity: ", velocity, " ", index)
    return int(index)

def discretizeAngle(angle):
    index = angle + 0.418
    index = index //0.01 
    #print("angle: ", angle, " ", index)
    return int(index)

def discretizeAngleVelocity(angleVelocity):
    index = angleVelocity + 4.8
    index = index //0.1 
    #print("angleVelocity: ", angleVelocity, " ", index)
    return int(index)


def getMaxFutureValue(q_table, position, velocity, angle, angleVelocity):
    positionIndex = discretizePosition(position) 
    velocityIndex = discretizeVelocity(velocity)
    angleIndex = discretizeAngle(angle)
    angleVelocityIndex = discretizeAngleVelocity(angleVelocity)
    ACTIONS = [0, 1]
    bestAction = 0
    bestActionNumber = random.choice(ACTIONS) # 0, 1, or 2 based on the best action that we find
    for action in ACTIONS:
        if q_table[action][positionIndex][velocityIndex][angleIndex][angleVelocityIndex] > bestAction:
            bestAction = q_table[action][positionIndex][velocityIndex][angleIndex][angleVelocityIndex]
            bestActionNumber = action
    #print(bestActionNumber)
    return bestAction, bestActionNumber
    

def initQTable():
    #[action][positionIndex][velocityIndex][angleIndex][angleVelocityIndex]
    return np.zeros((2, 97, 97, 84, 97))

def updateQTable(q_table, state, reward, action, new_state, total_reward):
    position = state[0]
    velocity = state[1]
    angle = state[2]
    angleVelocity = state[3]
    newPosition = new_state[0]
    newVelocity = new_state[1]
    newAngle = new_state[2]
    newAngleVelocity = new_state[3]
    positionIndex = discretizePosition(position)
    velocityIndex = discretizeVelocity(velocity)
    angleIndex = discretizeAngle(angle)
    angleVelocityIndex = discretizeAngleVelocity(angleVelocity)

    learningRate = 0.4
    discountFactor = 0.4
    maxFutureValue, _ = getMaxFutureValue(q_table, newPosition, newVelocity, newAngle, newAngleVelocity)

    #print("params: ", action, positionIndex, velocityIndex, angleIndex, angleVelocityIndex)
    #print( "currnet qval", q_table[action][positionIndex][velocityIndex][angleIndex][angleVelocityIndex] )

    if total_reward > 100:
        reward =reward + 500
        print("goal has been reached!")

    qval = q_table[action][positionIndex][velocityIndex][angleIndex][angleVelocityIndex] + learningRate * (reward + discountFactor * maxFutureValue - q_table[action][positionIndex][velocityIndex][angleIndex][angleVelocityIndex])
    q_table[action][positionIndex][velocityIndex][angleIndex][angleVelocityIndex] = qval

    #print( "new qval", q_table[action][positionIndex][velocityIndex][angleIndex][angleVelocityIndex] )
def runEpisode(q_table):
    state, _ = env.reset()
    running = True
    total_reward = 0
    while running:
        _, actionNumber = getMaxFutureValue(q_table, state[0], state[1], state[2], state[3])
        new_state, reward, terminated, truncated, _ = env.step(actionNumber)
        updateQTable(q_table, state, reward, actionNumber, new_state, total_reward)
        #print("state: ", state)
        if terminated or truncated or total_reward >100:
            running = False
        state = new_state
        total_reward = reward + total_reward

    #print("totalreward", total_reward)
    

env = gym.make("CartPole-v0", render_mode="human")
state, _ = env.reset()

q_table = initQTable()
episodes = 10000
for i in range(episodes):
    if i % 1000 == 0:
        mode = "human"
    else:
        mode = "none"
        print("episode: ", i)
    env = gym.make("CartPole-v0", render_mode=mode)
    runEpisode(q_table)
    env.close()

#print(q_table)