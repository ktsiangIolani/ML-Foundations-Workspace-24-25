import gymnasium as gym

# 0 is accelerate left, 1 is dont accelerate, and 2 is accelerate right
ACTIONS = [0, 1, 2]
#initialize the mountain car environment from gymnasium
env = gym.make("MountainCar-v0", render_mode = "human")
env.reset()

for i in range(20):
    env.step(2)