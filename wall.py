import pygame
from config import Vars, Colors, PygameVars as Pyv


# The Wall class
class Wall:
    # takes as arguments two points: (a, b) and (c, d). Think of a line in a cartesian
    # plane with points A = (a, b) and B = (c, d)
    # it also takes as argument the "on" status, which defaults to True if no argument is given
    # this means that the wall starts as turned on, and get turned off when the remove_walls_with() method is called
    def __init__(self, a, b, c, d, on=True):
        self.a, self.b, self.c, self.d = a, b, c, d
        self.on = on

        # The color of the walls
        self.color = Colors.BLACK

    # The show method that takes as argument the thickness of a wall
    def show(self, thickness):
        if self.on:
            # drawing of the wall.
            pygame.draw.line(Pyv.SCREEN, self.color, (self.a, self.b), (self.c, self.d), thickness)
