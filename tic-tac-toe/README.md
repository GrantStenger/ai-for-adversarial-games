# Building game-playing AI.
- Comptetative Zero-Sum Games
- Perfect Information
- Simple state representation

This tic-tac-toe AI is currently unbeatable.

To Do's: 
* Implement MiniMax 
* Implement Alpha-Beta Pruning
* Build Javascript front-end
* Optimize runtime (encode boards as bits, be more careful with recursion)

To get to chess, implement minimax with possibly some simple heuristics on connect-4. 

To understand minimax well, solve tic-tac-toe.

What happens when there's not perfect information? Poker for example.

Try some sort of minimax + heuristic algo on 2048.

This directory now also includes a C++ implementation of tic-tac-toe minimax.

s_0 // Initial state
player(s) // who's the player in state s
actions(s) // possible moves from state s
result(s, a) // the state after action a is taken on state s
terminal(s) // returns true if s is a terminal state
utility(s, p) // the objective funtion for state s for player p

Tic tac toe: fewer than 9! (362,880) terminal nodes
Chess: over 10^40