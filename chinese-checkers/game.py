from board import Board


class Game:
    def __init__(self, players):
        self.players = players
        self.board = Board()
        self.current_player_index = 0
        self.winner = 0

    def play(self):
        # Every turn check if there is a winner
        while self.winner == 0:
            self.board.show()
            print("Player: %d" % (self.current_player_index+1))
            # During this player's turn, they will be prompted to move
            self.players[self.current_player_index].make_turn(self.board)
            # Update the Game's current player
            self.current_player_index = (
                self.current_player_index + 1) % len(self.players)
            # Check if there is a winner
            self.winner = self.board.check_win()
        # self.board.show()
        print("Player %d wins!" % self.winner)
