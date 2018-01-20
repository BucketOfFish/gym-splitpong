# Test split pong environment with a random agent

import gym
import gym_splitpong
from OpenAIPackages import *

# env = gym.make("splitpong-v0")
# env.render()

runRandom("splitpong-v0", 10000)
