class Player:
    """
    Represents the player character.

    Attributes:
        x (int): The x-coordinate of the player.
        y (int): The y-coordinate of the player.
        dx (int): The change in x-coordinate of the player.
        dy (int): The change in y-coordinate of the player.
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def move(self, dx: int, dy: int) -> None:
        """
        Move the player by dx and dy.

        Args:
            dx (int): The change in x-coordinate of the player.
            dy (int): The change in y-coordinate of the player.
        """
        self.dx = dx
        self.dy = dy
        self.x += dx
        self.y += dy

    def collide(self, other) -> bool:
        """
        Check if the player collides with the other object.

        Args:
            other: The other object to check for collision.

        Returns:
            bool: True if the player collides with the other object, False otherwise.
        """
        return self.x == other.x and self.y == other.y
