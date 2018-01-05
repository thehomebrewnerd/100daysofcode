# game-bot.py
# initial attempt at building a game playing AI bot

import gym

env = gym.make('MsPacman-v0')
obs = env.reset()
reward_sum = 0;

for _ in range(1000):
    env.render()
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    reward_sum += reward
    print(reward_sum, done, action)
