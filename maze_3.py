import pygame
import pygame.gfxdraw
import math
import random
from config import Vars, Colors, Debugger, PygameVars as Pyv
from DoublyLinkedList import Node
from cell import Cell
from border import Border
from maze_tkinter import Tkinter_Setup as Ts


# Function that sets up one-time events and variables and then starts the loop that will
# keep the pygame window open.
def main_loop():
    # Open Tkinter interface.
    Ts.start_loop()

    # Initiate pygame module.
    pygame.init()

    # The « SIZE » of the cells is equal to the floor of the width of the window,
    # minus the ratio of twice the coordinates of the border and the number of columns.

    # TODO : the size of a cell shouldn't be too small.
    # This block of code:
    # iteration = 1
    # Vars.SIZE = int((Pyv.WIDTH - 2 * Vars.BORDER) / Vars.COLS)
    # while ((Pyv.WIDTH - 2 * Vars.BORDER) % Vars.COLS) != 0:
    #     Pyv.WIDTH += Vars.padding_func(iteration)
    #     Pyv.HEIGHT += Vars.padding_func(iteration)
    #     Vars.SIZE = int((Pyv.WIDTH - 2 * Vars.BORDER) / Vars.COLS)
    #     iteration += 1
    # Or this one:
    iteration = 1
    Vars.SIZE = int((Pyv.WIDTH - 2 * Vars.BORDER) / Vars.COLS)
    while ((Pyv.WIDTH - 2 * Vars.BORDER) % Vars.COLS) != 0:
        Pyv.WIDTH += 1
        Pyv.HEIGHT += 1
        Vars.SIZE = int((Pyv.WIDTH - 2 * Vars.BORDER) / Vars.COLS)
        iteration += 1

    # Create a Screen() object with width Pyv.WIDTH and height Pyv.HEIGHT.
    Pyv.SCREEN = pygame.display.set_mode((Pyv.WIDTH, Pyv.HEIGHT))
    # Create a Clock() object; basically the frames per second.
    Pyv.FPS = pygame.time.Clock()

    # Create all the cells with their respective rows and store them in Vars.grid.
    Vars.grid = create_cells()
    # Create a border with coordinates Vars.BORDER.
    Vars.border = Border(Vars.BORDER, Vars.BORDER)

    # Disable the left wall of the first cell.
    Vars.grid[0][0].walls["left"].on = False
    # Disable the right wall of the last cell.
    Vars.grid[-1][-1].walls["right"].on = False

    # Some logging:
    Debugger.STREAMER.debug(f"Cell SIZE: {Vars.SIZE}.")
    Debugger.STREAMER.debug(f"Hori COLS Length: {Vars.SIZE * Vars.COLS}.")
    Debugger.STREAMER.debug(f"SCREEN size: {Pyv.WIDTH, Pyv.HEIGHT}.")
    Debugger.STREAMER.debug(f"BORDER coords: {Vars.border.top_left_corn}, {Vars.border.bot_left_corn},"
                            f"{Vars.border.top_right_corn}, {Vars.border.bot_right_corn}.")
    Debugger.STREAMER.debug(f"Start Cell: {Vars.grid[0][0].spaced_out_x, Vars.grid[0][0].spaced_out_y}.")
    Debugger.STREAMER.debug(f"End Cell: {Vars.grid[-1][-1].spaced_out_x, Vars.grid[-1][-1].spaced_out_y}.")
    # print(f"Square 'SIZE': {Vars.SIZE}.")
    # print(f"Hori COLS Length: {Vars.SIZE * Vars.COLS}.")
    # print(f"SCREEN size: {Pyv.WIDTH, Pyv.HEIGHT}.")
    # print(f"BORDER: {Vars.border.x, Vars.border.y}.")
    # print(f"BORDER Dimensions: {Vars.border.horizontal, Vars.border.vertical}.")
    # print(f"Start Cell: {Vars.grid[0][0].spaced_out_x, Vars.grid[0][0].spaced_out_y}.")
    # print(f"End Cell: {Vars.grid[-1][-1].spaced_out_x, Vars.grid[-1][-1].spaced_out_y}.")
    # print(f"Star Cell: {Vars.grid[0][0].x + Vars.border.x, Vars.grid[0][0].y + Vars.border.y}.")
    # print(f"End Cell: {Vars.grid[-1][-1].x + Vars.border.x, Vars.grid[-1][-1].y + Vars.border.y}.")

    # While true
    while 1:
        # For each event in pygame.event.get(), check if the exit button
        # has been pressed.
        for event in pygame.event.get():
            # If it has, exit the program.
            if event.type == pygame.QUIT:
                raise SystemExit
        # Call the draw() function.
        draw()


