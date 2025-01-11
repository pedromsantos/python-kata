from enum import Enum


class Player(Enum):
    X = 1
    O = 2


class Row(Enum):
    TOP = 1
    MIDDLE = 2
    BOTTOM = 3


class Column(Enum):
    LEFT = 1
    CENTER = 2
    RIGHT = 3


class Cell:
    def __init__(self, row: Row, column: Column):
        self.row = row
        self.column = column

    def equals(self, other: 'Cell') -> bool:
        return self.row == other.row and self.column == other.column


class Turn:
    def __init__(self, cell: Cell, player: Player):
        self.cell = cell
        self.player = player

    def equals(self, other: 'Turn') -> bool:
        return self.player == other.player and self.cell.equals(other.cell)


class TicTacToe:
    def play(self, turn: Turn) -> None:
        pass


class Output:
    def print_play(self, x: int, y: int, player: str) -> None:
        pass

    def print_winner(self, player: str) -> None:
        pass

    def print_error(self, error_message: str) -> None:
        pass
