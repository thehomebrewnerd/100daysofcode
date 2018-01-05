# game-bot.py
# initial attempt at building a game playing AI bot

import gym

env = gym.make('MsPacman-v0')
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
