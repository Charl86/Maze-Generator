import random
import pygame
from mazeGenerator import mazeInstance
from mazeGenerator.parts.wall import Wall
from mazeGenerator.config import PygameVars as Pyv


# The Cell class.
class Cell:
    # Takes as arguments an x and y coordinate, that represent the coordinates of the
    # top-left corner of the cell.
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        # Definition of some attributes:
        self.thickness = 5  # set the thickness of the walls.

        # Colors:
        # self.maze_cell_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 200)
        self.maze_cell_color = (0, 175, 255, 255)  # color for cells that are part of the maze
        # self.maze_cell_color = (255, 255, 255, 255)
        self.current_cell_color = (100, 0, 255, 125)  # color for current cell
        self.trail_cells_color = (255, 0, 255, 100)  # color for cells in the doubly-linked list.

        self.visited = False  # If a cell has been picked.

        # The actual coordinates with the "area" applied of a cell.
        self.spaced_out_x = self.x * self.size + mazeInstance.borderCoords
        self.spaced_out_y = self.y * self.size + mazeInstance.borderCoords

        # The walls of a cell:
        self.walls = {
            "top": Wall(
                (self.spaced_out_x, self.spaced_out_y),
                (self.spaced_out_x + self.size, self.spaced_out_y)
                    ),
            "right": Wall(
                (self.spaced_out_x + self.size, self.spaced_out_y),
                (self.spaced_out_x + self.size, self.spaced_out_y + self.size)
                    ),
            "bot": Wall(
                (self.spaced_out_x + self.size, self.spaced_out_y + self.size),
                (self.spaced_out_x, self.spaced_out_y + self.size)
                    ),
            "left": Wall(
                (self.spaced_out_x, self.spaced_out_y + self.size),
                (self.spaced_out_x, self.spaced_out_y)
                    )
                }

    # The method that shows the walls of a cell, if they are turned on.
    def show(self):
        # self.highlight()
        self.walls["top"].show(self.thickness)
        self.walls["right"].show(self.thickness)
        self.walls["bot"].show(self.thickness)
        self.walls["left"].show(self.thickness)

    # Method turns off the walls between two cells
    def remove_walls_with(self, other):
        # the difference between the coordinates of the two walls
        x_difference, y_difference = self.x - other.x, self.y - other.y

        # The coordinate of the cells are stored before applying their "area".
        # This means that the left-top corners of the cells (the coordinates) are one unit
        # beside each other, e.g. Cell_1: (0, 0), Cell_2: (1, 0), Cell_3: (2, 0), etc.

        # If the difference in x, defined as self.x - other.x, is 1, then that means
        # that self.x is greater than other.x by 1, meaning that self.x is to the right of other.x
        if x_difference == 1:
            # therefore, we turn off the left wall of self and the right wall of other
            self.walls["left"].on = False
            other.walls["right"].on = False
        # If the x_difference is -1, then self.x is lesser than other.x by 1,
        # meaning that self is to the left of other
        elif x_difference == -1:
            # we then turn off the walls between them.
            self.walls["right"].on = False
            other.walls["left"].on = False

        # Likewise, if the y_difference between self.y and other.y is 1, that means
        # that self.y is greater than other.y by 1, meaning that self is below
        # other (by the way coordinates work on pygame. It would be equivalent to using the
        # fourth quadrant in a cartesian plane with the y-axis turned positive).
        if y_difference == 1:
            # we turn off the walls between them.
            self.walls["top"].on = False
            other.walls["bot"].on = False
        # If the y_difference is -1, then self is above other
        elif y_difference == -1:
            # and we turn off the respective walls between them.
            self.walls["bot"].on = False
            other.walls["top"].on = False

    # Method for choosing a random adjacent neighbor.
    def getUnvNeigh(self, neighborhood):
        return random.choice([uv for uv in self.neighbors(neighborhood) if not uv.visited])

    def unvisitedNeigh(self, neighborhood):
        if any([not neighbor.visited for neighbor in self.neighbors(neighborhood)]):
            return True
        else:
            return False

    # A getter that returns a list of the adjacent cells of self.
    def neighbors(self, neighborhood):
        # In order to get the adjacent cells, in theory we'd have 4 cases in which we add 1 to each coordinate
        # of the cell e.g. in order to get the top neighboring cell, you add -1 to the y-coordinate of the current cell;
        # in order to get the right neighboring cell, you only add 1 to the x-coordinate, and so on so forth.

        # But what happens when you have to get the neighboring cells of a cell on the edge of the maze. A cell on
        # the edge of the maze would only have 3 adjacent cells (2 if the cell is in one of the corners). Therefore, in
        # this list comprehension, we set a limit: if the coordinates of a new possible neighboring cell are outside of
        # the maze, then we intuitively discard it as a possible neighboring cell.
        neighborCoords = [
            (self.y - 1, self.x), (self.y, self.x + 1),
            (self.y + 1, self.x), (self.y, self.x - 1)
        ]
        possibleNeighbors = []
        for row, col in neighborCoords:
            if 0 <= row <= (len(neighborhood) - 1) and\
                    0 <= col <= (len(neighborhood[row]) - 1):
                possibleNeighbors.append(neighborhood[row][col])
        return possibleNeighbors

    # Method that takes charge of dyeing the cells depending on which of the data structures
    # they belong to.
    def highlight(self, currentCell=False, backtracking=False):
        if self.visited and self != currentCell:
            pygame.gfxdraw.box(
                Pyv.SCREEN, pygame.Rect(
                    self.spaced_out_x, self.spaced_out_y,
                    self.size, self.size
                ), self.trail_cells_color
            )
        elif self == currentCell:
            pygame.gfxdraw.box(
                Pyv.SCREEN, pygame.Rect(
                    self.spaced_out_x, self.spaced_out_y,
                    self.size, self.size
                ), self.current_cell_color
            )
            if backtracking:
                pygame.gfxdraw.box(
                        Pyv.SCREEN, pygame.Rect(
                            self.spaced_out_x, self.spaced_out_y,
                            self.size, self.size
                        ), (100, 255, 0)
                    )
