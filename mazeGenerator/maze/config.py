import pygame
import math
import logging
import random
from maze.DoublyLinkedList import Node, DoublyLinkedList


log_file = f"maze_3 - Logging.log"

with open(log_file, "w"):
    pass


class Vars(object):
    starting_cell = None
    current_cell = None
    maze = []
    grid = []
    border = None
    doublyLL = DoublyLinkedList()
    COLS = None
    ROWS = None
    SIZE = None
    # Border = 0
    BORDER = 20

    @staticmethod
    def padding_func(cols_or_rows):
        return int(round(161.89079 * 0.9006 ** cols_or_rows + 18.69355, 0))


class PygameVars(object):
    WIDTH, HEIGHT = 400, 400
    SPEED = 15

    SCREEN = None
    FPS = None


class Colors(object):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    ASPHALT = (49, 49, 49)
    RED = (255, 0, 0)
    RAND_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 200)


class Debugger(object):
    formatter = logging.Formatter("%(message)s")

    LOGGER = logging.getLogger(__name__)
    LOGGER.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    STREAMER = logging.getLogger(__name__)
    STREAMER.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.DEBUG)

    LOGGER.addHandler(file_handler)
    STREAMER.addHandler(stream_handler)


if __name__ == "__main__":
    for i in range(101):
        print(f"{i, Vars.padding_func(i)}")
