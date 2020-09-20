from mazeGenerator.maze.settings import Settings
from mazeGenerator.interface.tkinterWin import TkMenu
from mazeGenerator.maze.generator import Generator


# App class
class App:
    def __init__(self):
        self.mSettings = Settings(speed=15)  # Initialize Settings object.
        self.tkinterWin = TkMenu(self.mSettings)  # Initialize Tkinter Menu object.
        self.generator = Generator(self.mSettings)  # Initialize [Maze] Generator object.

    # Runs app.
    def run(self, debug=False):
        self.tkinterWin.loop()  # Start Tkinter Menu Window loop.

        if not debug:  # If not debugging Tk window, run generator.
            self.generator.run()
