import gym
import matplotlib.pyplot as plt

observations = []
rewards = []

def run(model, maxSteps=1000):
    env = gym.make(model)
    env.reset()
    for step in range(maxSteps):
        env.render()
        observation, reward, done, info = env.step(env.action_space.sample())
        observations.append(observation)
        rewards.append(reward)
        # if done:
            # print("Finished after", step+1, "time steps.")
            # break

def rewardHistory():
    plt.plot(rewards)
    plt.show()
