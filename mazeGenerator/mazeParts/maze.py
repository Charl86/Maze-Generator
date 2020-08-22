# import pygame
# import pygame.gfxdraw
# import random
import pygame
import pygame.gfxdraw
import random
from mazeGenerator.mazeParts.config import Colors, PygameVars as Pyv
from mazeGenerator.mazeParts.DoublyLinkedList import Node, DoublyLinkedList


class Maze:
    def __init__(self):
        self.BORDER = 20

        self.ROWS = False
        self.COLS = False
        self.SIZE = False

        self.doublyLL = DoublyLinkedList()
        self.maze = []
        self.current_cell = None

    def start(self, test=False):
        from mazeGenerator.mazeParts.border import Border
        from mazeGenerator.interface import Tkinter_Setup as Ts

        # Open Tkinter interface.
        Ts.start_loop()

        if test is True:
            raise SystemExit

        # Create a border with coordinates self.BORDER.
        self.border = Border(self.BORDER, self.BORDER)

        # Calculate size of the screen based on the size of the border.
        Pyv.WIDTH = self.border.horizon_length + 2 * self.BORDER
        Pyv.HEIGHT = self.border.vertical_length + 2 * self.BORDER

        # Initiate pygame module.
        pygame.init()

        # Create a Screen() object with width Pyv.WIDTH and height Pyv.HEIGHT.
        Pyv.SCREEN = pygame.display.set_mode((Pyv.WIDTH, Pyv.HEIGHT))

        # Create a Clock() object; basically the frames per second.
        Pyv.FPS = pygame.time.Clock()

        # Create all the cells with their respective rows and store them in self.grid.
        self.grid = self.create_cells()

        # Disable the left wall of the first cell.
        self.grid[0][0].walls["left"].on = False
        # Disable the right wall of the last cell.
        self.grid[-1][-1].walls["right"].on = False

        # While true
        while 1:
            # For each event in pygame.event.get(), check if the exit button
            # has been pressed.
            for event in pygame.event.get():
                # If it has, exit the program.
                if event.type == pygame.QUIT:
                    raise SystemExit
            # Call the draw() function.
            self.draw()

    # This function will create 'the_grid' variable, which will be a 2D-array
    # The amount of sub-arrays inside the 'the_grid' variable will be 'self.ROWS',
    # and each sub-array will have 'self.COLS' amount of 'Cell' objects.
    # In the end, this function will return the 'the_grid' 2D-Array, containing
    # arrays, the latter which contain 'Cell' objects.
    def create_cells(self):
        from mazeGenerator.mazeParts.cell import Cell

        the_grid = []  # Creation of the 2D-array.
        nth_row = []  # Creation of the nth-array to-be-appended to 'the_grid'.

        # For each array in 'self.ROWS' amount:
        for row in range(self.ROWS):
            for col in range(self.COLS):  # For each 'Cell' object per array:
                # We create a new 'Cell' object, whose coordinates are its
                # index position within the 'the_grid' 2D-array:
                new_cell = Cell(col, row)

                # Then we append it to the nth-array within the 'the_grid' 2D-array:
                nth_row.append(new_cell)

            # Once there is a 'self.COLS' amount of 'Cell' object in a given
            # nth-array, we append this array to the 'the_grid' 2D-array:
            the_grid.append(nth_row)

            # Then we clear this array, in order to add new 'Cell' objects:
            nth_row = []

        # Once there is a 'self.ROWS' amount of arrays in 'the_grid', we return
        # this 2D-array:
        return the_grid

    # This function can be divided into 3 parts:
    # 1) The screen will be fully painted with the 'Colors.COLORS' variable,
    # covering anything that was painted before. The frames per second will
    # be set to the 'Pyv.SPEED' variable, and a border, coming from the 'Border'
    # object, will ultimately draw itself on the screen, given that the coordinates
    # of the top-left corner of the border object aren't (0, 0).
    #
    # 2) The actual maze-generation algorithm. You could swap this part with any other
    # maze generation algorithm and in theory the program would work just fine. The
    # algorithm used in this program is Wilson's, (...).
    # 3) Display all the objects on the screen that were drawn before or during the
    # procedure of the algorithm.
    def draw(self):
        # 1rst Part: Repainting the screen, setting the frames per second
        Pyv.SCREEN.fill(Colors.WHITE)
        Pyv.FPS.tick(Pyv.SPEED)

        # and drawing the border.
        self.border.draw()

        # 2nd Part: The Algorithm Loop:
        if len(self.maze) == 0:  # If there aren't any cells that are part of the maze
            # choose one random cell, from the a random column in self.grid, and make it
            # part of the maze.
            self.maze.append(random.choice([cell for row in self.grid for cell in row]))

        # If there is a cell that is part of the maze or there is no current cell
        if len(self.maze) != 0 or self.current_cell is None:
            # create an array that contains all the cells that aren't part of the maze
            cells_not_in_maze = [cell for row in self.grid for cell in row if cell not in self.maze]
            # if there are cells not in the maze and the current cell is None
            if cells_not_in_maze != [] and self.current_cell is None:
                # choose a a cell from the cells that aren't in the maze and make it
                # the current cell.
                self.current_cell = random.choice(cells_not_in_maze)

            # For each row containing cells in the grid
            for row in self.grid:
                # for each cell per row
                for cell in row:
                    # color the cells depending on their individual information
                    cell.highlight()
                    # and draw them on the screen (this will not display them though).
                    cell.show()

            # If there are cells in the maze and cells not in the maze
            if len(self.maze) != 0 and cells_not_in_maze != []:
                # add to a doubly-linked list, a node with the current cell as its value
                self.doublyLL.add(Node(self.current_cell))

                # choose a random cell neighboring the current cell, as the future current cell
                next_cell = self.current_cell.get_a_neighbor()

                # assign the next cell as the current cell.
                self.current_cell = next_cell

                # If the next cell (or now current cell) is in the doubly-linked list
                if next_cell in self.doublyLL.traverse(values=True):
                    # Pop the last node of the doubly-linked list and return its value,
                    # and then assign it to the popped_cell variable.
                    popped_cell = self.doublyLL.pop().val
                    # While the popped_cell isn't the next_cell (or current_cell)
                    while popped_cell != next_cell:
                        # Keep popping nodes with cell as values from the doubly-linked list.
                        popped_cell = self.doublyLL.pop().val
                # Else if the next cell (or now current_cell) is part of the maze
                elif next_cell in self.maze:
                    # create a node that has as value this next cell, and append this node
                    # to the doubly-linked list.
                    self.doublyLL.add(Node(next_cell))
                    # While there is a node (with a cell) before the last node (with a cell)
                    # in the doubly-linked list
                    while self.doublyLL.peek().prev_nod is not None:
                        # turn off walls between the cell of the second-to-last node and the cell
                        # of the last node
                        self.doublyLL.peek().prev_nod.val.remove_walls_with(self.doublyLL.peek().val)
                        # Delete the last node containing the last cell of the doubly-linked list,
                        # and make it at the same time part of the maze.
                        self.maze.append(self.doublyLL.pop().val)
                    # While there is no node before the last node of the doubly-linked list
                    else:
                        # Delete the last node containing the last cell of the doubly-linked list,
                        # and make it at the same time part of the maze.
                        self.maze.append(self.doublyLL.pop().val)

                    # make the current cell equal to None.
                    self.current_cell = None

        # 3rd Part: display everything that has been drawn.
        pygame.display.update()
