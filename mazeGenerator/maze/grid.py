from mazeGenerator.maze.cell import Cell


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

    @property
    def width(self):
        return len(self.elements[0])

    @property
    def height(self):
        return len(self.elements)

    def append(self):
        self.elements.append

    def __getitem__(self, key):
        return self.elements[key]

    def __contains__(self, item):
        return item in self.elements
