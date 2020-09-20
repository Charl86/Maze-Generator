

class Grid:
    def __init__(self):
        self.elements = []

    @property
    def width(self):
        return len(self.elements[0])

    @property
    def height(self):
        return len(self.elements)

    def append(self):
        self.elements.append

    def __getitem__(self, key):
        return self.elements[key]

    def __contains__(self, item):
        return item in self.elements
