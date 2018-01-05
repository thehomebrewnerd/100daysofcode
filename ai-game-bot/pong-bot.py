import gym

env = gym.make("Pong-v0")
observation = env.reset()

for _ in range(1000):
    env.render()
    obs, reward, done, info = env.step(env.action_space.sample())
