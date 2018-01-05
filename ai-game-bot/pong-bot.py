import gym

env = gym.make("Pong-v0")
observation = env.reset()
done = False

while not done:
    env.render()
    obs, reward, done, info = env.step(env.action_space.sample())
