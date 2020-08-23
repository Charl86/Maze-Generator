from mazeGenerator.maze.maze import pygame
from mazeGenerator.maze.config import Colors, PygameVars as Pyv


# The Wall class
class Wall:
    # takes as arguments two points: A and B which are tuples. A will be the starting point
    # of the line and B will be its ending point.
    # It also takes as argument the "on" status, which defaults to True if no argument is given
    # this means that the wall starts as turned on, and get turned off when the remove_walls_with() method is called
    def __init__(self, A, B, on=True):
        self.A, self.B = A, B
        # Validating that tuples are actually given as A and B.
        if not isinstance(self.A, tuple) or not isinstance(self.B, tuple):
            raise TypeError("Tuple objects were expected for A and B but instead at least"
                            "one of them is not.")

        self.on = on

        # The color of the walls.
        self.color = Colors.WHITE

    # The show method that takes as argument the thickness of a wall.
    def show(self, thickness):
        if self.on:
            # Drawing of the wall.
            pygame.draw.line(Pyv.SCREEN, self.color, self.A, self.B, thickness)
