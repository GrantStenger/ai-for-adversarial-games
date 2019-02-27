# AI in Adversarial Games

### Game Status
* Tic-tac-toe is fully built and plays perfectly. It is unbeatable. It needs to be optimized and code should be cleaner.
* Connect-4 is built and AI development is in progress.
* Pyramix is built and a human-level heuristic-greedy player has been implemented.
* Texas Hold'em is currently being rebuilt with better optimization.
* Chess, Black Jack, checkers, dollar-auction, and prisoners dilemma are currently unbuilt.

### Proposed Time Line
* By Sunday, Nov. 11:
  * minimax implemented for connect 4 + heuristics
  * test RL on simple game
  * theoretical results on pyramix (computational complexity etc.)
  * poker fully debugged and pristine
* By Sunday, Nov. 18:
  * super human pyramix player
  * connect 4 solved
  * RL tested on pyramix
* By Sunday, Nov. 25:
  * our "above and beyond week"
  * shocking new discoveries
  * world is changed for the better
* By Sunday, Dec. 2:
  * presentation made
  * final touches

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

### The General Path:
* Ultimate goal: the stock market is the most competitive adversarial game in the world.
* To get there, we need to be really, really good players.
* Games like Catan are stochastic and require sharp long-term planning.
* Games like texas hold'em require intelligent understanding of probability spaces and bankroll management.
* We plan to build AIs for these games with classical techniques like minimax w/ alpha-beta pruning and to beat them with modern reinforcement learning techniques.
* To get minimax working well, we're attempting to beat a simpler purely deterministic game like connect-4.
* If we're going to try to make minimax work on connect-4, we better be sure that we can get minimax working ~very~ well on tic-tac-toe.
* We're also solving a more esoteric game called pyramix which seems to be a great mix of AI planning and reinforcement learning.

### Interesting Resources:
* [CS234: Reinforcement Learning](http://web.stanford.edu/class/cs234/index.html)
* [Efficient Reinforcement Learning in Adversarial Games](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6495112)
* [GANGs: Generative Adversarial Network Games](https://arxiv.org/abs/1712.00679)
* [Exploration by Random Network Distillation](https://arxiv.org/abs/1810.12894)
* [Reinforcement Learning with Prediction-Based Rewards](https://blog.openai.com/reinforcement-learning-with-prediction-based-rewards/#RNDjump)
* [Human-level control through deep reinforcement learning](https://www.nature.com/articles/nature14236)
* [Deep RL Bootcamp](https://sites.google.com/view/deep-rl-bootcamp/lectures)

## RL Overview (From Stanford CS234 [1])
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

### Techniques to Test
* DQN
* Policy Gradients and Actor Critic
* TRPO and PPO
* SVG, DDPG, and Stochastic Computation Graphs
* RND

## Sources
[1] [Stanford CS234](http://web.stanford.edu/class/cs234/slides/cs234_2018_l1.pdf)
