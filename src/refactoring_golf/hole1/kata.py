# ruff: noqa
class Game:
    def __init__(self):
        self.last_symbol = " "
        self.board = Board()

    def play(self, symbol, x, y):
        # if first move
        if self.last_symbol == " ":
            # if player is X
            if symbol == "O":
                raise Exception("Invalid first player")
        # if not first move but player repeated
        elif symbol == self.last_symbol:
            raise Exception("Invalid next player")
        # if not first move but play on an already played tile
        elif self.board.tile_at(x, y).symbol != " ":
            raise Exception("Invalid position")

        # update game state
        self.last_symbol = symbol
        self.board.add_tile_at(symbol, x, y)

    def winner(self):
        # if the positions in first row are taken
        if (
            self.board.tile_at(0, 0).symbol != " "
            and self.board.tile_at(0, 1).symbol != " "
            and self.board.tile_at(0, 2).symbol != " "
        ):
            # if first row is full with same symbol
            if (
                self.board.tile_at(0, 0).symbol == self.board.tile_at(0, 1).symbol
                and self.board.tile_at(0, 2).symbol == self.board.tile_at(0, 1).symbol
            ):
                return self.board.tile_at(0, 0).symbol

        # if the positions in first row are taken
        if (
            self.board.tile_at(1, 0).symbol != " "
            and self.board.tile_at(1, 1).symbol != " "
            and self.board.tile_at(1, 2).symbol != " "
        ):
            # if middle row is full with same symbol
            if (
                self.board.tile_at(1, 0).symbol == self.board.tile_at(1, 1).symbol
                and self.board.tile_at(1, 2).symbol == self.board.tile_at(1, 1).symbol
            ):
                return self.board.tile_at(1, 0).symbol

        # if the positions in first row are taken
        if (
            self.board.tile_at(2, 0).symbol != " "
            and self.board.tile_at(2, 1).symbol != " "
            and self.board.tile_at(2, 2).symbol != " "
        ):
            # if middle row is full with same symbol
            if (
                self.board.tile_at(2, 0).symbol == self.board.tile_at(2, 1).symbol
                and self.board.tile_at(2, 2).symbol == self.board.tile_at(2, 1).symbol
            ):
                return self.board.tile_at(2, 0).symbol

        return " "


class Tile:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol


class Board:
    def __init__(self):
        self.plays = []
        for i in range(3):
            for j in range(3):
                self.plays.append(Tile(i, j, " "))

    def tile_at(self, x, y):
        return next(tile for tile in self.plays if tile.x == x and tile.y == y)

    def add_tile_at(self, symbol, x, y):
        tile = Tile(x, y, symbol)  # noqa: F841 - dead code, mirrors ts-kata source

        next(t for t in self.plays if t.x == x and t.y == y).symbol = symbol
