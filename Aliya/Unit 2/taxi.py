import gymnasium as gym
import numpy as np
import pygame
import random




# Create environment
env = gym.make("Taxi-v3", render_mode = "human")

state, info = env.reset()

print(state)
#((taxi_row * 5 + taxi_col) * 5 + passenger_location) * 4 + destination) = state


for i in range(1):
    env.render()
    print(state)
    action = env.action_space.sample(info["action_mask"])
    print(action)
    env.step(action)
    state, info = env.reset()
    print(info)
    
    

