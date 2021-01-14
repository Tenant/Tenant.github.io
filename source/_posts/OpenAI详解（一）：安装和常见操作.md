---
title: OpenAI详解（一）：安装和常见操作
date: 2021-01-14 13:50:09
categories:
  - 深度学习
  - OpenAI
tags:
  - 深度学习
  - OpenAI
description: 本文总结了OpenAI的入门知识。
---

# OpenAI

## 1. Gym

[Homepage](https://gym.openai.com/)

[Github](https://github.com/openai/gym)

[Docs](https://gym.openai.com/docs/)

[Open AI. Greg Brockman, Vicki Cheung, Ludwig Pettersson, etc. 2016.](http://papers-repo.oss-cn-beijing.aliyuncs.com/Open-AI-gym.pdf) URL: https://arxiv.org/abs/1606.01540

### 1.1 Install

```bas
conda create -n gym python=3.5
source active gym
pip install gym
# pip install gym[all]
```

### 1.2 Environments

```python
import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
```

### 1.3 Register

It's very easy to add your own environments to the registry, and thus make them available for $gym.make()$: just $register()$ them at load time.

### 1.4 Demo

```python
import gym

env=gym.make('CartPole-v0')
env=env.unwrapped

print(env.action_space)
print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)
printt(env.action_space.n)
print(env.observation_space.shape[0])
```

