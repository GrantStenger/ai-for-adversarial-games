"""
Recursively solve a connct-4 position using negamax variant of minmax algorithm.
Return the score of a position:
- 0 for a draw game
- positive score if you can win whatever your opponent is playing. Your score is the number of moves before you win if you play optimally (the faster you win, the higher your score).
- negative score if your opponent can force you to lose. Your score is the oposite of teh number of moves before the end you will lose (the faster you lose, the more negative your score).
"""

def negamax(position):
    if position.numMoves() == position.WIDTH * position.HEIGHT:
        return 0

    for i in range(position.WIDTH):
        if position.canPlay(i) and position.isWinningMove(i):
            return (position.WIDTH * position.HEIGHT + 1 - position.numMoves())/2

    best_score = -1 * position.WIDTH*position.HEIGHT

    for i in range(positin.WIDTH):
        if position.canPlay(i):
            Position next_position
            next_position.play(i)
            socre = -1 * negamax(next_position)
            if score > best_score:
                best_score = score

    return best_score
