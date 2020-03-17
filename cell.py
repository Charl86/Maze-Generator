import pygame
import pygame.gfxdraw
import random
import logging
from wall import Wall
from config import Vars, Colors, PygameVars as Pyv


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.thickness = 3
        self.rect_thick = 2
        # self.fill_c = RAND_COLOR
        self.fill_c = (0, 175, 255, 255)
        # self.fill_c = (255, 255, 255, 255)
        self.fill_cur = (100, 0, 255, 125)
        self.fill_st = (255, 0, 255, 100)

        self.visited = False
        self.spaced_out_x, self.spaced_out_y = self.x * Vars.AREA + Vars.BORDER, self.y * Vars.AREA + Vars.BORDER
        self.walls = {
            "top": Wall(
                self.spaced_out_x, self.spaced_out_y, self.spaced_out_x + Vars.AREA, self.spaced_out_y),
            "right": Wall(
                self.spaced_out_x + Vars.AREA, self.spaced_out_y, self.spaced_out_x + Vars.AREA, self.spaced_out_y + Vars.AREA),
            "bot": Wall(
                self.spaced_out_x + Vars.AREA, self.spaced_out_y + Vars.AREA, self.spaced_out_x, self.spaced_out_y + Vars.AREA),
            "left": Wall(
                self.spaced_out_x, self.spaced_out_y + Vars.AREA, self.spaced_out_x, self.spaced_out_y)}

    def show(self):
        self.walls["top"].show(self.thickness)
        self.walls["right"].show(self.thickness)
        self.walls["bot"].show(self.thickness)
        self.walls["left"].show(self.thickness)

    def remove_walls_with(self, other):
        x_difference, y_difference = self.x - other.x, self.y - other.y

        if x_difference == 1:
            self.walls["left"].on = False
            other.walls["right"].on = False
        elif x_difference == -1:
            self.walls["right"].on = False
            other.walls["left"].on = False

        if y_difference == 1:
            self.walls["top"].on = False
            other.walls["bot"].on = False
        elif y_difference == -1:
            self.walls["bot"].on = False
            other.walls["top"].on = False

    def get_a_neighbor(self):
        if len(Vars.doublyLL.traverse()) >= 2:
            return random.choice([neighbor for neighbor in self.neighbors
                                  if neighbor != Vars.doublyLL.peek().prev_nod.val])
        else:
            return random.choice([neighbor for neighbor in self.neighbors])

        # if len(self.neighbors):
        #     if len(Vars.stack) > 1:
        #         # return random.choice([neighbor for neighbor in self.neighbors if neighbor != Vars.stack[-1]])
        #         # n = []
        #         # for neighbor in self.neighbors:
        #         #     if neighbor != Vars.stack[-2]:
        #         #         n.append(neighbor)
        #         # return random.choice(n)
        #         # return random.choice([neighbor for neighbor in self.neighbors if neighbor != Vars.stack[-2]])
        #     else:
        #         return random.choice([neighbor for neighbor in self.neighbors])

    @property
    def neighbors(self):
        # possible_neighbors = []
        # for row, col in [(self.y - 1, self.x), (self.y, self.x + 1), (self.y + 1, self.x), (self.y, self.x - 1)]:
        #     if 0 <= row <= (ROWS - 1) and 0 <= col <= (COLS - 1):
        #         possible_neighbors.append(Vars.grid[row][col])
        # return possible_neighbors
        return [Vars.grid[row][col] for row, col in
                [(self.y - 1, self.x), (self.y, self.x + 1), (self.y + 1, self.x), (self.y, self.x - 1)]
                if 0 <= row <= (Vars.ROWS - 1) and 0 <= col <= (Vars.COLS - 1)]

    def highlight(self):
        if self in Vars.doublyLL.traverse(values=True) and self != Vars.current_cell:
            pygame.gfxdraw.box(Pyv.SCREEN, pygame.Rect(
                self.spaced_out_x, self.spaced_out_y, Vars.AREA, Vars.AREA), self.fill_st)
        elif self in Vars.maze:
            pygame.gfxdraw.box(Pyv.SCREEN, pygame.Rect(
                self.spaced_out_x, self.spaced_out_y, Vars.AREA, Vars.AREA), self.fill_c)
        if self == Vars.current_cell:
            pygame.gfxdraw.box(Pyv.SCREEN, pygame.Rect(self.spaced_out_x, self.spaced_out_y, Vars.AREA, Vars.AREA),
                               self.fill_cur)
