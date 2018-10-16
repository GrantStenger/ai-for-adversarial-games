# Connect-4

### Status
* Playable in console by a human

### To Do's:
* Implement MiniMax
* Implement Alpha-Beta Pruning
* Build Javascript front-end
* Optimize runtime (encode boards as bits, potentially rewrite in C++, be more careful with recursion)

### Game Plan
1. Build Random Player
2. Build player who will always make immediately winning moves, otherwise random
3. Build player who will block opponent from making immediately winning moves
4. Build player who explores games to depth d and uses minimax with a specified heuristic to choose which move to play

### Possible Heuristics
* Chains of length 1 worth 2 point, chains of length 2 worth 4 points, chains of length 3 worth 16 points, chains of length 4 worth 256 points
* Minimize opponents chain score
* Maximize your chain score minus opponents chain score
* Maximize central control (how should we weight values? 1234321?)
* Chains with open ends are more valuable than blocked ends (set up multi-directional attacks)
* Don't fill a slot under a game winning move for yourself (ie penalize for losing long chains)
* Build 7s
