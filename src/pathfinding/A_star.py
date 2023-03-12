from math import sqrt

from src.tiles import Tile, TileSet


class Node(Tile):
    def __init__(self, x, y, tile_set: TileSet, parent=None, is_start=False):
        self.tile_set = tile_set
        self.parent = parent
        super().__init__(x, y)
        self.distance_from_start, self.distance_from_end, self.cost, self.neighbours = None, None, None, None
        if not is_start:
            self.calculate_costs()
        else:
            end = tile_set.end
            self.distance_from_start = 0
            self.distance_from_end = sqrt((self.x - end.x) ** 2 + (self.y - end.y) ** 2)
            self.cost = float(self.distance_from_end)
        self.get_neighbours()

    def calculate_costs(self):
        start, end = self.tile_set.start, self.tile_set.end
        self.distance_from_start = 0 if self == start else (self.parent.distance_from_start +
                                                            (1 if self.x == self.parent.x ^ self.y == self.parent.y
                                                             else sqrt(2)))
        self.distance_from_end = sqrt((self.x - end.x) ** 2 + (self.y - end.y) ** 2)
        self.cost = self.distance_from_start + self.distance_from_end

    def get_neighbours(self):
        self.neighbours = set()
        for x in (self.x - 1, self.x, self.x + 1):
            for y in (self.y - 1, self.y, self.y + 1):
                if (x, y) != (0, 0):
                    self.neighbours.add(self.tile_set.items[(x, y)])


def run(tile_set):
    # TODO fix this func
    tiles_to_evaluate, evaluated_tiles = set(), set()
    tiles_to_evaluate.add(Node(tile_set.start.x, tile_set.start.y, tile_set))
    while tiles_to_evaluate:
        current_node = tiles_to_evaluate.pop()
        tiles_to_evaluate.add(current_node)
        for elt in tiles_to_evaluate:
            if elt.cost < current_node.cost or \
                    (elt.cost == current_node.cost and elt.distance_from_end < current_node.distance_from_end):
                current_node = elt
        tiles_to_evaluate.remove(current_node)
        evaluated_tiles.add(current_node)

        if current_node == tile_set.end:
            return

        for node in current_node.neighbours:
            print(node)

        return
