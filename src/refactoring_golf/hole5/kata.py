# ruff: noqa
FIRST_ROW = 0
SECOND_ROW = 1
THIRD_ROW = 2
FIRST_COLUMN = 0
SECOND_COLUMN = 1
THIRD_COLUMN = 2

PLAYER_O = "O"
EMPTY_PLAY = " "


class Game:
    def __init__(self):
        self.last_symbol = EMPTY_PLAY
        self.board = Board()

    def play(self, symbol, x, y):
        self._validate_first_move(symbol)
        self._validate_player(symbol)
        self._validate_position_is_empty(x, y)

        self._update_last_player(symbol)
        self._update_board(symbol, x, y)

    def _validate_first_move(self, player):
        if self.last_symbol == EMPTY_PLAY:
            if player == PLAYER_O:
                raise Exception("Invalid first player")

    def _validate_player(self, player):
        if player == self.last_symbol:
            raise Exception("Invalid next player")

    def _validate_position_is_empty(self, x, y):
        if self.board.tile_at(x, y).symbol != EMPTY_PLAY:
            raise Exception("Invalid position")

    def _update_last_player(self, player):
        self.last_symbol = player

    def _update_board(self, player, x, y):
        self.board.add_tile_at(player, x, y)

    def winner(self):
        if self._is_row_full(FIRST_ROW) and self._is_row_full_with_same_symbol(FIRST_ROW):
            return self.board.tile_at(FIRST_ROW, FIRST_COLUMN).symbol

        if self._is_row_full(SECOND_ROW) and self._is_row_full_with_same_symbol(SECOND_ROW):
            return self.board.tile_at(SECOND_ROW, FIRST_COLUMN).symbol

        if self._is_row_full(THIRD_ROW) and self._is_row_full_with_same_symbol(THIRD_ROW):
            return self.board.tile_at(THIRD_ROW, FIRST_COLUMN).symbol

        return EMPTY_PLAY

    def _is_row_full(self, row):
        return (
            self.board.tile_at(row, FIRST_COLUMN).symbol != EMPTY_PLAY
            and self.board.tile_at(row, SECOND_COLUMN).symbol != EMPTY_PLAY
            and self.board.tile_at(row, THIRD_COLUMN).symbol != EMPTY_PLAY
        )

    def _is_row_full_with_same_symbol(self, row):
        return (
            self.board.tile_at(row, FIRST_COLUMN).symbol == self.board.tile_at(row, SECOND_COLUMN).symbol
            and self.board.tile_at(row, THIRD_COLUMN).symbol == self.board.tile_at(row, SECOND_COLUMN).symbol
        )


class Tile:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol


class Board:
    def __init__(self):
        self.plays = []
        for i in range(FIRST_ROW, THIRD_ROW + 1):
            for j in range(FIRST_COLUMN, THIRD_COLUMN + 1):
                self.plays.append(Tile(i, j, EMPTY_PLAY))

    def tile_at(self, x, y):
        return next(tile for tile in self.plays if tile.x == x and tile.y == y)

    def add_tile_at(self, symbol, x, y):
        next(t for t in self.plays if t.x == x and t.y == y).symbol = symbol
