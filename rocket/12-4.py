"""Make a game that begins with a rocket in the center of the
screen. Allow the player to move the rocket up, down, left, or right using the
four arrow keys. Make sure the rocket never moves beyond any edge of the
screen."""
import pygame
import sys
from rocket import Rock
from settings import Settings


class Rocket:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.display_wide, self.settings.display_height))
        self.bg_color = self.settings.background_color
        self.rocket = Rock(self)
        pygame.display.set_caption("ROCKET")

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._key_down(event)
            elif event.type == pygame.KEYUP:
                self._key_up(event)

    def _key_down(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True

    def _key_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    rg = Rocket()
    rg.run_game()