# This function will create 'the_grid' variable, which will be a 2D-array
# The amount of sub-arrays inside the 'the_grid' variable will be 'Vars.ROWS',
# and each sub-array will have 'Vars.COLS' amount of 'Cell' objects.
# In the end, this function will return the 'the_grid' 2D-Array, containing
# arrays, the latter which contain 'Cell' objects.
def create_cells():
    the_grid = []  # Creation of the 2D-array.
    nth_row = []  # Creation of the nth-array to-be-appended to 'the_grid'.

    # For each array in 'Vars.ROWS' amount:
    for row in range(Vars.ROWS):
        for col in range(Vars.COLS):  # For each 'Cell' object per array:
            # We create a new 'Cell' object, whose coordinates are its
            # index position within the 'the_grid' 2D-array:
            new_cell = Cell(col, row)

            # Then we append it to the nth-array within the 'the_grid' 2D-array:
            nth_row.append(new_cell)

        # Once there is a 'Vars.COLS' amount of 'Cell' object in a given
        # nth-array, we append this array to the 'the_grid' 2D-array:
        the_grid.append(nth_row)

        # Then we clear this array, in order to add new 'Cell' objects:
        nth_row = []

    # Once there is a 'Vars.ROWS' amount of arrays in 'the_grid', we return
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
def draw():
    # 1rst Part: Repainting the screen, setting the frames per second
    Pyv.SCREEN.fill(Colors.WHITE)
    Pyv.FPS.tick(Pyv.SPEED)

    # and drawing the border.
    Vars.border.draw()

    # 2nd Part: The Algorithm Loop:
    if len(Vars.maze) == 0:  # If there aren't any cells that are part of the maze
        # choose one random cell, from the a random column in Vars.grid, and make it
        # part of the maze.
        Vars.maze.append(random.choice([cell for row in Vars.grid for cell in row]))

    # If there is a cell that is part of the maze or there is no current cell
    if len(Vars.maze) != 0 or Vars.current_cell is None:
        # create an array that contains all the cells that aren't part of the maze
        cells_not_in_maze = [cell for row in Vars.grid for cell in row if cell not in Vars.maze]
        # if there are cells that aren't in the maze or if there is no current cell
        if cells_not_in_maze != [] and Vars.current_cell is None:
            # choose a a cell from the cells that aren't in the maze and make it
            # the current cell.
            Vars.current_cell = random.choice(cells_not_in_maze)

        # For each row containing cells in the grid
        for row in Vars.grid:
            # for each cell per row
            for cell in row:
                # color the cells depending on their individual information
                cell.highlight()
                # and draw them on the screen (this will not display them though).
                cell.show()

        # If  there are no cells that are part of the maze and there are cells that are
        # not part of the maze
        if len(Vars.maze) != 0 and cells_not_in_maze != []:
            # add to a doubly-linked list, a node with the current cell as its value
            Vars.doublyLL.add(Node(Vars.current_cell))

            # choose a random cell neighboring the current cell, as the future current cell
            next_cell = Vars.current_cell.get_a_neighbor()

            # assign the next cell as the current cell.
            Vars.current_cell = next_cell

            # If the next cell (or now current cell) is in the doubly-linked list
            if next_cell in Vars.doublyLL.traverse(values=True):
                # Pop the last node of the doubly-linked list and return its value,
                # and then assign it to the popped_cell variable.
                popped_cell = Vars.doublyLL.pop().val
                # While the popped_cell isn't the next_cell (or current_cell)
                while popped_cell != next_cell:
                    # Keep popping nodes with cell as values from the doubly-linked list.
                    popped_cell = Vars.doublyLL.pop().val
            # Else if the next cell (or now current_cell) is part of the maze
            elif next_cell in Vars.maze:
                # create a node that has as value this next cell, and append this node
                # to the doubly-linked list.
                Vars.doublyLL.add(Node(next_cell))
                # While there is a node (with a cell) before the last node (with a cell)
                # in the doubly-linked list
                while Vars.doublyLL.peek().prev_nod is not None:
                    # turn off walls between the cell of the second-to-last node and the cell
                    # of the last node
                    Vars.doublyLL.peek().prev_nod.val.remove_walls_with(Vars.doublyLL.peek().val)
                    # Delete the last node containing the last cell of the doubly-linked list,
                    # and make it at the same time part of the maze.
                    Vars.maze.append(Vars.doublyLL.pop().val)
                # While there is no node before the last node of the doubly-linked list
                else:
                    # Delete the last node containing the last cell of the doubly-linked list,
                    # and make it at the same time part of the maze.
                    Vars.maze.append(Vars.doublyLL.pop().val)

                # make the current cell equal to None.
                Vars.current_cell = None

    # 3rd Part: display everything that has been drawn.
    pygame.display.update()


# Start the program.
main_loop()
