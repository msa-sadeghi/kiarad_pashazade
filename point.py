import pygame
from pygame.sprite import Sprite


class Cat(Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(600, 400))
        self.alive = True

    def update(self, player_rect):
        if player_rect.colliderect(self.rect):
            self.kill()
            self.alive = False
