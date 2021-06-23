"""Make a game that begins with a rocket in the center of the
screen. Allow the player to move the rocket up, down, left, or right using the
four arrow keys. Make sure the rocket never moves beyond any edge of the
screen."""
import pygame
import sys


class Rocket:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("ROCKET")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == "__main":
    rg = Rocket()
    rg.run_game()
