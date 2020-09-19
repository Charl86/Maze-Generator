

class Grid:
    def __init__(self, width=None, height=None):
        self.width = width
        self.height = height

        self.elements = []

    def append(self):
        self.elements.append

    def __getitem__(self, key):
        return self.elements[key]

    def __contains__(self, item):
        return item in self.elements
