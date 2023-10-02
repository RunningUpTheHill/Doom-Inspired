import pygame as pg

f = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, f, f, f, f, f, f, f, f, f, f, f, f, 1],
    [1, f, f, 1, 1, 1, 1, f, 1, 1, 1, f, f, 1],
    [1, f, f, f, f, f, 1, f, f, f, 1, f, f, 1],
    [1, f, f, f, f, f, 1, f, f, f, 1, f, f, 1],
    [1, f, f, 1, 1, 1, 1, f, f, f, f, f, f, 1],
    [1, f, f, f, f, f, f, f, f, f, 1, f, f, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for i, row in enumerate(self.mini_map):
            for j, val in enumerate(row):
                if val:
                    self.world_map[(j, i)] = val

    def draw(self):
        [pg.draw.rect(self.game.screen, "darkgray", (pos[0]*100, pos[1]*100, 100, 100), 2) for pos in self.world_map]

