from random import random, choice
from typing import Tuple


class TileSet:
    def __init__(self, grid_size: Tuple[int, int], tile_size: int = 1, _empty: bool = True) -> None:
        self.size, self.grid = tile_size, grid_size
        self.items = {(x, y): Tile(x, y) for x in range(grid_size[0]) for y in range(grid_size[1])}
        self.walls = set()
        self.start, self.end = None, None
        if not _empty:
            self.generate_walls(.3)
            self.random_start()
            self.random_end()

    def set_tile_size(self, tile_size: int = 1) -> None:
        self.size = tile_size

    def generate_walls(self, density: float):
        dict_ = dict(self.items)
        for key, elt in dict_.items():
            if random() < density:
                self.items.pop(key)
                self.walls.add(elt)

    def random_start(self):
        elt = choice(tuple(self.items.values()))
        self.start = elt

    def random_end(self):
        elt = choice(tuple(self.items.values()))
        self.end = elt


class Tile:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    def __repr__(self):
        return f"{type(self).__name__}(x: {self.x}, y: {self.y})"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))
