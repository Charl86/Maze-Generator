import random
import pygame
import pygame.gfxdraw
from mazeGenerator import mazeInstance
from mazeGenerator.config import Colors, PygameVars as Pyv
from mazeGenerator.datast.mystack import MyStack
from mazeGenerator.interface import Tkinter_Setup as Ts
from mazeGenerator.parts.border import Border
from mazeGenerator.parts.cell import Cell


class Generator:
    def __init__(self):
        self.maze = mazeInstance
        self.stack = MyStack()

        self.grid = []
        self.current_cell = None
        self.backtracking = False

    def start(self, test=False):
        # Open Tkinter interface.
        Ts.start_loop()

        if test is True:
            raise SystemExit

        # Create a border with coordinates self.BORDER.
        self.maze.border = Border(self.maze.borderCoords, self.maze.borderCoords)

        # Calculate size of the screen based on the size of the border.
        Pyv.WIDTH = self.maze.border.horizon_length + 2 * self.maze.borderCoords
        Pyv.HEIGHT = self.maze.border.vertical_length + 2 * self.maze.borderCoords

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

    def draw(self):
        # 1rst Part: Repainting the screen, setting the frames per second
        Pyv.SCREEN.fill(Colors.BLACK)
        Pyv.FPS.tick(Pyv.SPEED)

        # and drawing the border.
        self.maze.border.draw()

        if all([not cell.visited for cell in self.allCells]):
            self.current_cell = random.choice(self.allCells)
            self.current_cell.visited = True
            self.stack.push(self.current_cell)

        # For each row containing cells in the grid
        for row in self.grid:
            # for each cell per row
            for cell in row:
                # Draw them on the screen (this will not display them though).
                cell.highlight(currentCell=self.current_cell, backtracking=self.backtracking)
                cell.show()

        self.backtracking = False
        if any([not cell.visited for cell in self.allCells]):
            # choose a random cell neighboring the current cell, as the future current cell
            if self.current_cell.unvisitedNeigh(self.grid):
                nextCell = self.current_cell.getUnvNeigh(self.grid)
                self.current_cell.remove_walls_with(nextCell)
                self.stack.push(nextCell)
                nextCell.visited = True
                self.current_cell = nextCell
            elif self.stack.peek() is not None:
                self.stack.pop()
                self.current_cell = self.stack.peek()
                self.backtracking = True
        else:
            self.current_cell = None

        # 3rd Part: display everything that has been drawn.
        pygame.display.update()

    def create_cells(self):
        the_grid = []  # Creation of the 2D-array.
        nth_row = []  # Creation of the nth-array to-be-appended to 'the_grid'.

        # For each array in 'self.ROWS' amount:
        for row in range(self.maze.rows):
            for col in range(self.maze.cols):  # For each 'Cell' object per array:
                # We create a new 'Cell' object, whose coordinates are its
                # index position within the 'the_grid' 2D-array:
                new_cell = Cell(col, row, self.maze.size)

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
