import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """a class to manage the ship"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """load the image and get its rect"""
        self.image = pygame.image.load("images/boat.bmp")
        self.rect = self.image.get_rect()

        """start the new ship at the bottom center of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        # store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)
        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
