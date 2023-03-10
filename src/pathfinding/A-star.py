from math import sqrt

from src.tiles import Tile


class Node(Tile):
    def __init__(self, x, y, tile_set, parent=None):
        self.tile_set = tile_set
        self.parent = parent
        super().__init__(x, y)
        self.distance_from_start, self.distance_from_end, self.cost = None, None, None
        self.calculate_costs()

    def calculate_costs(self):
        start, end = self.tile_set.start, self.tile_set.end
        self.distance_from_start = 0 if self == start else self.parent.distance_from_start + 1
        self.distance_from_end = sqrt((self.x - end.x) ** 2 + (self.y - end.y) ** 2)
        self.cost = self.distance_from_start + self.distance_from_end


def run(tile_set):
    tiles_to_evaluate, evaluated_tiles = set(), set()
    tiles_to_evaluate.add(Node(tile_set.start.x, tile_set.start.y, tile_set))
    while tiles_to_evaluate:
        current_node = tiles_to_evaluate.pop()
        tiles_to_evaluate.add(current_node)
        for elt in tiles_to_evaluate:
            if elt.cost < current_node.costor or\
                    (elt.cost == current_node.cost and elt.distance_from_end < current_node.distance_from_end):
                current_node = elt
        tiles_to_evaluate.remove(current_node)
        evaluated_tiles.add(current_node)

        if current_node == tile_set.end:
            return


