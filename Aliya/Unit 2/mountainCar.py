import gymnasium as gym

# 0 - acclerate left; 1 - don't accelerate; 2 - accelerate right
ACTIONS = [0, 1, 2]

# Initialize the mountain car environment from gymnasium
env = gym.make("MountainCar-v0", render_mode = "human")
env.reset()

for i in range(20):
    env.step(2)
