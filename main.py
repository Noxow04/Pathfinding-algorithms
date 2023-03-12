# import src.my_pygame as my_pyg
from src.tiles import TileSet
from src.pathfinding.A_star import run

params = {
    'tile_size': 30,
    'grid_size': (30, 30)
}

tile_set = TileSet(**params, _empty=False)

run(tile_set)

# my_pyg.init(**params)
# my_pyg.run(tile_set)
