import pygame
import pygame.gfxdraw
import random
import logging
from wall import Wall
from config import Vars, Colors, Debugger, PygameVars as Pyv


# The Cell class.
class Cell:
    # Takes as arguments an x and y coordinate, that represent the coordinates of the
    # top-left corner of the cell.
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Definition of some attributes:
        self.thickness = 3  # set the thickness of the walls.
        # self.rect_thick = 2

        # Colors:
        # self.fill_c = RAND_COLOR
        self.fill_c = (0, 175, 255, 255)  # color for cells that are part of the maze
        # self.fill_c = (255, 255, 255, 255)
        self.fill_cur = (100, 0, 255, 125)  # color for current cell
        self.fill_st = (255, 0, 255, 100)  # color for cells in the doubly-linked list.

        self.visited = False  # If a cell has been chosen as the current cell.
        # The actual coordinates with the "area" applied of a cell.
        self.spaced_out_x, self.spaced_out_y = self.x * Vars.SIZE + Vars.BORDER, self.y * Vars.SIZE + Vars.BORDER

        # The walls of a cell:
        self.walls = {
            "top": Wall(
                (self.spaced_out_x, self.spaced_out_y),
                (self.spaced_out_x + Vars.SIZE, self.spaced_out_y)),
            "right": Wall(
                (self.spaced_out_x + Vars.SIZE, self.spaced_out_y),
                (self.spaced_out_x + Vars.SIZE, self.spaced_out_y + Vars.SIZE)),
            "bot": Wall(
                (self.spaced_out_x + Vars.SIZE, self.spaced_out_y + Vars.SIZE),
                (self.spaced_out_x, self.spaced_out_y + Vars.SIZE)),
            "left": Wall(
                (self.spaced_out_x, self.spaced_out_y + Vars.SIZE),
                (self.spaced_out_x, self.spaced_out_y))
        }

    # The method that shows the walls of a cell, if they are turned on.
    def show(self):
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
    def get_a_neighbor(self):
        # When there are two or more nodes containing a cell in the doubly-linked list
        if len(Vars.doublyLL.traverse()) >= 2:
            # choose a random neighbor from self.neighbors (which returns all the adjacent cells),
            # as long as it isn't the previous current_cell.
            return random.choice([neighbor for neighbor in self.neighbors
                                  if neighbor != Vars.doublyLL.peek().prev_nod.val])
        # If there is only one node with one cell in the doubly-linked list
        else:
            # choose any neighboring cell because there's only one cell in the doubly-linked list
            # and thus there is no fear of walking backwards.
            return random.choice([neighbor for neighbor in self.neighbors])

        # if len(self.neighbors):
        #     if len(Vars.stack) > 1:
        #         # return random.choice([neighbor for neighbor in self.neighbors if neighbor != Vars.stack[-1]])
        #         # n = []
        #         # for neighbor in self.neighbors:
        #         #     if neighbor != Vars.stack[-2]:
        #         #         n.append(neighbor)
        #         # return random.choice(n)
        #         # return random.choice([neighbor for neighbor in self.neighbors if neighbor != Vars.stack[-2]])
        #     else:
        #         return random.choice([neighbor for neighbor in self.neighbors])

    # A getter that returns a list of the adjacent cells of self.
    @property
    def neighbors(self):
        # possible_neighbors = []
        # for row, col in [(self.y - 1, self.x), (self.y, self.x + 1), (self.y + 1, self.x), (self.y, self.x - 1)]:
        #     if 0 <= row <= (ROWS - 1) and 0 <= col <= (COLS - 1):
        #         possible_neighbors.append(Vars.grid[row][col])
        # return possible_neighbors

        # In order to get the adjacent cells, in theory we'd have 4 cases in which we add 1 to each coordinate
        # of the cell e.g. in order to get the top neighboring cell, you add -1 to the y-coordinate of the current cell;
        # in order to get the right neighboring cell, you only add 1 to the x-coordinate, and so on so forth.

        # But what happens when you have to get the neighboring cells of a cell on the edge of the maze. A cell on
        # the edge of the maze would only have 3 adjacent cells (2 if the cell is in one of the corners). Therefore, in
        # this list comprehension, we set a limit: if the coordinates of a new possible neighboring cell are outside of
        # the maze, then we intuitively discard it as a possible neighboring cell.
        return [Vars.grid[row][col] for row, col in
                [(self.y - 1, self.x), (self.y, self.x + 1), (self.y + 1, self.x), (self.y, self.x - 1)]
                if 0 <= row <= (Vars.ROWS - 1) and 0 <= col <= (Vars.COLS - 1)]

    # Method that takes charge of dyeing the cells depending on which of the data structures
    # they belong to.
    def highlight(self):
        # If the cell is in the doubly-linked list (and thus not part of the maze yet) and the cell isn't the
        # current cell
        if self in Vars.doublyLL.traverse(values=True) and self != Vars.current_cell:
            # "Paint" it with self.fill_st (basically draws a rectangle with the given color over the cell).
            pygame.gfxdraw.box(Pyv.SCREEN, pygame.Rect(
                self.spaced_out_x, self.spaced_out_y, Vars.SIZE, Vars.SIZE), self.fill_st)
        # Else if the cell is part of the maze
        elif self in Vars.maze:
            # "Paint" it with the self.fill_c color.
            pygame.gfxdraw.box(Pyv.SCREEN, pygame.Rect(
                self.spaced_out_x, self.spaced_out_y, Vars.SIZE, Vars.SIZE), self.fill_c)
        # But if the cell is the current cell
        if self == Vars.current_cell:
            # "Paint" it with the self.fill_cur color.
            pygame.gfxdraw.box(Pyv.SCREEN, pygame.Rect(self.spaced_out_x, self.spaced_out_y, Vars.SIZE, Vars.SIZE),
                               self.fill_cur)
