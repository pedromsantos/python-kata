# pylint: skip-file
# ruff: noqa: TRY002
from smelly_tic_tac_toe.board import Board
from smelly_tic_tac_toe.column_winner_checker import ColumnWinnerChecker
from smelly_tic_tac_toe.diagonal_winner_checker import DiagonalWinnerChecker
from smelly_tic_tac_toe.row_winner_checker import RowWinnerChecker


class Game:
    def __init__(self) -> None:
        self.last_symbol = " "
        self.board = Board()
        self.winner = " "
        self.row_winner_checker = RowWinnerChecker()
        self.column_winner_checker = ColumnWinnerChecker()
        self.diagonal_winner_checker = DiagonalWinnerChecker()

    def play(self, symbol, x, y):
        # if first move
        if self.last_symbol == " ":
            # if player is O
            if symbol == "O":
                msg = "Invalid first player"
                raise Exception(msg)
        # if not first move but player repeated
        elif symbol == self.last_symbol:
            msg = "Invalid next player"
            raise Exception(msg)
        # if not first move but play on an already played tile
        elif self.board.tile_at(x, y).symbol != " ":
            msg = "Invalid position"
            raise Exception(msg)

        # update game state
        self.last_symbol = symbol
        self.board.add_tile_at(symbol, x, y)

    def determine_winner(self):
        row_winner = self.row_winner_checker.check(self.board)
        if row_winner != " ":
            return row_winner

        column_winner = self.column_winner_checker.check(self.board)
        if column_winner != " ":
            return column_winner

        return self.diagonal_winner_checker.check(self.board)
