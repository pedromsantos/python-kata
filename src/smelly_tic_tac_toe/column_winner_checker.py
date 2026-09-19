# pylint: skip-file
# ruff: noqa: SIM102
# Cross-file Duplicated Code / Shotgun Surgery kata fixture: this checker
# re-implements the exact same "are these three tiles taken and equal"
# pattern as RowWinnerChecker, independently, instead of sharing one
# extracted line-checking algorithm.
class ColumnWinnerChecker:
    def check(self, board):
        # if the positions in first column are taken
        if (
            board.tile_at(0, 0).symbol != " "
            and board.tile_at(1, 0).symbol != " "
            and board.tile_at(2, 0).symbol != " "
        ):
            # if first column is full with same symbol
            if (
                board.tile_at(0, 0).symbol == board.tile_at(1, 0).symbol
                and board.tile_at(2, 0).symbol == board.tile_at(1, 0).symbol
            ):
                return board.tile_at(0, 0).symbol

        # if the positions in middle column are taken
        if (
            board.tile_at(0, 1).symbol != " "
            and board.tile_at(1, 1).symbol != " "
            and board.tile_at(2, 1).symbol != " "
        ):
            # if middle column is full with same symbol
            if (
                board.tile_at(0, 1).symbol == board.tile_at(1, 1).symbol
                and board.tile_at(2, 1).symbol == board.tile_at(1, 1).symbol
            ):
                return board.tile_at(0, 1).symbol

        # if the positions in last column are taken
        if (
            board.tile_at(0, 2).symbol != " "
            and board.tile_at(1, 2).symbol != " "
            and board.tile_at(2, 2).symbol != " "
        ):
            # if last column is full with same symbol
            if (
                board.tile_at(0, 2).symbol == board.tile_at(1, 2).symbol
                and board.tile_at(2, 2).symbol == board.tile_at(1, 2).symbol
            ):
                return board.tile_at(0, 2).symbol

        return " "
