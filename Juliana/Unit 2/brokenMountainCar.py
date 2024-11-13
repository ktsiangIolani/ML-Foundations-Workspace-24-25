import gymnasium as gym
import numpy as np
import random

# --------------------------- BROKEN CODE FOR Q LEARNING (FIX 5 THINGS!) ---------------------------

ACTIONS = [0, 1, 2]
def discretizePosition(position):
    index = position + 1.2
    index = index // 0.1 
    return int(index)

def discretizeVelocity(velocity):
    index = velocity + 0.07
    index = index // 0.01
    return int(index)

def getMaxFutureValue(q_table, position, velocity):
    positionIndex = discretizePosition(position) 
    velocityIndex = discretizeVelocity(velocity)

    bestAction = -100
    actionNumber = random.choice(ACTIONS)
    for action in ACTIONS:
        if q_table[action][positionIndex][velocityIndex] > bestAction: 
            bestAction = q_table[action][positionIndex][velocityIndex]
            actionNumber = action
    return bestAction, actionNumber

def updateQTable(q_table, state, action, reward, new_state, episode):
    positionIndex = discretizePosition(state[0])
    velocityIndex = discretizeVelocity(state[1])
    if new_state[0] >= 0.5:
        q_table[action][positionIndex][velocityIndex]  = 100 
        print(f"GOAL REACHED ON EPISODE {episode}!!!")
    else:
        maxFutureVal, _ = getMaxFutureValue(q_table, new_state[0], new_state[1])
        currentQ = q_table[action][positionIndex][velocityIndex] 
        newQ = currentQ + 0.1*(reward + 0.9*maxFutureVal - currentQ) 
        q_table[action][positionIndex][velocityIndex] = newQ

# --------------------------- COMPLETED CODE FOR MOUNTAIN CAR ENV ---------------------------

def initQTable():
    return np.zeros((3, 18, 14))

def runEpisode(q_table, episode):
    state, _ = env.reset()
    running = True
    while running:
        _, actionNumber = getMaxFutureValue(q_table, state[0], state[1])
        new_state, reward, terminated, truncated, _ = env.step(actionNumber)
        updateQTable(q_table, state, actionNumber, reward, new_state, episode)
        if terminated or truncated:
            running = False
        state = new_state
    return q_table


if __name__ == "__main__":
    q_table = initQTable()
    episodes = 1000
    for i in range(episodes):
        if(i % 10 == 0):
            print("episode: ", i)
        if i % 100 == 0:
            mode = "human"
        else:
            mode = "none"
        env = gym.make("MountainCar-v0", render_mode=mode)
        q_table = runEpisode(q_table, i)
    env.close()