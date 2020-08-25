from mazeGenerator.maze import mazeSettings
from mazeGenerator.interface.tkinterWin import TkMenu
from mazeGenerator.maze.generator import Generator


class App:
    def __init__(self):
        self.mSettings = mazeSettings
        self.tkinterWin = TkMenu(self.mSettings)
        self.generator = Generator(self.mSettings)

    def run(self, debug=False):
        self.tkinterWin.loop()

        if not debug:
            self.generator.run()
