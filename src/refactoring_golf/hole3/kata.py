# ruff: noqa: ANN202, ANN204, EM101, SIM102, TRY002, TRY003
class Game:
    def __init__(self):
        self.last_symbol = " "
        self.board = Board()

    def play(self, symbol, x, y):
        self._validate_first_move(symbol)
        self._validate_player(symbol)
        self._validate_position_is_empty(x, y)

        self._update_last_player(symbol)
        self._update_board(symbol, x, y)

    def _validate_first_move(self, player):
        if self.last_symbol == " ":
            if player == "O":
                raise Exception("Invalid first player")

    def _validate_player(self, player):
        if player == self.last_symbol:
            raise Exception("Invalid next player")

    def _validate_position_is_empty(self, x, y):
        if self.board.tile_at(x, y).symbol != " ":
            raise Exception("Invalid position")

    def _update_last_player(self, player):
        self.last_symbol = player

    def _update_board(self, player, x, y):
        self.board.add_tile_at(player, x, y)

    def winner(self):
        if self._is_first_row_full() and self._is_first_row_full_with_same_symbol():
            return self.board.tile_at(0, 0).symbol

        if self._is_second_row_full() and self._is_second_row_full_with_same_symbol():
            return self.board.tile_at(1, 0).symbol

        if self._is_third_row_full() and self._is_third_row_full_with_same_symbol():
            return self.board.tile_at(2, 0).symbol

        return " "

    def _is_first_row_full(self):
        return (
            self.board.tile_at(0, 0).symbol != " "
            and self.board.tile_at(0, 1).symbol != " "
            and self.board.tile_at(0, 2).symbol != " "
        )

    def _is_first_row_full_with_same_symbol(self):
        return (
            self.board.tile_at(0, 0).symbol == self.board.tile_at(0, 1).symbol
            and self.board.tile_at(0, 2).symbol == self.board.tile_at(0, 1).symbol
        )

    def _is_second_row_full(self):
        return (
            self.board.tile_at(1, 0).symbol != " "
            and self.board.tile_at(1, 1).symbol != " "
            and self.board.tile_at(1, 2).symbol != " "
        )

    def _is_second_row_full_with_same_symbol(self):
        return (
            self.board.tile_at(1, 0).symbol == self.board.tile_at(1, 1).symbol
            and self.board.tile_at(1, 2).symbol == self.board.tile_at(1, 1).symbol
        )

    def _is_third_row_full(self):
        return (
            self.board.tile_at(2, 0).symbol != " "
            and self.board.tile_at(2, 1).symbol != " "
            and self.board.tile_at(2, 2).symbol != " "
        )

    def _is_third_row_full_with_same_symbol(self):
        return (
            self.board.tile_at(2, 0).symbol == self.board.tile_at(2, 1).symbol
            and self.board.tile_at(2, 2).symbol == self.board.tile_at(2, 1).symbol
        )


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
        next(t for t in self.plays if t.x == x and t.y == y).symbol = symbol
