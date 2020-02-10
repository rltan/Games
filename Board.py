class Board(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.construct_board()

    def construct_board(self):
        space = " "
        board = []
        row = []

        for y in range(self.height):
            for x in range(self.width):
                row.append(space)
            board.append(row)
            row = []

        return board

    def print_board(self):
        for y in range(self.height):
            print(self.board[y])

