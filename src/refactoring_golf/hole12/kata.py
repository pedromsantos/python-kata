# ruff: noqa: ANN202, ANN204, EM101, TRY002, TRY003
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
        coordinate = Coordinate(x, y)
        self._validate_position_is_empty(coordinate)

        self._update_last_player(player)
        self._update_board(Tile(player, coordinate))

    def _validate_first_move(self, player: Player):
        if self.last_player == NO_PLAYER and player == PLAYER_O:
            raise Exception("Invalid first player")

    def _validate_player(self, player: Player):
        if player == self.last_player:
            raise Exception("Invalid next player")

    def _validate_position_is_empty(self, coordinate: "Coordinate"):
        if self.board.is_tile_played_at(coordinate):
            raise Exception("Invalid position")

    def _update_last_player(self, player: Player):
        self.last_player = player

    def _update_board(self, tile: "Tile"):
        self.board.add_tile_at(tile)

    def winner(self):
        return self.board.find_full_row_with_same_player_or_no_player()


class Coordinate:
    def __init__(self, x: Row, y: Column):
        self.x = x
        self.y = y

    def equal(self, other: "Coordinate"):
        return self.x == other.x and self.y == other.y


class Tile:
    def __init__(self, player: Player, coordinate: Coordinate):
        self.coordinate = coordinate
        self.player: Player = player

    @property
    def is_not_empty(self):
        return self.player != NO_PLAYER

    def has_same_player_as(self, other: "Tile"):
        return self.player == other.player

    def has_same_coordinates_as(self, other: "Tile"):
        return self.coordinate.equal(other.coordinate)

    def update_player(self, new_player: Player):
        self.player = new_player


class Board:
    def __init__(self):
        self.plays: list[Tile] = []
        for x in range(FIRST_ROW, THIRD_ROW + 1):
            for y in range(FIRST_COLUMN, THIRD_COLUMN + 1):
                self.plays.append(Tile(NO_PLAYER, Coordinate(cast("Row", x), cast("Column", y))))

    def is_tile_played_at(self, coordinate: Coordinate):
        return self._find_tile(Tile(NO_PLAYER, coordinate)).is_not_empty

    def add_tile_at(self, tile: Tile):
        self._find_tile(tile).update_player(tile.player)

    def find_full_row_with_same_player_or_no_player(self):
        if self._is_row_full(FIRST_ROW) and self._is_row_full_with_same_player(FIRST_ROW):
            return self._player_at(Coordinate(FIRST_ROW, FIRST_COLUMN))

        if self._is_row_full(SECOND_ROW) and self._is_row_full_with_same_player(SECOND_ROW):
            return self._player_at(Coordinate(SECOND_ROW, FIRST_COLUMN))

        if self._is_row_full(THIRD_ROW) and self._is_row_full_with_same_player(THIRD_ROW):
            return self._player_at(Coordinate(THIRD_ROW, FIRST_COLUMN))

        return NO_PLAYER

    def _find_tile(self, tile: Tile):
        return next(t for t in self.plays if t.has_same_coordinates_as(tile))

    def _player_at(self, coordinate: Coordinate):
        return self._find_tile(Tile(NO_PLAYER, coordinate)).player

    def _is_row_full(self, row: Row):
        return (
            self.is_tile_played_at(Coordinate(row, FIRST_COLUMN))
            and self.is_tile_played_at(Coordinate(row, SECOND_COLUMN))
            and self.is_tile_played_at(Coordinate(row, THIRD_COLUMN))
        )

    def _is_row_full_with_same_player(self, row: Row):
        return self._has_same_player(
            Coordinate(row, FIRST_COLUMN), Coordinate(row, SECOND_COLUMN)
        ) and self._has_same_player(Coordinate(row, SECOND_COLUMN), Coordinate(row, THIRD_COLUMN))

    def _has_same_player(self, coordinate: Coordinate, other_coordinate: Coordinate):
        return self._find_tile(Tile(NO_PLAYER, coordinate)).has_same_player_as(
            self._find_tile(Tile(NO_PLAYER, other_coordinate))
        )
