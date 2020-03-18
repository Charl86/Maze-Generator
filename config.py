import pygame
import math
import logging
import random
from DoublyLinkedList import Node, DoublyLinkedList


log_file = f"maze_3 - Logging.log"

with open(log_file, "w"):
    pass


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
########################################################################################################################


class Vars(object):
    starting_cell = None
    current_cell = None
    maze = []
    grid = []
    border = None
    logger = LOGGER
    doublyLL = DoublyLinkedList()
    COLS = None
    ROWS = None
    AREA = None
    BORDER = 10
    # self.WIDTH, self.HEIGHT = 400, 400
    # self.SPEED = 3
    # self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    # self.FPS = pygame.time.Clock()
    # self.WHITE = (255, 255, 255)
    # self.BLACK = (0, 0, 0)
    # self.ASPHALT = (49, 49, 49)
    # self.RAND_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 200)


class PygameVars(object):
    WIDTH, HEIGHT = 400, 400
    SPEED = 5

    SCREEN = None
    FPS = None


class Colors(object):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    ASPHALT = (49, 49, 49)
    RED = (255, 0, 0)
    RAND_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 200)


# AREA = 40
# AREA = math.floor((WIDTH - 2 * BORDER) / Vars.COLS)
# while (WIDTH - 2 * BORDER) % AREA != 0:
#     AREA -= 1

# COLS, ROWS = math.floor((WIDTH - 2 * BORDER) / AREA), math.floor((HEIGHT - 2 * BORDER) / AREA)

