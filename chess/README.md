# Chess

* Stockfish: "It's a pretty simple combination of static, positional analysis combined with dynamic branching to deliver "minimax" style evaluations."

* Great resources:
  * https://github.com/official-stockfish/Stockfish
  * https://www.youtube.com/watch?v=pUyURF1Tqvg
  * https://en.wikipedia.org/wiki/Stockfish
  * https://www.chessprogramming.org/Main_Page

### Ideas
* General Idea
  * While not checkmated:
	* Given a board position, construct a list of all possible legal moves,
	* Compare moves,
	* Select and play the “best” move.
* Choosing "the best move" (General Heuristics)
  * Choose moves which maximize squares accessible by your pieces
  * Minimize the number of squares accessible by opponent's pieces
  * Maximize the difference between the number of squares accessible by your pieces and the number of squares accessible by your opponent's pieces. (This 3-part construction will be applied to all future heuristics)
  * Based on the commonly accepted point system, maximize your points, minimize opponents points, => maximize difference between your points and their points.
  * Castle quickly
  * Develop minor pieces early
  * Capture undefended pieces
  * Capture pieces when there are more attackers than defenders
  * Note: predict if in opening, middle game, or endgame and adjust heuristics accordingly
  * Defend pieces that are being attacked
  * Minimize squares the opponent's king can move
  * Check your opponent's king
  * Make moves that "tie your pieces together"
  * Try to develop your pawns to queens
  * If there's a guaranteed "mate in X", mate.
* A specific example heuristic
  * H(x) = 200(K-K')
  * + 9(Q-Q')
  * + 5(R-R')
  * + 3(B-B' + N-N')
  * + 1(P-P')
  * - 0.2(D-D' + B-B' + I-I') (doubled, blocked, isolated)
  * + 0.1(M-M') (mobility i.e. number of legal moves)
  * + 0.5(BP-BP') (bishop pair)
  * + 0.1(ROF-ROF') (rook on open file)

### To Do's
* Make smaller chess games
* Find optimal piece positioning given an m by n board and see how this changes given access to different numbers of pieces.
* What if in chess you could place your pieces however you like so long as you are behind the midline. What if you can only use the back two rows?
* How valuable are each of the pieces?
