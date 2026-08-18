# ruff: noqa: ANN202, ANN204, EM101, SIM102, TRY002, TRY003
FIRST_ROW = 0
SECOND_ROW = 1
THIRD_ROW = 2
FIRST_COLUMN = 0
SECOND_COLUMN = 1
THIRD_COLUMN = 2

PLAYER_O = "O"
NO_PLAYER = " "


class Game:
    def __init__(self):
        self.last_player = NO_PLAYER
        self.board = Board()

    def play(self, player, x, y):
        self._validate_first_move(player)
        self._validate_player(player)
        self._validate_position_is_empty(x, y)

        self._update_last_player(player)
        self._update_board(player, x, y)

    def _validate_first_move(self, player):
        if self.last_player == NO_PLAYER:
            if player == PLAYER_O:
                raise Exception("Invalid first player")

    def _validate_player(self, player):
        if player == self.last_player:
            raise Exception("Invalid next player")

    def _validate_position_is_empty(self, x, y):
        if self.board.tile_at(x, y).is_not_empty:
            raise Exception("Invalid position")

    def _update_last_player(self, player):
        self.last_player = player

    def _update_board(self, player, x, y):
        self.board.add_tile_at(player, x, y)

    def winner(self):
        return self.board.find_row_full_with_same_player()


class Tile:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player

    @property
    def is_not_empty(self):
        return self.player != NO_PLAYER

    def has_same_player_as(self, other):
        return self.player == other.player

    def has_same_coordinates_as(self, other):
        return self.x == other.x and self.y == other.y

    def update_player(self, new_player):
        self.player = new_player


class Board:
    def __init__(self):
        self.plays = []
        for x in range(FIRST_ROW, THIRD_ROW + 1):
            for y in range(FIRST_COLUMN, THIRD_COLUMN + 1):
                self.plays.append(Tile(x, y, NO_PLAYER))

    def tile_at(self, x, y):
        return next(t for t in self.plays if t.has_same_coordinates_as(Tile(x, y, NO_PLAYER)))

    def add_tile_at(self, player, x, y):
        tile = Tile(x, y, player)
        next(t for t in self.plays if t.has_same_coordinates_as(tile)).update_player(player)

    def find_row_full_with_same_player(self):
        if self._is_row_full(FIRST_ROW) and self._is_row_full_with_same_player(FIRST_ROW):
            return self.tile_at(FIRST_ROW, FIRST_COLUMN).player

        if self._is_row_full(SECOND_ROW) and self._is_row_full_with_same_player(SECOND_ROW):
            return self.tile_at(SECOND_ROW, FIRST_COLUMN).player

        if self._is_row_full(THIRD_ROW) and self._is_row_full_with_same_player(THIRD_ROW):
            return self.tile_at(THIRD_ROW, FIRST_COLUMN).player

        return NO_PLAYER

    def _is_row_full(self, row):
        return (
            self.tile_at(row, FIRST_COLUMN).is_not_empty
            and self.tile_at(row, SECOND_COLUMN).is_not_empty
            and self.tile_at(row, THIRD_COLUMN).is_not_empty
        )

    def _is_row_full_with_same_player(self, row):
        return self.tile_at(row, FIRST_COLUMN).has_same_player_as(
            self.tile_at(row, SECOND_COLUMN)
        ) and self.tile_at(row, THIRD_COLUMN).has_same_player_as(self.tile_at(row, SECOND_COLUMN))
