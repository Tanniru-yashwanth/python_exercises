import pygame
from settings import Settings


class Rock:
    def __init__(self, rg_game):
        self.screen = rg_game.screen
        self.screen_rect = rg_game.screen.get_rect()
        self.img = pygame.image.load("images/rocket.bmp")
        self.img_rect = self.img.get_rect()
        self.settings = Settings()

        self.img_rect.center = self.screen_rect.center
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.speed = float(self.settings.image_speed)

    def update(self):
        if self.moving_right and self.img_rect.right < self.screen_rect.right:
            self.img_rect.x += self.speed
        elif self.moving_left and self.img_rect.left > self.screen_rect.left:
            self.img_rect.x -= self.speed
        elif self.moving_up and self.img_rect.top > self.screen_rect.top:
            self.img_rect.y -= self.speed
        elif self.moving_down and self.img_rect.bottom < self.screen_rect.bottom:
            self.img_rect.y += self.speed



    def blitme(self):
        self.screen.blit(self.img, self.img_rect)
