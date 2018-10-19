# Connect-4

### Status
* Playable in console by a human
* Game is playable for any generalized board size

### To Do's:
* Implement MiniMax
* Implement Alpha-Beta Pruning
* Build Javascript front-end
* Optimize runtime (encode boards as bits, potentially rewrite in C++, be more careful with recursion)
* Generalize connect-4 board size
* Simulator works best with no printing, human experience better with it => make two versions: optimized and comfortable
* What's the best way to internally represent board configurations within each player as they imagine the changes made for each possible choice?

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
* Don't fill a slot under a game winning move for yourself (ie penalize for losing long chains). Never play directly below your own game winning space.
* Build 7s
* Fork your threats whenever possible
* Threat analysis
  * Odd threats vs even threats

### Interesting Math
* How many possible unique connect-4 games are there?
  * 7^42 is an upper-bound on the number of possible connect-4 games
    * Maximum 7 choices per turn
    * Maximum 6*7 possible turns (board is 6 by 7)
  * At most 4^24 + 7^21 - 4^12 games will be reflectively symmetrical
    * Horizontal symmetry: 4 column choices and 4*6 possible turns
    * Vertical symmetry: 7 column choices and 7*3 possible turns
    * Both Horizontally and Vertically symmetrical: 4 column choices and 4*3 possible turns

### Background
* Pascal Pons wrote a great connect-4 solver here: http://blog.gamesolver.org/
* Briefly about the game:
  * Two player game
  * Perfect information
  * Deterministically turn based (what happens when turns are random?)
  * 7 by 6 board (what happens when this changes?)
  * The winner is the person who creates a chain of 4 in a row
  * If the board completely fills up before a player gets four in a row, it's a tie
  * Each player chooses a column to place a tile in and it drops down to the lowest free slot
  * Strongly solved in 1988 by James D. Allen and Victor Allis
    * Allis solved it in his thesis here: http://www.informatik.uni-trier.de/~fernau/DSL0607/Masterthesis-Viergewinnt.pdf
    * Allen solved in in this book: http://blog.gamesolver.org/data/expert_play_in_connect_4.html
    * At the time, a brute force solution was not possible. They solved it with a combinatorial solution with a knowledge database
  * John Tromp was the first to solve the game with a proper brute force solution in 1995. He's solved a bunch of board possibilities here: https://tromp.github.io/c4/c4.html

### Questions
* When two random players are playing, how much more likely is player1 going to win? How does this change as the size of the board changes? What is the proper function?
* How likely is a tie with random players? How does this change as the board size changes? What is the true mathematical function underlying this?
  * 8 by 8: 1,000,000 games
    * Player 1 wins: 557159
    * Player 2 wins: 442825
    * Ties: 16
* What is the average number of moves until a win given a certain board size given random players? What is the distribution? How does the distribution change with board size?
* How does the game change when turns are determined randomly? What happens when a player gets a turn 55% of the time?
* Given a width, is there an expected value height that the game will get to?
* If the board size grows in O(n^2), will the number of tiles grow in O(nlogn)

### Building a Solver
* Each position should be given a score
  * Positive in current player should win, 0 if tie, negative if current player should lose
  * Value 1 if current player wins with her last stone, value 2 if second to last, etc.
* Comparing solvers
  * Have them play against each other, output % wins for each player
  * Compare move execution time (on the same machine)
