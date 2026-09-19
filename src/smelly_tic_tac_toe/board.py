# pylint: skip-file
class Tile:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.symbol = " "


class Board:
    def __init__(self) -> None:
        self.plays = []
        for i in range(3):
            for j in range(3):
                self.plays.append(Tile(i, j))

    def tile_at(self, x, y):
        return next(tile for tile in self.plays if tile.x == x and tile.y == y)

    def add_tile_at(self, symbol, x, y):
        tile = self.tile_at(x, y)
        tile.symbol = symbol
