import pygame
import pygame.gfxdraw
from config import Vars, Colors, PygameVars as Pyv


class Border:
    # Takes as arguments an x and y coordinate, that represent the coordinates of the
    # top-left corner of the cell.
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.color = Colors.RED  # The color of the border.
        self.thickness = 2  # The thickness of the border.

        # TODO: Apply this to the drawing of the border
        self.horizontal = Pyv.WIDTH - 2 * self.x
        self.vertical = Pyv.HEIGHT - 2 * self.y

    def draw(self):
        if self.x or self.y:
            # pygame.draw.rect(Pyv.SCREEN, self.color, pygame.Rect(
            #     (self.x, self.y), (Pyv.WIDTH - 2 * self.x, Pyv.HEIGHT - 2 * self.y)),
            #                  self.thickness)
            # There's a constant '6'
            # TODO: Generalize the constant
            pygame.draw.rect(Pyv.SCREEN, self.color, pygame.Rect(
                (self.x, self.y), (Pyv.WIDTH - 2 * self.x - 6, Pyv.HEIGHT - 2 * self.y - 6)),
                             self.thickness)
