from board import Board


class Game:
    def __init__(self, players):
        self.players = players
        self.board = Board()
        self.current_player = 0
        self.winner = 0

    def play(self):
        while self.winner is 0:
            self.board.show()
            self.players[self.current_player].move(self.board)
            self.current_player = (
                self.current_player + 1) % len(self.players)
            self.winner = self.board.check_win()
        self.board.show()
        print("Player %d wins!" % self.winner)
