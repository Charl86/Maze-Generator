import pygame
import pygame.gfxdraw
import math
import random
from config import Vars, Colors, PygameVars as Pyv
from DoublyLinkedList import Node
from cell import Cell
from border import Border
from maze_tkinter import Tkinter_Setup as Ts


def create_cells():
    the_grid = []
    nth_row = []

    for row in range(Vars.ROWS):
        for col in range(Vars.COLS):
            new_cell = Cell(col, row)
            nth_row.append(new_cell)
        the_grid.append(nth_row)
        nth_row = []
    return the_grid


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

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
        draw()


main_loop()
