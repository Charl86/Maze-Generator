import random
import pygame
import pygame.gfxdraw
from mazeGenerator.mazeParts.config import Colors, PygameVars as Pyv
from mazeGenerator.mazeParts.debugger import Debugger
from mazeGenerator.mazeParts.mystack import MyStack


class Maze:
    def __init__(self):
        self.BORDER = 20

        self.ROWS = False
        self.COLS = False
        self.SIZE = False

        self.current_cell = None
        self.backtracking = False

        self.visited = []
        self.stack = MyStack()
        self.goodStack = []

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
        Pyv.SCREEN.fill(Colors.BLACK)
        Pyv.FPS.tick(Pyv.SPEED)

        # and drawing the border.
        self.border.draw()

        if all([not cell.visited for cell in self.allCells]):
            self.current_cell = random.choice(self.allCells)
            self.current_cell.visited = True
            # self.stack.push(self.current_cell)
            self.goodStack.append(self.current_cell)

        # For each row containing cells in the grid
        for row in self.grid:
            # for each cell per row
            for cell in row:
                # Draw them on the screen (this will not display them though).
                if self.backtracking and cell == self.current_cell:
                    cell.highlight(backtracking=self.backtracking)
                else:
                    cell.highlight()
                cell.show()

        self.backtracking = False
        if any([not cell.visited for cell in self.allCells]):
            # choose a random cell neighboring the current cell, as the future current cell
            if self.current_cell.unvisitedNeigh():
                nextCell = self.current_cell.getUnvNeigh()
                # self.stack.push(nextCell)
                self.current_cell.remove_walls_with(nextCell)
                self.goodStack.append(nextCell)
                nextCell.visited = True
                self.current_cell = nextCell
                # self.current_cell.visited = True
            # elif self.stack.peek() is not None:
            elif len(self.goodStack) > 0:
                self.goodStack.pop()
                self.current_cell = self.goodStack[-1]
                self.backtracking = True
        else:
            self.current_cell = None

        # 3rd Part: display everything that has been drawn.
        pygame.display.update()

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

    @property
    def allCells(self):
        return [cell for row in self.grid for cell in row]
