# AI in Adversarial Games

### Game Status
* Tic-tac-toe is fully built and plays perfectly. It is unbeatable. It needs to be optimized and code should be cleaner.
* Connect-4 is built and AI development is in progress.
* Pyramix is currently being built.
* Texas Hold'em is currently being rebuilt with better optimization.
* Chess, Black Jack, checkers, dollar-auction, and prisoners dilemma are currently unbuilt.

### Algorithms to test
* Minimax + Alpha-Beta Pruning
* Deep Q Learning
* Deep Deterministic Policy Gradients
* Actor Critique
* Monte Carlo Tree Search

### To Do's:
* Test Transfer Learning
* Multi-Agent Reinforcement Learning
* Try Imitation Learning

### Interesting Resources:
* [CS234: Reinforcement Learning](http://web.stanford.edu/class/cs234/index.html)
* [Efficient Reinforcement Learning in Adversarial Games](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6495112)
* [GANGs: Generative Adversarial Network Games](https://arxiv.org/abs/1712.00679)

## Overview (From Stanford CS234 [1])
* Reinforcement Learning: Learning to make good sequences of decisions.
  * Optimization: Find an optimal way to make decisions––yielding best outcomes.
  * Delayed consequences: When planning, decisions involve reasoning about not just immediate benefit of a decision but how its longer term ramifications; when learning, temporal credit assignment is hard (what caused later high or low rewards?).
  * Exploration: Learning about the world by making decisions (agent as scientist); Censored data, only get a reward (label) for decision made.
  * Generalization: Policy is mapping from past experience to action.
AI Planning (vs RL)
  * Minimax is AI planning, no need for exploration, already given model of how decisions impact world
  * RL needs to explore the world.
Imitation Learning
  * Reduces RL to Supervised Learning
  * Avoids exploration problem
  * Limitations: can be expensive to collect data

## Sources
[1] [Stanford CS234](http://web.stanford.edu/class/cs234/slides/cs234_2018_l1.pdf)
