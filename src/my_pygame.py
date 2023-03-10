import pygame as pyg

from src.tiles import TileSet
from typing import Tuple

WINDOW = pyg.display.set_mode((800, 800))
GAP = 1
COLORS = {
    'background': (50, 50, 50),
    'empty_tile': (200, 200, 200),
    'start': (50, 255, 50),
    'end': (255, 50, 50)
}


def init(tile_size: int, grid_size: Tuple[int, int]):
    global WINDOW, GAP
    GAP = (tile_size // 10) if tile_size > 10 else 1
    window_size = (grid_size[0] * (tile_size + GAP) + GAP,
                   grid_size[1] * (tile_size + GAP) + GAP)
    WINDOW = pyg.display.set_mode(window_size)


def display(tile_set: TileSet):
    WINDOW.fill(COLORS['background'])
    for elt in tile_set.items:
        pyg.draw.rect(WINDOW, COLORS['empty_tile'],
                      pyg.Rect((tile_set.size + GAP) * elt.x + GAP,
                               (tile_set.size + GAP) * elt.y + GAP,
                               tile_set.size, tile_set.size))
    start, end = tile_set.start, tile_set.end
    if start:
        pyg.draw.rect(WINDOW, COLORS['start'],
                      pyg.Rect((tile_set.size + GAP) * start.x + GAP,
                               (tile_set.size + GAP) * start.y + GAP,
                               tile_set.size, tile_set.size))
    if end:
        pyg.draw.rect(WINDOW, COLORS['end'],
                      pyg.Rect((tile_set.size + GAP) * end.x + GAP,
                               (tile_set.size + GAP) * end.y + GAP,
                               tile_set.size, tile_set.size))
    pyg.display.flip()


def run(tile_set):
    is_running = True
    while is_running:
        display(tile_set)
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                is_running = False
    pyg.quit()
