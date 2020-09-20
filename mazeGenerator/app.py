from mazeGenerator.maze.settings import Settings
from mazeGenerator.interface.tkinterWin import TkMenu
from mazeGenerator.maze.generator import Generator


class App:
    def __init__(self):
        self.mSettings = Settings(speed=30)
        self.tkinterWin = TkMenu(self.mSettings)
        self.generator = Generator(self.mSettings)

    def run(self, debug=False):
        self.tkinterWin.loop()

        if not debug:
            self.generator.run()
