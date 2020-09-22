from mazeGenerator.maze.cell import Cell


# The Grid class
class Grid:
    def __init__(self):
        self.elements = []  # 2D-Array.

    def populateGrid(self, mSettings):
        nth_row = []  # Creation of the nth-array to-be-appended to 'the_grid'.

        # For row in number of rows:
        for row in range(mSettings.rows):
            for col in range(mSettings.cols):  # For col in number of cols:
                # Create Cell object with coordinates (col, row) and pass in settings.
                new_cell = Cell(col, row, mSettings)

                # Append new cell to current row.
                nth_row.append(new_cell)

            # Append current row to grid.
            self.elements.append(nth_row)

            # Clear row for next colums iteration.
            nth_row = []

    # Get width of grid.
    @property
    def width(self):
        return len(self.elements[0])

    # Get height of grid.
    @property
    def height(self):
        return len(self.elements)

    # Add lists of cells to grid.
    def append(self):
        self.elements.append

    # Define square brackets operator for Grid object.
    def __getitem__(self, key):
        return self.elements[key]


if __name__ == "__main__":
    grid = Grid()
    grid.elements = [[1, 2, 3], [5, 7, 11], [2, 4, 6], [16, 32, 64], [17, 18, 19]]

    print([1, 2, 3] in grid)
