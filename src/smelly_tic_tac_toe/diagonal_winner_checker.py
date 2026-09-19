# pylint: skip-file
# ruff: noqa: SIM102
# Cross-file Duplicated Code / Shotgun Surgery kata fixture: this checker
# re-implements the exact same "are these three tiles taken and equal"
# pattern as RowWinnerChecker and ColumnWinnerChecker, independently.
class DiagonalWinnerChecker:
    def check(self, board):
        # if the positions in the main diagonal are taken
        if (
            board.tile_at(0, 0).symbol != " "
            and board.tile_at(1, 1).symbol != " "
            and board.tile_at(2, 2).symbol != " "
        ):
            # if main diagonal is full with same symbol
            if (
                board.tile_at(0, 0).symbol == board.tile_at(1, 1).symbol
                and board.tile_at(2, 2).symbol == board.tile_at(1, 1).symbol
            ):
                return board.tile_at(0, 0).symbol

        # if the positions in the anti-diagonal are taken
        if (
            board.tile_at(0, 2).symbol != " "
            and board.tile_at(1, 1).symbol != " "
            and board.tile_at(2, 0).symbol != " "
        ):
            # if anti-diagonal is full with same symbol
            if (
                board.tile_at(0, 2).symbol == board.tile_at(1, 1).symbol
                and board.tile_at(2, 0).symbol == board.tile_at(1, 1).symbol
            ):
                return board.tile_at(0, 2).symbol

        return " "
