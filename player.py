from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = player_pos
        self.angle = player_angle

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = player_speed * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx -= speed_cos
            dy -= speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy -= speed_cos
        if keys[pg.K_d]:
            dx -= speed_sin
            dy += speed_cos

        self.check_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= player_rotation_speed * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += player_rotation_speed * self.game.delta_time
        self.angle %= math.tau

    def draw(self):
        # pg.draw.line(self.game.screen, "yellow", (self.x * 100, self.y * 100),
        #              (self.x * 100 + width * math.cos(self.angle), self.y * 100 + width * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, "green", (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_collision(self, dx, dy):
        if self.check_wall(int(self.x+dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y+dy)):
            self.y += dy

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)