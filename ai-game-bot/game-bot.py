# game-bot.py
# initial attempt at building a game playing AI bot

# before running the following modules need to be installed
# Python3
# brew install python3
# OpenAI libraries
# pip3 install gym
# pip3 install numpy incremental
# brew install golang libjpeg-turbo
# pip3 install universe


# docker should also be installed before running

import gym
import universe

env = gym.make('flashgames.NeonRace-v0')
env.configure(remotes=1) # create docker container

observation_n = env.reset()

while True:
    action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()
