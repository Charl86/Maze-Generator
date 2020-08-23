from mazeGenerator import mazeInstance
from mazeGenerator.maze.maze import pygame
from mazeGenerator.maze.config import Colors, PygameVars as Pyv


class Border:
    # Takes as arguments an x and y coordinate, that represent the coordinates of the
    # top-left corner of the cell.
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Corners of the border.
        # self.top_left_corn = self.x, self.y
        # self.bot_left_corn = self.x, self.y + Pyv.HEIGHT - 2 * self.y
        # self.top_right_corn = self.x + Pyv.WIDTH - 2 * self.x, self.y
        # self.bot_right_corn = self.x + Pyv.WIDTH - 2 * self.x, self.y + Pyv.HEIGHT - 2 * self.y

        # Dimensions of border
        self.horizon_length = mazeInstance.COLS * mazeInstance.SIZE
        self.vertical_length = mazeInstance.ROWS * mazeInstance.SIZE
        # self.horizon_length = Pyv.WIDTH - 2 * self.x
        # self.vertical_length = Pyv.WIDTH - 2 * self.y

        self.color = Colors.RED  # The color of the border.
        self.thickness = 2  # The thickness of the border.

    def draw(self):
        # if self.x or self.y:
        #     pygame.draw.rect(Pyv.SCREEN, self.color, pygame.Rect(
        #         (self.x, self.y), (Pyv.WIDTH - 2 * self.x, Pyv.HEIGHT - 2 * self.y)),
        #                      self.thickness)
        if self.x or self.y:
            pygame.draw.rect(Pyv.SCREEN, self.color, pygame.Rect(
                (self.x, self.y), (self.horizon_length, self.vertical_length)),
                             self.thickness)