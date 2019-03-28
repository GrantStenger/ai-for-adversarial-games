class Game:
    def __init__(self, board_size):
        self.board = Board(board_size)
        print(self.board)

    def play(self):
        pass

class Board:
    def __init__(self, board_size):
        self.board = []
        for i in range(board_size):
            row = []
            for j in range(board_size):
                row.append(Cell())
            self.board.append(row)

    def __str__(self):
        output = ""
        for row in self.board:
            for cell in row:
                output += cell + " "
            output += "\n"
        return output

class Cell:
    def __init__(self):
        self.is_viewed = False

    def __repr__(self):
        if self.is_viewed:
            return "1"
        else:
            return "0"

    def __str__(self):
        if self.is_viewed:
            return "1"
        else:
            return "0"
