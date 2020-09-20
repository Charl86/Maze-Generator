import random
import math
import pygame
from mazeGenerator.maze.wall import Wall


# Cell class
class Cell:
    # Takes 3 arguments: x and y coordinates in 2D-grid and size (width and height).
    def __init__(self, x, y, size, mazeSettings):
        self.x = x
        self.y = y
        self.size = size
        self.mazeSettings = mazeSettings

        self.thickness = 5  # Wall thickness.
        self.visited = False  # If a cell has been visited.

        # The coordinates on the display window, not the 2D-grid.
        self.spaced_out_x = self.size * self.x + self.mazeSettings.borderCoords
        self.spaced_out_y = self.size * self.y + self.mazeSettings.borderCoords

        # Walls initialization:
        self.walls = {
            "top": Wall(
                (self.spaced_out_x, self.spaced_out_y),
                (self.spaced_out_x + self.size, self.spaced_out_y),
                self.mazeSettings),
            "right": Wall(
                (self.spaced_out_x + self.size, self.spaced_out_y),
                (self.spaced_out_x + self.size, self.spaced_out_y + self.size),
                self.mazeSettings),
            "bot": Wall(
                (self.spaced_out_x + self.size, self.spaced_out_y + self.size),
                (self.spaced_out_x, self.spaced_out_y + self.size),
                self.mazeSettings),
            "left": Wall(
                (self.spaced_out_x, self.spaced_out_y + self.size),
                (self.spaced_out_x, self.spaced_out_y),
                self.mazeSettings)
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
        neighborCoords = [
            (self.y - 1, self.x), (self.y, self.x + 1),
            (self.y + 1, self.x), (self.y, self.x - 1)
        ]

        possibleNeighbors = []
        for row, col in neighborCoords:
            if 0 <= row <= neighborhood.height - 1 and 0 <= col <= neighborhood.width - 1:
                possibleNeighbors.append(neighborhood[row][col])
        return possibleNeighbors

    # Highlight self based on parameters
    def highlight(self, currentCell=False, backtracking=False):
        if self != currentCell and self.visited:  # If self is not current cell and was visited
            pygame.gfxdraw.box(
                self.mazeSettings.PyGv.SCREEN, self.rectanColor, self.mazeSettings.Colors.trailCellC
            )
        elif self == currentCell:  # If cell is current cell
            if not backtracking:  # If generator is not bactracking
                pygame.gfxdraw.box(
                    self.mazeSettings.PyGv.SCREEN, self.rectanColor, self.mazeSettings.Colors.currCellC
                )
            else:
                pygame.gfxdraw.box(
                    self.mazeSettings.PyGv.SCREEN, self.rectanColor, self.mazeSettings.Colors.backtracking
                )

    @property  # Highlight size.
    def rectanColor(self):
        return pygame.Rect(self.spaced_out_x, self.spaced_out_y, self.size, self.size)
