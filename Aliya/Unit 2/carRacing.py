import gymnasium as gym
import numpy as np
from gymnasium import ActionWrapper

env = gym.make("CarRacing-v3", render_mode = "human", continuous = False)
env.reset()

#state, info = env.reset()


print(env.action_space.__dict__)
action = env.action_space.sample()
print(type(action))

for i in range(1000):
    action = env.action_space.sample()
    env.step(action)
    print(action)
#env.step(print(action))
#print(action)
#print(state)

