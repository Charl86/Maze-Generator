import random


class PygameVars(object):
    WIDTH, HEIGHT = 400, 400
    SPEED = 2

    SCREEN = None
    FPS = None


class Colors(object):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    ASPHALT = (49, 49, 49)
    RED = (255, 0, 0)
    RAND_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 200)

    currCellC = (100, 0, 255, 125)
    trailCellC = (255, 0, 255, 100)
    backtracking = (150, 255, 0, 255)
