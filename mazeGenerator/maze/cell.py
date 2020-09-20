import random
import math
import pygame
from mazeGenerator.maze.wall import Wall


# Cell class
class Cell:
    # Takes 3 arguments: x and y coordinates in 2D-grid and size (width and height).
    def __init__(self, x, y, mSettings, **kwargs):
        self.x = x
        self.y = y
        self.size = mSettings.size
        self.mSettings = mSettings

        self.thickness = 5  # Wall thickness.
        self.visited = False  # If a cell has been visited.

        # The coordinates on the display window, not the 2D-grid.
        self.spaced_out_x = self.size * self.x + self.mSettings.borderCoords
        self.spaced_out_y = self.size * self.y + self.mSettings.borderCoords

        self.trailCellC = (0, 150, 255)  # Trail color.
        self.currCellC = (255, 0, 255)  # Current cell color.
        self.backtC = (255, 255, 0)  # Backtracking color.

        for key in kwargs:
            if key in self.__dict__:
                self.__dict__[key] = kwargs[key]

        # Walls initialization:
        self.walls = {
            "top": Wall(
                (self.spaced_out_x, self.spaced_out_y),
                (self.spaced_out_x + self.size, self.spaced_out_y),
                self.mSettings),
            "right": Wall(
                (self.spaced_out_x + self.size, self.spaced_out_y),
                (self.spaced_out_x + self.size, self.spaced_out_y + self.size),
                self.mSettings),
            "bot": Wall(
                (self.spaced_out_x + self.size, self.spaced_out_y + self.size),
                (self.spaced_out_x, self.spaced_out_y + self.size),
                self.mSettings),
            "left": Wall(
                (self.spaced_out_x, self.spaced_out_y + self.size),
                (self.spaced_out_x, self.spaced_out_y),
                self.mSettings)
                }

    # Draw cell walls
    def show(self):
        self.walls["top"].show(self.thickness)
        self.walls["right"].show(self.thickness)
        self.walls["bot"].show(self.thickness)
        self.walls["left"].show(self.thickness)

    # Remove walls between self and other
    def remove_walls_with(self, other):
        # Take the difference between self.x, other.x and self.y, other.y.
        x_difference, y_difference = self.x - other.x, self.y - other.y

        if x_difference == 1:  # If other is to the right of self, remove corresponding walls.
            self.walls["left"].on = False
            other.walls["right"].on = False
        elif x_difference == -1:  # If other is to the left of self, remove walls.
            self.walls["right"].on = False
            other.walls["left"].on = False

        if y_difference == 1:  # If other is above self, remove corresponding walls.
            self.walls["top"].on = False
            other.walls["bot"].on = False
        elif y_difference == -1:  # If other is bellow self, remove walls.
            self.walls["bot"].on = False
            other.walls["top"].on = False

    # Determine if self has unvisited neighbors
    def unvisitedNeigh(self, neighborhood):
        if any([not neighbor.visited for neighbor in self.neighbors(neighborhood)]):
            return True
        else:
            return False

    # Choose a random unvisited neighbor of self from the neighborhood (the 2D-grid)
    def getUnvNeigh(self, neighborhood):
        return random.choice([uv for uv in self.neighbors(neighborhood) if not uv.visited])

    # Get all neighbors
    def neighbors(self, neighborhood):
        possibleNeighbors = []
        for i in range(4):
            # Get cardinal points centered at (self.x, self.y), in order to get
            # neighbors' coordinates.
            newX = round(math.cos(math.radians(90) * i) + self.x)
            newY = round(-math.sin(math.radians(90) * i) + self.y)

            if 0 <= newX < neighborhood.width and 0 <= newY < neighborhood.height:
                possibleNeighbors.append(neighborhood[newY][newX])

        return possibleNeighbors

    # Highlight self based on parameters
    def highlight(self, currentCell=False, backtracking=False):
        if self != currentCell and self.visited:  # If self is not current cell and was visited
            pygame.gfxdraw.box(
                self.mSettings.PyGv.SCREEN, self.rectangle, self.trailCellC
            )
        elif self == currentCell:  # If cell is current cell
            if not backtracking:  # If generator is not bactracking
                pygame.gfxdraw.box(
                    self.mSettings.PyGv.SCREEN, self.rectangle, self.currCellC
                )
            else:
                pygame.gfxdraw.box(
                    self.mSettings.PyGv.SCREEN, self.rectangle, self.backtC
                )

    @property  # Highlight area.
    def rectangle(self):
        return pygame.Rect(self.spaced_out_x, self.spaced_out_y, self.size, self.size)
