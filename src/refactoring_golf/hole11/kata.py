# ruff: noqa: ANN202, ANN204, EM101, SIM102, TRY002, TRY003
from typing import Literal, cast

Row = Literal[0, 1, 2]
Column = Literal[0, 1, 2]
Player = Literal[" ", "X", "O"]

FIRST_ROW: Row = 0
SECOND_ROW: Row = 1
THIRD_ROW: Row = 2
FIRST_COLUMN: Column = 0
SECOND_COLUMN: Column = 1
THIRD_COLUMN: Column = 2

PLAYER_O: Player = "O"
NO_PLAYER: Player = " "


class Game:
    def __init__(self):
        self.last_player: Player = NO_PLAYER
        self.board = Board()

    def play(self, player: Player, x: Row, y: Column):
        self._validate_first_move(player)
        self._validate_player(player)
        self._validate_position_is_empty(x, y)

        self._update_last_player(player)
        self._update_board(Tile(x, y, player))

    def _validate_first_move(self, player: Player):
        if self.last_player == NO_PLAYER:
            if player == PLAYER_O:
                raise Exception("Invalid first player")

    def _validate_player(self, player: Player):
        if player == self.last_player:
            raise Exception("Invalid next player")

    def _validate_position_is_empty(self, x: Row, y: Column):
        if self.board.is_tile_played_at(x, y):
            raise Exception("Invalid position")

    def _update_last_player(self, player: Player):
        self.last_player = player

    def _update_board(self, tile: "Tile"):
        self.board.add_tile_at(tile)

    def winner(self):
        return self.board.find_row_full_with_same_player()


class Tile:
    def __init__(self, x: Row, y: Column, player: Player):
        self.x: Row = x
        self.y: Column = y
        self.player: Player = player

    @property
    def is_not_empty(self):
        return self.player != NO_PLAYER

    def has_same_player_as(self, other: "Tile"):
        return self.player == other.player

    def has_same_coordinates_as(self, other: "Tile"):
        return self.x == other.x and self.y == other.y

    def update_player(self, new_player: Player):
        self.player = new_player


class Board:
    def __init__(self):
        self.plays: list[Tile] = []
        for x in range(FIRST_ROW, THIRD_ROW + 1):
            for y in range(FIRST_COLUMN, THIRD_COLUMN + 1):
                self.plays.append(Tile(cast("Row", x), cast("Column", y), NO_PLAYER))

    def is_tile_played_at(self, x: Row, y: Column):
        return self._find_tile_at(Tile(x, y, NO_PLAYER)).is_not_empty

    def add_tile_at(self, tile: Tile):
        self._find_tile_at(tile).update_player(tile.player)

    def find_row_full_with_same_player(self):
        if self._is_row_full(FIRST_ROW) and self._is_row_full_with_same_player(FIRST_ROW):
            return self._player_at(FIRST_ROW, FIRST_COLUMN)

        if self._is_row_full(SECOND_ROW) and self._is_row_full_with_same_player(SECOND_ROW):
            return self._player_at(SECOND_ROW, FIRST_COLUMN)

        if self._is_row_full(THIRD_ROW) and self._is_row_full_with_same_player(THIRD_ROW):
            return self._player_at(THIRD_ROW, FIRST_COLUMN)

        return NO_PLAYER

    def _find_tile_at(self, tile: Tile):
        return next(t for t in self.plays if t.has_same_coordinates_as(tile))

    def _has_same_player(self, x: Row, y: Column, other_x: Row, other_y: Column):
        return self._tile_at(x, y).has_same_player_as(self._tile_at(other_x, other_y))

    def _player_at(self, x: Row, y: Column):
        return self._tile_at(x, y).player

    def _tile_at(self, x: Row, y: Column):
        return next(t for t in self.plays if t.has_same_coordinates_as(Tile(x, y, NO_PLAYER)))

    def _is_row_full(self, row: Row):
        return (
            self.is_tile_played_at(row, FIRST_COLUMN)
            and self.is_tile_played_at(row, SECOND_COLUMN)
            and self.is_tile_played_at(row, THIRD_COLUMN)
        )

    def _is_row_full_with_same_player(self, row: Row):
        return self._has_same_player(row, FIRST_COLUMN, row, SECOND_COLUMN) and self._has_same_player(
            row, SECOND_COLUMN, row, THIRD_COLUMN
        )
