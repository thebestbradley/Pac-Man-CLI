## food.py
import pygame


class Food:
    """
    Represents the food that the player collects.

    Attributes:
        x (int): The x-coordinate of the food.
        y (int): The y-coordinate of the food.
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self, surface) -> None:
        """
        Draw the food on the given surface.

        Args:
            surface: The surface to draw the food on.
        """
        pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.x, self.y, 10, 10))
