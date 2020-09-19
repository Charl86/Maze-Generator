import pygame
from mazeGenerator.maze import mazeSettings


# Border class
class Border:
    # Takes as arguments an x and y coordinate, that represent the coordinates of the
    # top-left corner of the cell.
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Dimensions of border
        self.horizon_length = mazeSettings.cols * mazeSettings.size
        self.vertical_length = mazeSettings.rows * mazeSettings.size

        self.color = mazeSettings.Colors.RED  # The color of the border.
        self.thickness = 2  # The thickness of the border.

    # Method to draw border on canvas
    def draw(self):
        if self.x or self.y:  # If border coordinates aren't (0, 0)
            pygame.draw.rect(
                mazeSettings.PyGv.SCREEN, self.color, pygame.Rect(
                    (self.x, self.y), (self.horizon_length, self.vertical_length)),
                self.thickness)
