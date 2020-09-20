import random


class PyGv:
    def __init__(self, width=400, height=0, speed=30):
        self.WIDTH, self.HEIGHT = width, height
        self.SPEED = speed

        self.SCREEN = None
        self.FPS = None


class Colors:
    def __init__(self):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.ASPHALT = (49, 49, 49)
        self.RED = (255, 0, 0)
        self.RAND_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 200)

        self.currCellC = (100, 0, 255, 125)
        self.trailCellC = (255, 0, 255, 100)
        self.backtracking = (150, 255, 0, 255)


class Settings:
    def __init__(self, rows=None, cols=None, size=None, borderCoords=20, speed=30):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.borderCoords = borderCoords

        self.PyGv = PyGv(speed=speed)
        self.Colors = Colors()
