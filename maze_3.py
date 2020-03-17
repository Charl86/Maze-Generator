import pygame
import pygame.gfxdraw
import math
import random
from config import Vars, Colors, PygameVars as Pyv
from DoublyLinkedList import Node
from cell import Cell
from border import Border
from maze_tkinter import Tkinter_Setup as Ts


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
# 2)
def draw():

    Pyv.SCREEN.fill(Colors.WHITE)
    Pyv.FPS.tick(Pyv.SPEED)

    Vars.border.draw()

    # The Algorithm Loop:
    if len(Vars.maze) == 0:
        Vars.maze.append(random.choice([cell for row in Vars.grid for cell in row]))

    if len(Vars.maze) != 0 or Vars.current_cell is None:
        cells_not_in_maze = [cell for row in Vars.grid for cell in row if cell not in Vars.maze]
        if cells_not_in_maze != [] and Vars.current_cell is None:
            Vars.current_cell = random.choice(cells_not_in_maze)

        for row in Vars.grid:
            for cell in row:
                cell.highlight()
                cell.show()

        if len(Vars.maze) != 0 and cells_not_in_maze != []:
            Vars.doublyLL.add(Node(Vars.current_cell))

            next_cell = Vars.current_cell.get_a_neighbor()

            Vars.current_cell = next_cell

            if next_cell in Vars.doublyLL.traverse(values=True):
                popped_cell = Vars.doublyLL.pop().val
                while popped_cell != next_cell:
                    popped_cell = Vars.doublyLL.pop().val
            elif next_cell in Vars.maze:
                Vars.doublyLL.add(Node(next_cell))
                while Vars.doublyLL.peek().prev_nod is not None:
                    Vars.doublyLL.peek().prev_nod.val.remove_walls_with(Vars.doublyLL.peek().val)
                    Vars.maze.append(Vars.doublyLL.pop().val)
                else:
                    Vars.maze.append(Vars.doublyLL.pop().val)

                Vars.current_cell = None

    pygame.display.update()


def main_loop():
    Ts.start_loop()

    pygame.init()

    Vars.AREA = math.floor((Pyv.WIDTH - 2 * Vars.BORDER) / Vars.COLS)
    Pyv.SCREEN = pygame.display.set_mode((Pyv.WIDTH, Pyv.HEIGHT))
    Pyv.FPS = pygame.time.Clock()

    Vars.grid = create_cells()
    Vars.border = Border(Vars.BORDER, Vars.BORDER)

    Vars.grid[0][0].walls["left"].on = False
    Vars.grid[-1][-1].walls["right"].on = False

    # Some logging:
    print(f"Square 'AREA': {Vars.AREA}.")
    print(f"Hori COLS Length: {Vars.AREA * Vars.COLS}.")
    print(f"SCREEN size: {Pyv.WIDTH, Pyv.HEIGHT}.")
    print(f"BORDER: {Vars.border.x, Vars.border.y}.")
    print(f"BORDER Dimensions: {Vars.border.horizontal, Vars.border.vertical}.")
    print(f"Start Cell: {Vars.grid[0][0].spaced_out_x, Vars.grid[0][0].spaced_out_y}.")
    print(f"End Cell: {Vars.grid[-1][-1].spaced_out_x, Vars.grid[-1][-1].spaced_out_y}.")
    # print(f"Star Cell: {Vars.grid[0][0].x + Vars.border.x, Vars.grid[0][0].y + Vars.border.y}.")
    # print(f"End Cell: {Vars.grid[-1][-1].x + Vars.border.x, Vars.grid[-1][-1].y + Vars.border.y}.")

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
        draw()


main_loop()
