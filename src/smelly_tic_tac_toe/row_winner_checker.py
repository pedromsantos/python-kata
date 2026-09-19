# pylint: skip-file
# ruff: noqa: SIM102
class RowWinnerChecker:
    def check(self, board):
        # if the positions in first row are taken
        if (
            board.tile_at(0, 0).symbol != " "
            and board.tile_at(0, 1).symbol != " "
            and board.tile_at(0, 2).symbol != " "
        ):
            # if first row is full with same symbol
            if (
                board.tile_at(0, 0).symbol == board.tile_at(0, 1).symbol
                and board.tile_at(0, 2).symbol == board.tile_at(0, 1).symbol
            ):
                return board.tile_at(0, 0).symbol

        # if the positions in middle row are taken
        if (
            board.tile_at(1, 0).symbol != " "
            and board.tile_at(1, 1).symbol != " "
            and board.tile_at(1, 2).symbol != " "
        ):
            # if middle row is full with same symbol
            if (
                board.tile_at(1, 0).symbol == board.tile_at(1, 1).symbol
                and board.tile_at(1, 2).symbol == board.tile_at(1, 1).symbol
            ):
                return board.tile_at(1, 0).symbol

        # if the positions in last row are taken
        if (
            board.tile_at(2, 0).symbol != " "
            and board.tile_at(2, 1).symbol != " "
            and board.tile_at(2, 2).symbol != " "
        ):
            # if last row is full with same symbol
            if (
                board.tile_at(2, 0).symbol == board.tile_at(2, 1).symbol
                and board.tile_at(2, 2).symbol == board.tile_at(2, 1).symbol
            ):
                return board.tile_at(2, 0).symbol

        return " "
