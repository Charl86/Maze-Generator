import pygame
from config import Vars, Colors, PygameVars as Pyv


class Wall:
    def __init__(self, a, b, c, d, on=True):
        self.a, self.b, self.c, self.d = a, b, c, d
        self.on = on

        self.color = Colors.BLACK

    def show(self, thickness):
        if self.on:
            pygame.draw.line(Pyv.SCREEN, self.color, (self.a, self.b), (self.c, self.d), thickness)
