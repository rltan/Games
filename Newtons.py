import BoardGame.Board as bg
import sys


class Ball(object):

    def __init__(self, color):
        self.color = color
        self.symbol = self.get_symbol(color)

    def get_symbol(self, color):
        return color[0]


class Player(object):

    def __init__(self, name, color):
        self.name = name
        self.ball = Ball(color)


class Newtons(object):

    def __init__(self):
        self.board = bg.Board(7, 7)
        self.player_1 = Player("Raymond", "Red")
        self.player_2 = Player("Jasmine", "Blue")
        self.turn = True

    def switch_player(self):
        if self.turn:
            self.turn = False
        else:
            self.turn = True

    def winner(self):
        counter = {'p1': 0, 'p2': 0}

        # Check rows for winner
        for row in self.board.board:
            for x_position in row:
                if x_position == self.player_1.ball.symbol:
                    counter['p1'] += 1
                    counter['p2'] = 0
                elif x_position == self.player_2.ball.symbol:
                    counter['p2'] += 1
                    counter['p1'] = 0
                else:
                    continue

        if counter['p1'] == 5:
            self._print_winner(self.player_1.name)
            return True
        elif counter['p2'] == 5:
            self._print_winner(self.player_2.name)
            return True
        else:
            counter = {'p1': 0, 'p2': 0}

        # Check cols for winner
        for x_position in range(7):
            for row in self.board.board:
                if row[x_position] == self.player_1.ball.symbol:
                    counter['p1'] += 1
                    counter['p2'] = 0
                elif row[x_position] == self.player_2.ball.symbol:
                    counter['p2'] += 1
                    counter['p1'] = 0
                else:
                    continue

        if counter['p1'] == 5:
            self._print_winner(self.player_1.name)
            return True
        elif counter['p2'] == 5:
            self._print_winner(self.player_2.name)
            return True
        else:
            return False

        # Check diagonal

    def _print_winner(self, name):
        print("{} is the winner!!!".format(name))

    def take_turn(self, player):
        columns = [0, 1, 2, 3, 4, 5, 6]
        print("{}, enter an option (0-6): ".format(player.name), end="")
        column = int(input())

        if column in columns:
            for row in range(6, -1, -1):
                # print("Row: {}".format(row))
                if self.board.board[row][column] == " ":
                    self.board.board[row][column] = player.ball.symbol
                    break
                elif row == 0 and self.board.board[row][column] != "":
                    print("Column is full, choose a different column")
                    self.take_turn(player.ball)
                else:
                    continue


if __name__ == "__main__":
    game = Newtons()
    turn_counter = 0
    while not game.winner():
        if game.turn:
            game.take_turn(game.player_1)
        else:
            game.take_turn(game.player_2)
        game.board.print_board()

        turn_counter += 1
        game.switch_player()



