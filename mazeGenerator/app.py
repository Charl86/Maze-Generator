from mazeGenerator.maze.settings import Settings
from mazeGenerator.interface.tkinterWin import TkMenu
from mazeGenerator.maze.generator import Generator


# App class
class App:
    def __init__(self):
        # Initialize Settings object.
        self.mSettings = Settings(speed=4)

        # Initialize Tkinter Menu object.
        self.tkinterWin = TkMenu(self.mSettings)

        # Initialize [Maze] Generator object.
        self.generator = Generator(
            self.mSettings, canvasC=self.mSettings.Colors.WHITE, wallC=self.mSettings.Colors.BLACK,
            trailCellC=(0, 150, 255), currCellC=(255, 0, 255), backtC=(255, 255, 0)
        )

    # Runs app.
    def run(self, debug=False):
        self.tkinterWin.loop()  # Start Tkinter Menu Window loop.

        if not debug:  # If not debugging Tk window, run generator.
            self.generator.run()
