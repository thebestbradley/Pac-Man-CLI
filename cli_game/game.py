import pygame
from player import Player
from food import Food


class Game:
    def __init__(self, width: int, height: int):
        self.score = 0
        self.width = width
        self.height = height
        self.player = Player(width // 2, height // 2)
        self.food = Food(0, 0)
        self.paused = False

    def start_game(self):
        """
        Starts the game.
        """
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("CLI Game")
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return

                    if event.key == pygame.K_p:
                        self.pause_game()

                    if event.key == pygame.K_r:
                        self.restart_game()

            if not self.paused:
                screen.fill((0, 0, 0))

                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.player.move(-1, 0)
                if keys[pygame.K_RIGHT]:
                    self.player.move(1, 0)
                if keys[pygame.K_UP]:
                    self.player.move(0, -1)
                if keys[pygame.K_DOWN]:
                    self.player.move(0, 1)

                self.food.draw(screen)
                if self.player.collide(self.food):
                    self.score += 1
                    self.food = Food(0, 0)

                self.update_score(screen)
                if self.check_game_over(screen):
                    return

                pygame.display.flip()

            clock.tick(60)

    def pause_game(self):
        """
        Pauses the game.
        """
        self.paused = True

    def resume_game(self):
        """
        Resumes the game.
        """
        self.paused = False

    def restart_game(self):
        """
        Restarts the game.
        """
        self.score = 0
        self.player = Player(self.width // 2, self.height // 2)
        self.food = Food(0, 0)
        self.paused = False

    def end_game(self):
        """
        Ends the game.
        """
        pygame.quit()

    def update_score(self, screen):
        """
        Updates the score on the screen.
        """
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def check_game_over(self, screen):
        """
        Checks if the game is over.
        """
        if self.player.x < 0 or self.player.x >= self.width or self.player.y < 0 or self.player.y >= self.height:
            font = pygame.font.Font(None, 36)
            game_over_text = font.render("Game Over", True, (255, 255, 255))
            screen.blit(game_over_text, (self.width // 2 - 80, self.height // 2 - 18))
            pygame.display.flip()
            pygame.time.wait(2000)
            return True

        return False
