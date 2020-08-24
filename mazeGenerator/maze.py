

class Maze:
    def __init__(self, rows=None, cols=None, size=None, borderCoords=20):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.borderCoords = borderCoords

        self.border = None
