import random
import pygame
import pygame.gfxdraw
from mazeGenerator.datast.mystack import MyStack
from mazeGenerator.maze.border import Border
from mazeGenerator.maze.cell import Cell


class Generator:
    def __init__(self, mSettings):
        self.mSettings = mSettings
        self.stack = MyStack()

        self.grid = []
        self.current_cell = None
        self.backtracking = False

    def run(self):
        # Create a border with coordinates self.BORDER.
        self.mSettings.border = Border(self.mSettings.borderCoords, self.mSettings.borderCoords)

        # Calculate size of the screen based on the size of the border.
        self.mSettings.PyGv.WIDTH = \
            self.mSettings.border.horizon_length + 2 * self.mSettings.borderCoords
        self.mSettings.PyGv.HEIGHT = \
            self.mSettings.border.vertical_length + 2 * self.mSettings.borderCoords

        # Initiate pygame module.
        pygame.init()

        # Create a Screen() object with width self.mSettings.WIDTH and height self.mSettings.HEIGHT.
        self.mSettings.PyGv.SCREEN = pygame.display.set_mode(
            (self.mSettings.PyGv.WIDTH, self.mSettings.PyGv.HEIGHT)
        )

        # Create a Clock() object; basically the frames per second.
        self.mSettings.PyGv.FPS = pygame.time.Clock()

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
        self.mSettings.PyGv.SCREEN.fill(self.mSettings.Colors.BLACK)
        self.mSettings.PyGv.FPS.tick(self.mSettings.PyGv.SPEED)

        # and drawing the border.
        self.mSettings.border.draw()

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
        for row in range(self.mSettings.rows):
            for col in range(self.mSettings.cols):  # For each 'Cell' object per array:
                # We create a new 'Cell' object, whose coordinates are its
                # index position within the 'the_grid' 2D-array:
                new_cell = Cell(col, row, self.mSettings.size)

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


if __name__ == "__main__":
    pass
