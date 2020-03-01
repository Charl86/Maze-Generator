import pygame
import pygame.gfxdraw
from config import Vars, Colors, PygameVars as Pyv


class Border:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.color = Colors.RED
        self.thickness = 2

    def draw(self):
        if self.x or self.y:
            pygame.draw.rect(Pyv.SCREEN, self.color, pygame.Rect(
                (self.x, self.y), (Pyv.WIDTH - 2 * self.x, Pyv.HEIGHT - 2 * self.y)),
                             self.thickness)
