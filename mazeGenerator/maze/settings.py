import random
import colorsys


class PyGv:
    def __init__(self, **kwargs):
        self.WIDTH, self.HEIGHT = 400, 400
        self.SPEED = 30

        self.SCREEN = None
        self.FPS = None

        for key in kwargs:
            if key.upper() in self.__dict__:
                self.__dict__[key.upper()] = kwargs[key]
            elif key in self.__dict__:
                self.__dict__[key] = kwargs[key]


class Colors:
    def __init__(self, **kwargs):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.ASPHALT = (49, 49, 49)
        self.RED = (255, 0, 0)

        self.currCellC = (100, 0, 255, 125)
        self.trailCellC = (255, 0, 255, 100)
        self.backtracking = (150, 255, 0, 255)

        for key in kwargs:
            if key.upper() in self.__dict__:
                self.__dict__[key.upper()] = kwargs[key]
            elif key in self.__dict__:
                self.__dict__[key] = kwargs[key]

    @property
    def rand_color(self):
        return tuple(round(255 * i) for i in colorsys.hsv_to_rgb(random.uniform(0, 1), 1, 1))


class Settings:
    def __init__(self, rows=None, cols=None, size=None, borderCoords=20, **kwargs):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.borderCoords = borderCoords

        self.PyGv = PyGv(**kwargs)
        self.Colors = Colors(**kwargs)


if __name__ == "__main__":
    my_settings = Settings(speed=-1)
