import pygame


# The Wall class
class Wall:
    # Takes arguments A and B which are expected to be tubles representing a starting
    # and ending point. Also recieves a boolean argument that determines whether the
    # wall should be drawn or not. Receives settings for customizations.
    def __init__(self, A, B, mSettings, on=True):
        self.A, self.B = A, B
        # Validating that tuples are actually given as A and B.
        if not isinstance(self.A, tuple) or not isinstance(self.B, tuple):
            raise TypeError("Tuple objects were expected for A and B but instead at least"
                            "one of them is not.")

        self.mSettings = mSettings
        self.on = on

        # The color of the walls.
        self.color = self.mSettings.Colors.WHITE

    # Method that draws a wall using thickness parameter for thickness.
    def show(self, thickness):
        if self.on:  # If wall is turned on
            # Draw wall
            pygame.draw.line(self.mSettings.PyGv.SCREEN, self.color, self.A, self.B, thickness)
