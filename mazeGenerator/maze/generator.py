import random
import pygame
import pygame.gfxdraw
from mazeGenerator.datast.stack import Stack
from mazeGenerator.maze.border import Border
from mazeGenerator.maze.grid import Grid


class Generator:
    def __init__(self, mSettings, canvasC=(0, 0, 0)):
        self.mSettings = mSettings  # Maze configurations.
        self.stack = Stack()  # An instance of MyStack class.

        self.grid = Grid()  # The grid that contains all cells.

        self.current_cell = None  # Current cell.
        self.backtracking = False  # If generator is backtracking.
        self.border = None  # Border object.

        self.canvasC = canvasC  # Color of canvas.

    def run(self):
        # Create a border with top-left coordinates (self.borderCoords, self.borderCoords).
        # Pass in settings.
        self.border = Border(
            self.mSettings.borderCoords, self.mSettings.borderCoords, self.mSettings,
        )

        # Calculate size of the screen based on the size of the border and its coordinates.
        self.mSettings.PyGv.WIDTH = \
            self.border.horizon_length + 2 * self.mSettings.borderCoords
        self.mSettings.PyGv.HEIGHT = \
            self.border.vertical_length + 2 * self.mSettings.borderCoords

        # Initiate pygame module.
        pygame.init()

        # Create a Screen() object with width and height stored in mSettings.
        self.mSettings.PyGv.SCREEN = pygame.display.set_mode(
            (self.mSettings.PyGv.WIDTH, self.mSettings.PyGv.HEIGHT)
        )

        # Create a Clock() object; basically the frames per second.
        self.mSettings.PyGv.FPS = pygame.time.Clock()

        # Create all the cells with their respective rows and store them in self.grid.
        self.grid.populateGrid(self.mSettings)

        # Disable the left wall of the first cell.
        self.grid[0][0].walls["left"].on = False
        # Disable the right wall of the last cell.
        self.grid[-1][-1].walls["right"].on = False

        # Start window loop:
        while 1:
            # For each event in pygame.event.get(), check if the exit button has been clicked.
            for event in pygame.event.get():
                # If it has, exit the program.
                if event.type == pygame.QUIT:
                    raise SystemExit
            # Else call draw the maze and its parts.
            self.draw()

    def draw(self):
        # Fill the screen with desired color and set the FPS to the desired speed.
        self.mSettings.PyGv.SCREEN.fill(self.canvasC)
        self.mSettings.PyGv.FPS.tick(self.mSettings.PyGv.SPEED)

        # Draw border, if there is any.
        self.border.draw()

        # If no cell has been visited out of all cells
        if all([not cell.visited for cell in self.allCells]):
            # Pick one at random and mark it as visited, starting the algorithm with that one.
            self.current_cell = random.choice(self.allCells)
            self.current_cell.visited = True
            self.stack.push(self.current_cell)  # Push current cell to stack.

        # For each row containing cells in the grid
        for row in self.grid:
            # for each cell per row
            for cell in row:
                # Highlight cells depending on their attributes and whether or not
                # generator is backtracking.
                cell.highlight(currentCell=self.current_cell, backtracking=self.backtracking)
                cell.show()  # Draw cells.

        # Set backtracking to false each loop.
        self.backtracking = False
        # If there is at least one cell that hasn't been visited
        if any([not cell.visited for cell in self.allCells]):
            # If current cell has unvisited neighbor cells
            if self.current_cell.unvisitedNeigh(self.grid):
                # Choose random unvisited neighbor.
                nextCell = self.current_cell.getUnvNeigh(self.grid)
                # Remove walls between current cell and chosen neighbor cell.
                self.current_cell.remove_walls_with(nextCell)
                # Push chosen neighbor cell to stack.
                self.stack.push(nextCell)
                nextCell.visited = True
                self.current_cell = nextCell  # Make neighbor cell the current cell.
            elif self.stack.peek() is not None:  # If there is at least one cell before current in stack
                self.stack.pop()  # Pop last cell (which is current cell).
                self.current_cell = self.stack.peek()  # Make current cell the new last cell.
                self.backtracking = True
        else:  # If all cells have been visited
            self.current_cell = None  # Set current cell to None.

        # Display everything that has been drawn on canvas.
        pygame.display.update()

    @property
    def allCells(self):  # Return list of all cells in grid.
        return [cell for row in self.grid for cell in row]


# Unit Test:
if __name__ == "__main__":
    from mazeGenerator.maze.settings import Settings

    Generator(Settings(cols=10, rows=10, size=76, borderCoords=20, width=780, height=780, speed=12)).run()
