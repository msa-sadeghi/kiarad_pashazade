from pygame.sprite import Sprite
import pygame
import random
class Alien(Sprite):
    def __init__(self, image, x,y, speed, damage):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = speed
        self.damage = damage

    def move(self):
        self.rect.y += self.speed
        if self.rect.bottom >= 640:
            self.rect.x = random.randint(50, 900)
            self.rect.y= 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)