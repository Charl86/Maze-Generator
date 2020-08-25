import random


class Settings:
    class PygameVars:
        WIDTH, HEIGHT = 400, 400
        SPEED = 2

        SCREEN = None
        FPS = None

    class Colors:
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        ASPHALT = (49, 49, 49)
        RED = (255, 0, 0)
        RAND_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 200)

        currCellC = (100, 0, 255, 125)
        trailCellC = (255, 0, 255, 100)
        backtracking = (150, 255, 0, 255)

    def __init__(self, rows=None, cols=None, size=None, borderCoords=20):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.borderCoords = borderCoords

        self.border = None
