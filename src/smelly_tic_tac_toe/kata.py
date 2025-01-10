class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = ' '

class Board:
    def __init__(self):
        self.plays = []
        for i in range(3):
            for j in range(3):
                self.plays.append(Tile(i, j))

    def tile_at(self, x, y):
        return next(tile for tile in self.plays if tile.x == x and tile.y == y)

    def add_tile_at(self, symbol, x, y):
        tile = self.tile_at(x, y)
        tile.symbol = symbol

class Game:
    def __init__(self):
        self.last_symbol = ' '
        self.board = Board()
        self.winner = ' '

    def play(self, symbol, x, y):
        # if first move
        if self.last_symbol == ' ':
            # if player is O
            if symbol == 'O':
                raise Exception("Invalid first player")
        # if not first move but player repeated
        elif symbol == self.last_symbol:
            raise Exception("Invalid next player")
        # if not first move but play on an already played tile
        elif self.board.tile_at(x, y).symbol != ' ':
            raise Exception("Invalid position")

        # update game state
        self.last_symbol = symbol
        self.board.add_tile_at(symbol, x, y)

    def determine_winner(self):
        # if the positions in first row are taken
        if (
            self.board.tile_at(0, 0).symbol != ' ' and
            self.board.tile_at(0, 1).symbol != ' ' and
            self.board.tile_at(0, 2).symbol != ' '
        ):
            # if first row is full with same symbol
            if (
                self.board.tile_at(0, 0).symbol == self.board.tile_at(0, 1).symbol and
                self.board.tile_at(0, 2).symbol == self.board.tile_at(0, 1).symbol
            ):
                return self.board.tile_at(0, 0).symbol

        # if the positions in middle row are taken
        if (
            self.board.tile_at(1, 0).symbol != ' ' and
            self.board.tile_at(1, 1).symbol != ' ' and
            self.board.tile_at(1, 2).symbol != ' '
        ):
            # if middle row is full with same symbol
            if (
                self.board.tile_at(1, 0).symbol == self.board.tile_at(1, 1).symbol and
                self.board.tile_at(1, 2).symbol == self.board.tile_at(1, 1).symbol
            ):
                return self.board.tile_at(1, 0).symbol

        # if the positions in last row are taken
        if (
            self.board.tile_at(2, 0).symbol != ' ' and
            self.board.tile_at(2, 1).symbol != ' ' and
            self.board.tile_at(2, 2).symbol != ' '
        ):
            # if last row is full with same symbol
            if (
                self.board.tile_at(2, 0).symbol == self.board.tile_at(2, 1).symbol and
                self.board.tile_at(2, 2).symbol == self.board.tile_at(2, 1).symbol
            ):
                return self.board.tile_at(2, 0).symbol

        return ' '